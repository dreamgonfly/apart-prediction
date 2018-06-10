import pandas as pd
import numpy as np

import  keras
from keras.models import Sequential
from keras.layers import Conv1D, Flatten
from keras.layers import Input, Lambda
from keras import backend as K
from keras.models import Model

N_FEATURES = 20
N_TIME_WINDOW = 50
N_MONTH_TO_PREDICT = 6
INPUT_SHAPE = (N_FEATURES, N_TIME_WINDOW)



"""
merge two other neural networks
https://statcompute.wordpress.com/2017/01/08/an-example-of-merge-layer-in-keras/
https://nhanitvn.wordpress.com/2016/09/27/a-keras-layer-for-one-hot-encoding/
"""
def build_cnn():
    model = Sequential()
    model.add(Conv1D(32, kernel_size=(12), activation='relu', input_shape=INPUT_SHAPE))
    model.add(Conv1D(64, kernel_size=(6), activation='relu', input_shape=INPUT_SHAPE))
    model.add(Flatten() +)

def build_onehot():
    model = Sequential()
    model.add
