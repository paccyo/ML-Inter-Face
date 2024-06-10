import Calldict
import DatasetCHK
from GenerateCompileFile import CompileInfo
from GenerateModelFile import ModelInfo
from GeneratePreprocessFile import PreprocessInfo
from GenerateDataset import DatasetInfo
import matplotlib.pyplot as plt
import keras
import japanize_matplotlib





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
                # 'clipnorm':None,
                # 'clipvalue':None,
                # 'global_clipnorm':None
            }
        },
        'loss':['\'categorical_crossentropy\''],
        'metrics':['\'acc\'']
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

    # データの分割率
    part_dict = {'train':7, 'validation':3, 'test':0}
    # エポック指定
    epochs_ = 10


    
    # インスタンス化
    model_info = ModelInfo()
    compile_info = CompileInfo()
    preprocess_info = PreprocessInfo()
    dataset_info = DatasetInfo()

    # データの送信
    dataset_info.send(part_dict, r"C:\Users\yuuki\Documents\GUI_MLearning\GUI_MLearning-main\data3")
    preprocess_info.send(train_preprocess_dict, 'image', 'train', r'C:\Users\yuuki\Documents\GUI_MLearning\GUI_MLearning-main\dataset')
    model_info.send(model_dic)
    compile_info.send(compile_dic)

    import train_preprocess_info
    import validation_preprocess_info
    import test_preprocess_info
    import model_info
    import compile_info

    if part_dict['train'] != 0:
        train_generator = train_preprocess_info.preprocess_info()
    if part_dict['validation'] != 0:
        validation_generator = validation_preprocess_info.preprocess_info()
    if part_dict['test'] != 0:
        test_generator = test_preprocess_info.preprocess_info()

    model = model_info.model_build()

    optimizer_, loss_, metrics_ = compile_info.compile_build()


    model.summary()

    acc_hist = []
    val_acc_hist = []
    loss_hist = []
    val_loss_hist = []

    class PlotCallback(keras.callbacks.Callback):
        def on_epoch_end(self, batch, logs=None):
            acc_hist.append(logs['acc'])
            val_acc_hist.append(logs['val_acc'])
            loss_hist.append(logs['loss'])
            val_loss_hist.append(logs['val_loss'])
            plt.figure()
            plt.plot(acc_hist, label='スコア（学習データ）')
            plt.plot(val_acc_hist, label='スコア（検証データ）')
            plt.xlabel('Epoch')
            plt.ylabel(f'{metrics_}')
            plt.title('評価スコア')
            plt.legend()
            plt.savefig(f'metrics.png')
            plt.figure()
            plt.plot(acc_hist, label='スコア（学習データ）')
            plt.plot(val_acc_hist, label='スコア（検証データ）')
            plt.xlabel('Epoch')
            plt.ylabel(f'{loss_}')
            plt.title('損失スコア')
            plt.legend()
            plt.savefig(f'loss.png')
            

    model.compile(loss=loss_, optimizer=optimizer_, metrics=metrics_)

    plot_callback = PlotCallback()

    model.fit(train_generator, validation_data=validation_generator, epochs=epochs_, callbacks=[plot_callback])

    
    print('end')