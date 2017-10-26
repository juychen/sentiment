# coding: utf-8

# In[24]:

#import pip

#package_name='shutil'
#pip.main(['install', package_name])

# In[1]:

import sys

import matplotlib as mp
import matplotlib.pyplot as plt
import numpy as np  # linear algebra
import pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)


from keras.layers import LSTM, Dense, Embedding, Conv2D, AveragePooling2D,Flatten
from keras.models import Sequential
from optparse import OptionParser

import CNN 

argvs = sys.argv

opts, args = {}, []

print(argvs)
print("##########")

def main():

    CID = opts.cluster

    if (opts.load != 'none'): CID = opts.load

    X_train, X_test, Y_train, Y_test, X, X2, X3, enc = CNN.get_data()

    model = CNN.bulid_model(
        X_train, X_test, Y_train, Y_test, X, X2, X3, CID, fromfile='weights_8212_0_.hdf5')

    model.pop()
    model.pop()
    model.pop()

    l = model.predict(X_train)

    print(model.summary())

    print (l.shape)


    return


if __name__ == "__main__":

    plt.switch_backend('agg')
    mp.use('Agg')

    op = OptionParser()
    op.add_option(
        '-c',
        '--cluster',
        action='store',
        type='string',
        dest='cluster',
        help='indicate the clusterid')
    op.add_option(
        '-d',
        '--date',
        action='store',
        type='string',
        dest='date',
        help='indicate the date')
    op.add_option(
        '-l',
        '--load',
        default='none',
        action='store',
        type='string',
        dest='load',
        help='load weight form file')
    (opts, args) = op.parse_args()
    if len(args) > 0:
        op.print_help()
        op.error('Please input options instead of arguments.')
        exit(1)

    main()