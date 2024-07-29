from keras.models import Model
from keras.layers import *


def model_build():
    Input0000 = Input(shape=(4,))
    Dense0001 = Dense(units=32)(Input0000)
    Activation0002 = Activation(activation='relu')(Dense0001)
    Dense0003 = Dense(units=3)(Activation0002)
    Activation0004 = Activation(activation='softmax')(Dense0003)
    model = Model(inputs=Input0000, outputs=Activation0004)
    return model