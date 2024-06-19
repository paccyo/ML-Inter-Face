from keras.models import Model
from keras.layers import *


def model_build():
    Input0000 = Input(shape=None, batch_size=None, dtype=None, sparse=False, batch_shape=None, name=None, tensor=None, detail_view='F')
    Dense0001 = Dense(units=(256, 256, 3), use_bias=(256, 256, 3), kernel_initializer=(256, 256, 3), bias_initializer=(256, 256, 3), kernel_regularizer=(256, 256, 3), bias_regularizer=(256, 256, 3), activity_regularizer=(256, 256, 3), kernel_constraint=(256, 256, 3), bias_constraint=(256, 256, 3), detail_view=(256, 256, 3))(Input0000)
    Activation0002 = Activation(activation=(256, 256, 3), detail_view=(256, 256, 3))(Dense0001)
    model = Model(inputs=Input0000, outputs=Activation0002)
    return model