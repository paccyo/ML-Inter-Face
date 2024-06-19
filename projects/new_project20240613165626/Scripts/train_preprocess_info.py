
from keras.preprocessing.image import *



def preprocess_info():
    ImageDataGenerator_train = ImageDataGenerator(featurewise_center=False, samplewise_center=False)
    flow_from_directory_train = ImageDataGenerator_train.flow_from_directory(r'C:\Users\zaq11\Pictures\data\train', target_size=(256, 256), color_mode='rgb')
    return flow_from_directory_train