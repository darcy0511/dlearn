import os
import sys
import cPickle
import theano.tensor as T

homepath = os.path.join('..', '..')

if not homepath in sys.path:
    sys.path.insert(0, homepath)

from dlearn.models.layer import FullConnLayer, ConvPoolLayer
from dlearn.models.nnet import NeuralNet
from dlearn.utils import actfuncs, costfuncs
from dlearn.optimization import sgd


def load_data():
    with open('data.pkl', 'rb') as f:
        dataset = cPickle.load(f)

    return dataset


def scale_per_channel(F, consts, v_range=[-1, 1]):
    vmin, vmax = v_range
    fmin, fmax = F.min(axis=[2, 3]), F.max(axis=[2, 3])
    F = vmin + (vmax - vmin) * (F - fmin.dimshuffle(0, 1, 'x', 'x')) / \
        (fmax - fmin).dimshuffle(0, 1, 'x', 'x')
    consts.extend([fmin, fmax])
    return F


def train_model(dataset):
    X = T.tensor4()
    A = T.matrix()
    S = T.tensor3()

    filter_layers = []
    filter_layers.append(ConvPoolLayer(
        input=X,
        input_shape=(3, 160, 80),
        filter_shape=(32, 3, 5, 5),
        pool_shape=(2, 2),
        dropout_ratio=0.1,
        active_func=actfuncs.tanh,
        flatten=False
    ))

    weight_layers = []
    weight_layers.append(FullConnLayer(
        input=A,
        input_shape=11,
        output_shape=128,
        dropout_ratio=0.1,
        active_func=actfuncs.tanh
    ))

    weight_layers.append(FullConnLayer(
        input=weight_layers[-1].output,
        input_shape=weight_layers[-1].output_shape,
        output_shape=filter_layers[-1].output_shape[0],
        dropout_input=weight_layers[-1].dropout_output,
        active_func=actfuncs.tanh
    ))

    consts = []

    F = scale_per_channel(filter_layers[-1].output, consts)
    w = weight_layers[-1].output
    wF = (w.dimshuffle(0, 1, 'x', 'x') * F).sum(axis=1)
    wF = actfuncs.sigmoid(wF)

    F_dropout = scale_per_channel(filter_layers[-1].dropout_output, consts)
    w_dropout = weight_layers[-1].dropout_output
    wF_dropout = (w_dropout.dimshuffle(0, 1, 'x', 'x') * F_dropout).sum(axis=1)
    wF_dropout = actfuncs.sigmoid(wF_dropout)

    model = NeuralNet(filter_layers + weight_layers, [X, A], wF)
    model.target = S
    model.cost = costfuncs.binxent(wF_dropout.flatten(2), S.flatten(2)) + \
        1e-3 * model.get_norm(2)
    model.error = costfuncs.binerr(wF.flatten(2), S.flatten(2))
    model.consts = consts

    sgd.train(model, dataset, lr=1e-3, momentum=0.9,
              batch_size=100, n_epochs=300,
              epoch_waiting=10)

    return model


def save_model(model):
    with open('model_filterlc.pkl', 'wb') as f:
        cPickle.dump(model, f, cPickle.HIGHEST_PROTOCOL)


if __name__ == '__main__':
    dataset = load_data()
    model = train_model(dataset)
    save_model(model)
