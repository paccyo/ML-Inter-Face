
from keras.preprocessing.image import *



def preprocess_info():
    ImageDataGenerator_validation = ImageDataGenerator()
    flow_from_directory_validation = ImageDataGenerator_validation.flow_from_directory(r'C:\Users\zaq11\Pictures\data\validation', target_size=(256, 256), color_mode='rgb')
    return flow_from_directory_validation