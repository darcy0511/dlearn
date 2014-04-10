import os
import sys
import cPickle
import theano.tensor as T

homepath = '..'
if not homepath in sys.path:
    sys.path.insert(0, homepath)

from dlearn.data.dataset import Dataset
from dlearn.models.layer import FullConnLayer, ConvPoolLayer
from dlearn.models.nnet import NeuralNet
from dlearn.utils import actfuncs, costfuncs
from dlearn.utils.math import create_shared
from dlearn.optimization import sgd


def load_data():
    fpath = os.path.join('..', 'data', 'mnist', 'mnist.pkl')

    with open(fpath, 'rb') as f:
        train_set, valid_set, test_set = cPickle.load(f)

    dataset = Dataset()

    dataset.train_x = create_shared(
        train_set[0].reshape(train_set[0].shape[0], 1, 28, 28))
    dataset.train_y = create_shared(train_set[1], 'int32')

    dataset.valid_x = create_shared(
        valid_set[0].reshape(valid_set[0].shape[0], 1, 28, 28))
    dataset.valid_y = create_shared(valid_set[1], 'int32')

    dataset.test_x = create_shared(
        test_set[0].reshape(test_set[0].shape[0], 1, 28, 28))
    dataset.test_y = create_shared(test_set[1], 'int32')

    return dataset


def train_model(dataset):
    X = T.tensor4()
    Y = T.ivector()

    layers = []
    layers.append(ConvPoolLayer(
        input=X,
        input_shape=(1, 28, 28),
        filter_shape=(20, 1, 5, 5),
        pool_shape=(2, 2),
        active_func=actfuncs.tanh
    ))

    layers.append(ConvPoolLayer(
        input=layers[-1].output,
        input_shape=layers[-1].output_shape,
        filter_shape=(50, 20, 5, 5),
        pool_shape=(2, 2),
        active_func=actfuncs.tanh,
        flatten=True
    ))

    layers.append(FullConnLayer(
        input=layers[-1].output,
        input_shape=layers[-1].output_shape,
        output_shape=500,
        active_func=actfuncs.tanh
    ))

    layers.append(FullConnLayer(
        input=layers[-1].output,
        input_shape=layers[-1].output_shape,
        output_shape=10,
        active_func=actfuncs.softmax
    ))

    model = NeuralNet(layers, X, layers[-1].output)
    model.target = Y
    model.cost = costfuncs.neglog(layers[-1].output, Y)
    model.error = costfuncs.miscls_rate(layers[-1].output, Y)

    sgd.train(model, dataset, lr=0.1, momentum=0.9,
              batch_size=500, n_epochs=200,
              lr_decr=1.0)

    return model


def save_model(model):
    with open('model.pkl', 'wb') as f:
        cPickle.dump(model, f, cPickle.HIGHEST_PROTOCOL)


if __name__ == '__main__':
    dataset = load_data()
    model = train_model(dataset)
    save_model(model)
