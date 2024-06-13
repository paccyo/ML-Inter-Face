
from keras.preprocessing.image import *



def preprocess_info():
    ImageDataGenerator_test = ImageDataGenerator()
    flow_from_directory_test = ImageDataGenerator_test.flow_from_directory(r'C:\Users\zaq11\Pictures\data\test', target_size=(256, 256), color_mode='rgb')
    return flow_from_directory_test