import train_preprocess_info
import validation_preprocess_info
import test_preprocess_info
import model_info
import compile_info
import matplotlib.pyplot as plt
import keras
import japanize_matplotlib


def run():
    train_generator = train_preprocess_info.preprocess_info()
    validation_generator = validation_preprocess_info.preprocess_info()
    test_generator = test_preprocess_info.preprocess_info()

    model = model_info.model_build()

    optimizer_, loss_, metrics_ = compile_info.compile_build()

    epochs_ = 10

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