import train_preprocess_info
import validation_preprocess_info
import test_preprocess_info
import model_info
import compile_info
import matplotlib.pyplot as plt
import keras
import japanize_matplotlib
import sys

print('RunTrainfile')

def run(part_dict, data_type, epochs, batchs=None, project_path=None):

    if data_type == 'image':
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
                plt.savefig(f'{project_path}/metrics.png')
                plt.figure()
                plt.plot(acc_hist, label='スコア（学習データ）')
                plt.plot(val_acc_hist, label='スコア（検証データ）')
                plt.xlabel('Epoch')
                plt.ylabel(f'{loss_}')
                plt.title('損失スコア')
                plt.legend()
                plt.savefig(f'{project_path}/loss.png')
        
        if part_dict['train'] != 0:
            train_generator = train_preprocess_info.preprocess_info()
        if part_dict['validation'] != 0:
            validation_generator = validation_preprocess_info.preprocess_info()
        if part_dict['test'] != 0:
            test_generator = test_preprocess_info.preprocess_info()

        model = model_info.model_build()

        optimizer_, loss_, metrics_ = compile_info.compile_build()

        model.compile(loss=loss_, optimizer=optimizer_, metrics=metrics_)

        plot_callback = PlotCallback()

        model.fit(train_generator, validation_data=validation_generator, epochs=epochs, callbacks=[plot_callback])

    elif data_type == 'text':
        pass




part_dict, data_type, epochs, batchs, project_path = sys.argv[0], sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
run(part_dict, data_type, epochs, batchs, project_path)