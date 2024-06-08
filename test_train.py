import Calldict
import DatasetCHK
from GenerateCompileFile import CompileInfo
from GenerateModelFile import ModelInfo
from GeneratePreprocessFile import PreprocessInfo
from GenerateDataset import DatasetInfo






if __name__ == '__main__':

    img_info = (256, 256, 3)
    
    model_dic = {
        'Input0000': {
            'shape': img_info,
            'batch_size': None
        },
        'Conv2D0001': {
            'filters': 64,
            'kernel_size': (3, 3),
            'strides': (1, 1),
            'padding': '\'valid\'',
            'data_format': None,
            'dilation_rate': (1, 1),
            'groups': 1,
            'activation': None,
            'use_bias': True,
            'kernel_initializer': '\'glorot_uniform\'',
            'bias_initializer': '\'zeros\'',
            'kernel_regularizer': None,
            'bias_regularizer': None,
            'activity_regularizer': None,
            'kernel_constraint': None,
            'bias_constraint': None
        },
        'Activation0002': {
            'activation':'\'relu\''
        },
        'Conv2D0003': {
            'filters': 128,
            'kernel_size': (3, 3),
            'strides': (1, 1),
            'padding': '\'valid\'',
            'data_format': None,
            'dilation_rate': (1, 1),
            'groups': 1,
            'activation': None,
            'use_bias': True,
            'kernel_initializer': '\'glorot_uniform\'',
            'bias_initializer': '\'zeros\'',
            'kernel_regularizer': None,
            'bias_regularizer': None,
            'activity_regularizer': None,
            'kernel_constraint': None,
            'bias_constraint': None
        },
        'Activation0004': {
            'activation':'\'relu\''
        },
        'MaxPooling2D0005': {
            'pool_size': (2, 2),
            'strides': None,
            'padding': '\'valid\'',
            'data_format': None,
            'name': None
        },
        'GlobalAveragePooling2D0006': {
            'data_format': None,
            'keepdims': False
        },
        'Dense0007': {
            'units': 3,
            'use_bias': True,
            'kernel_initializer': '\'glorot_uniform\'',
            'bias_initializer': '\'zeros\'',
            'kernel_regularizer': None,
            'bias_regularizer': None,
            'activity_regularizer': None,
            'kernel_constraint': None,
            'bias_constraint': None
        },
        'Activation0008': {
            'activation':'\'softmax\''
        }
    }
    compile_dic = {
        'optimizer':{
            'Adam':{
                'learning_rate':0.001,
                'beta_1':0.9,
                'beta_2':0.999,
                'epsilon':1e-07,
                'decay':0.01,
                'clipnorm':None,
                'clipvalue':None,
                'global_clipnorm':None
            }
        },
        'loss':{
            'CategoricalCrossentropy':{
                'from_logits':False,
                'label_smoothing':0.0,
                'axis':-1
            }
        },
        'metrics':{
            'Accuracy':{
                'name':"\'accuracy\'",
            }
        }
    }
    train_preprocess_dict = {
        'ImageDataGenerator': {
            'featurewise_center':False,
            'samplewise_center': False,
        },
        'flow_from_directory': {
            'target_size': (256, 256),
            'color_mode': '\'rgb\'',
            'class_mode': '\'categorical\'',
            'batch_size' : 32
        }
    }

    validation_preprocess_dict = {
        'ImageDataGenerator': {
            'featurewise_center':False,
            'samplewise_center': False,
        },
        'flow_from_directory': {
            'target_size': (256, 256),
            'color_mode': '\'rgb\'',
            'class_mode': '\'categorical\'',
            'batch_size' : 32
        }
    }

    test_preprocess_dict = {
        # 'ImageDataGenerator': {
        #     'featurewise_center':False,
        #     'samplewise_center': False,
        # },
        # 'flow_from_directory': {
        #     'target_size': (256, 256),
        #     'color_mode': '\'rgb\'',
        #     'class_mode': '\'categorical\'',
        #     'batch_size' : 32
        # }
    }

    part_dict = {'train':7, 'validation':3, 'test':0}
    model_info = ModelInfo()
    compile_info = CompileInfo()
    preprocess_info = PreprocessInfo()
    dataset_info = DatasetInfo()


    dataset_info.send(part_dict, r"C:\Users\yuuki\Documents\GUI_MLearning\GUI_MLearning-main\data3")
    preprocess_info.send(train_preprocess_dict, 'image', 'train', r'C:\Users\yuuki\Documents\GUI_MLearning\GUI_MLearning-main\dataset')
    preprocess_info.send(validation_preprocess_dict, 'image', 'validation', r'C:\Users\yuuki\Documents\GUI_MLearning\GUI_MLearning-main\dataset')
    preprocess_info.send(test_preprocess_dict, 'image', 'test', r'C:\Users\yuuki\Documents\GUI_MLearning\GUI_MLearning-main\dataset')
    model_info.send(model_dic)
    compile_info.send(compile_dic)

    import train_preprocess_info
    import validation_preprocess_info
    import test_preprocess_info
    import model_info
    import compile_info

    train_generator = train_preprocess_info.preprocess_info()
    validation_generator = validation_preprocess_info.preprocess_info()
    test_generator = test_preprocess_info.preprocess_info()

    model = model_info.model_build()

    optimizer_, loss_, metrics_ = compile_info.compile_build()

    epochs_ = 10

    model.compile(loss=loss_, optimizer=optimizer_, metrics=metrics_)

    model.fit(train_generator, validation_data=validation_generator, epochs=epochs_)


    
