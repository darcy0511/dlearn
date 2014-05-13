import os
import sys
import cPickle
import numpy as np
import theano
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


def pooling(fmaps):
    s = fmaps.sum(axis=[2, 3])
    # Z = T.nnet.sigmoid(fmaps).sum(axis=[2, 3])
    Z = abs(T.tanh(fmaps)).sum(axis=[2, 3])
    return s / Z


def train_model(dataset):
    X = T.tensor4()
    A = T.matrix()
    S = T.tensor3()

    layers = []
    layers.append(ConvPoolLayer(
        input=X * S.dimshuffle(0, 'x', 1, 2),
        input_shape=(3, 160, 80),
        filter_shape=(32, 3, 5, 5),
        pool_shape=(2, 2),
        active_func=actfuncs.tanh,
        flatten=False,
        b=0.0
    ))

    layers.append(ConvPoolLayer(
        input=layers[-1].output,
        input_shape=layers[-1].output_shape,
        filter_shape=(64, 32, 5, 5),
        pool_shape=(2, 2),
        active_func=actfuncs.tanh,
        flatten=False,
        b=0.0
    ))

    layers.append(ConvPoolLayer(
        input=layers[-1].output,
        input_shape=layers[-1].output_shape,
        filter_shape=(128, 64, 3, 3),
        pool_shape=(2, 2),
        active_func=actfuncs.tanh,
        flatten=False,
        b=0.0
    ))

    F = pooling(layers[-1].output)

    layers.append(FullConnLayer(
        input=F,
        input_shape=layers[-1].output_shape[0],
        output_shape=64,
        dropout_ratio=0.1,
        active_func=actfuncs.tanh
    ))

    layers.append(FullConnLayer(
        input=layers[-1].output,
        input_shape=layers[-1].output_shape,
        output_shape=11,
        dropout_input=layers[-1].dropout_output,
        active_func=actfuncs.sigmoid
    ))

    model = NeuralNet(layers, [X, S], layers[-1].output)
    model.target = A
    model.cost = costfuncs.binxent(layers[-1].dropout_output, A) + \
        1e-3 * model.get_norm(2)
    model.error = costfuncs.binerr(layers[-1].output, A)

    sgd.train(model, dataset, lr=1e-2, momentum=0.9,
              batch_size=100, n_epochs=300,
              epoch_waiting=10)

    return model


def save_model(model):
    with open('model_scpool.pkl', 'wb') as f:
        cPickle.dump(model, f, cPickle.HIGHEST_PROTOCOL)


if __name__ == '__main__':
    dataset = load_data()
    model = train_model(dataset)
    save_model(model)