from keras.models import Model
from keras.layers import *
from keras.optimizers import *
from keras.preprocessing.image import *
import tensorflow as tf
from keras.callbacks import ModelCheckpoint

def model_build():
    Dense0000 = Dense(units=0,use_bias=True,kernel_initializer='glorot_uniform',bias_initializer='zeros',kernel_regularizer=None,bias_regularizer=None,activity_regularizer=None,kernel_constraint=None,bias_constraint=None,lora_rank=None)
    Activation0000 = Activation(activation=None)(Dense0000)
    Conv2D0000 = Conv2D(filters=0,kernel_size=(0, 0),strides=(1, 1),padding='valid',data_format=None,dilation_rate=(1, 1),groups=1,activation=None,use_bias=True,kernel_initializer='glorot_uniform',bias_initializer='zeros',kernel_regularizer=None,bias_regularizer=None,activity_regularizer=None,kernel_constraint=None,bias_constraint=None)(Activation0000)
    Conv1D0000 = Conv1D(filters=0,kernel_size=0,strides=1,padding='valid',data_format=None,dilation_rate=1,groups=1,activation=None,use_bias=True,kernel_initializer='glorot_uniform',bias_initializer='zeros',kernel_regularizer=None,bias_regularizer=None,activity_regularizer=None,kernel_constraint=None,bias_constraint=None)(Conv2D0000)
    MaxPooling2D0000 = MaxPooling2D(pool_size=(2, 2),strides=None,padding='valid',data_format=None,name=None)(Conv1D0000)
    MaxPooling1D0000 = MaxPooling1D(pool_size=2,strides=None,padding='valid',data_format=None,name=None)(MaxPooling2D0000)
    Flatten0000 = Flatten(data_format=None)(MaxPooling1D0000)
    GlobalAveragePooling2D0000 = GlobalAveragePooling2D(data_format=None,keepdims=False)(Flatten0000)
    model = Model(inputs=Dense0000, outputs=GlobalAveragePooling2D0000)
    return model
