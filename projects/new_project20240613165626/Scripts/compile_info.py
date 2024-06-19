from keras.optimizers import *


def compile_build():
    optimizer = Adam(learning_rate=0.001)
    loss = 'categorical_crossentropy'
    metrics = 'acc'
    return optimizer, loss, metrics