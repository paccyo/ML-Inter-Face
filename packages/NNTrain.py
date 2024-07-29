
import model_info
import compile_info
import matplotlib.pyplot as plt
from keras.callbacks import Callback
import japanize_matplotlib
import sys
import os
import glob
import pandas as pd
from keras.utils import to_categorical


print('RunTrainfile')

def run(train_part, validation_part, test_part, data_type, epochs, batchs=None, project_path=None, dataset_path=None, class_nums=None, train_type=None):
    """
    NN学習を実行します

    Parameters
    ----------
    train_part:str -> 学習データの割合
    validation_part:str -> 検証データの割合
    test_part:str -> テストデータの割合
    data_type:str -> image or dataframe
    epochs:str -> エポック数
    batchs:str -> バッチサイズ
    project_path:str -> 結果を保存したいディレクトリパス
    dataset_path:str -> データセットのパス
    class_nums:str -> 分類クラス数
    train_type:str -> classfier or reg
    """
    if data_type == 'image':
        import train_preprocess_info
        import validation_preprocess_info
        import test_preprocess_info
    train_part = int(train_part)
    validation_part = int(validation_part)
    test_part = int(test_part)
    epochs = int(epochs)
    batchs = int(batchs)
    class_nums = int(class_nums)
    acc_hist = []
    val_acc_hist = []
    loss_hist = []
    val_loss_hist = []
    class PlotCallback(Callback):
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
            plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
            os.remove(f'{project_path}/metrics_{len(acc_hist)-1}epoch.png')
            plt.savefig(f'{project_path}/metrics_{len(acc_hist)}epoch.png', bbox_inches='tight')
            plt.figure()
            plt.plot(loss_hist, label='スコア（学習データ）')
            plt.plot(val_loss_hist, label='スコア（検証データ）')
            plt.xlabel('Epoch')
            plt.ylabel(f'{loss_}')
            plt.title('損失スコア')
            plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
            os.remove(f'{project_path}/loss_{len(loss_hist)-1}epoch.png')
            plt.savefig(f'{project_path}/loss_{len(loss_hist)}epoch.png', bbox_inches='tight')
    if data_type == "image":
        if train_part != 0:
            train_generator = train_preprocess_info.preprocess_info()
        if validation_part != 0:
            validation_generator = validation_preprocess_info.preprocess_info()
        if test_part != 0:
            test_generator = test_preprocess_info.preprocess_info()

        model = model_info.model_build()

        optimizer_, loss_, metrics_ = compile_info.compile_build()

        model.compile(loss=loss_, optimizer=optimizer_, metrics=metrics_)

        plot_callback = PlotCallback()

        model.fit(train_generator, validation_data=validation_generator, epochs=epochs, callbacks=[plot_callback])

        model.save(f'{project_path}/trained_model.h5')

    elif data_type == 'dataframe':
        for csv_path in glob.glob(os.path.join(dataset_path, '*.*')):
            print(csv_path)
            dataset_type, data_or_target = os.path.splitext(os.path.basename(csv_path))[0].split('_')[0], os.path.splitext(os.path.basename(csv_path))[0].split('_')[1]
            print(dataset_type, data_or_target)
            if dataset_type == 'train' and data_or_target == 'data':
                df_train_data = pd.read_csv(csv_path)
            elif dataset_type == 'train' and data_or_target == 'target':
                df_train_target = pd.read_csv(csv_path)
            elif dataset_type == 'validation' and data_or_target == 'data':
                df_valdation_data = pd.read_csv(csv_path)
            elif dataset_type == 'validation' and data_or_target == 'target':
                df_validation_target = pd.read_csv(csv_path)
            elif dataset_type == 'test' and data_or_target == 'data':
                df_test_data = pd.read_csv(csv_path)
            elif dataset_type == 'test' and data_or_target == 'target':
                df_test_target = pd.read_csv(csv_path)

        print(type(train_type))
        print(train_part,validation_part,test_part)
        if train_type == 'categorical':
            if train_part != 0:
                train_target = conv_str_to_int(df_train_target.values)
                train_target = to_categorical(train_target, num_classes=class_nums)
            elif validation_part != 0:
                validation_target = conv_str_to_int(df_validation_target.values)
                validation_target = to_categorical(validation_target, num_classes=class_nums)
            elif test_part != 0:
                test_target = conv_str_to_int(df_test_target.values)
                test_target = to_categorical(test_target, num_classes=class_nums)
        else:
            if train_part != 0:
                train_target = conv_str_to_int(df_train_target.values)
            elif validation_part != 0:
                validation_target = conv_str_to_int(df_validation_target.values)
            elif test_part != 0:
                test_target = conv_str_to_int(df_test_target.values)

        model = model_info.model_build()

        optimizer_, loss_, metrics_ = compile_info.compile_build()

        model.compile(loss=loss_, optimizer=optimizer_, metrics=metrics_)

        plot_callback = PlotCallback()

        model.fit(df_train_data.values, train_target, validation_data=(df_valdation_data.values, validation_target),
                  epochs=epochs, batchs=batchs, callbacks=[plot_callback])

        model.save(f'{project_path}/trained_model.h5')
        
def conv_str_to_int(df_target):
    """
    dataframeの文字を数値化
    """
    labels_str = []
    labels = []
    for data in df_target:
        if data not in labels_str:
            labels_str.append(data)
    for data in df_target:
        labels.append(labels_str.index(data))
    return labels

_, train_part, validation_part, test_part, data_type, epochs, batchs, project_path, dataset_path, class_nums, train_type = sys.argv[0], sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6], sys.argv[7], sys.argv[8], sys.argv[9], sys.argv[10]
run(train_part, validation_part, test_part, data_type, epochs, batchs, project_path, dataset_path, class_nums, train_type)