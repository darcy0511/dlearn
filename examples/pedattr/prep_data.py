import os
import sys
import numpy as np

homepath = os.path.join('..', '..')

if not homepath in sys.path:
    sys.path.insert(0, homepath)

import conf


def load_rawdata():
    from scipy.io import loadmat

    rawdata = []
    for dname in conf.datasets:
        fpath = os.path.join(homepath, 'data', 'pedattr', dname)
        matdata = loadmat(fpath)

        m, n = matdata['images'].shape
        for i in xrange(m):
            for j in xrange(n):
                if matdata['images'][i, j].size == 0:
                    break
                rawdata.append((matdata['images'][i, j],
                                matdata['attributes'][i, 0].ravel()))

    return rawdata


def create_dataset(rawdata):
    from dlearn.data.dataset import Dataset
    from dlearn.utils import imgproc

    def imgprep(img):
        img = imgproc.resize(img, (80, 30))
        img = imgproc.subtract_luminance(img)
        img = np.rollaxis(img, 2)
        return img.ravel()

    m = len(rawdata)
    X = [0] * m
    Y = [0] * m

    for i, (img, attr) in enumerate(rawdata):
        X[i] = imgprep(img)
        Y[i] = attr

    X = np.asarray(X)
    Y = np.asarray(Y)

    X = np.tanh(X - X.mean(axis=0))

    dataset = Dataset(X, Y)
    dataset.split(0.7, 0.2)

    return dataset


def save_dataset(dataset):
    import cPickle

    with open('data.pkl', 'wb') as f:
        cPickle.dump(dataset, f, cPickle.HIGHEST_PROTOCOL)

if __name__ == '__main__':
    rawdata = load_rawdata()
    dataset = create_dataset(rawdata)
    save_dataset(dataset)
