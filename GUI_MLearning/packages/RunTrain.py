import train_preprocess_info
import validation_preprocess_info
import test_preprocess_info
import model_info
import compile_info
import matplotlib.pyplot as plt
import keras
import japanize_matplotlib
import sys
import os

print('RunTrainfile')

def run(train_part, validation_part, test_part, data_type, epochs, batchs=None, project_path=None):
    train_part = int(train_part)
    validation_part = int(validation_part)
    test_part = int(test_part)
    epochs = int(epochs)
    batchs = int(batchs)
    if data_type == "image":
        print(data_type)
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
                plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
                os.remove(f'{project_path}/metrics_{len(acc_hist)-1}epoch.png')
                plt.savefig(f'{project_path}/metrics_{len(acc_hist)}epoch.png', bbox_inches='tight')
                plt.figure()
                plt.plot(acc_hist, label='スコア（学習データ）')
                plt.plot(val_acc_hist, label='スコア（検証データ）')
                plt.xlabel('Epoch')
                plt.ylabel(f'{loss_}')
                plt.title('損失スコア')
                plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
                os.remove(f'{project_path}/loss_{len(loss_hist)-1}epoch.png')
                plt.savefig(f'{project_path}/loss_{len(loss_hist)}epoch.png', bbox_inches='tight')
        
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

        model.save('trained_model.h5')

    elif data_type == 'text':
        pass




_, train_part, validation_part, test_part, data_type, epochs, batchs, project_path = sys.argv[0], sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6], sys.argv[7]
run(train_part, validation_part, test_part, data_type, epochs, batchs, project_path)