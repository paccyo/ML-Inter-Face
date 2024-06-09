import train_preprocess_info
import validation_preprocess_info
import test_preprocess_info
import model_info
import compile_info
import matplotlib.pyplot as plt
import keras


def run():
    train_generator = train_preprocess_info.preprocess_info()
    validation_generator = validation_preprocess_info.preprocess_info()
    test_generator = test_preprocess_info.preprocess_info()

    model = model_info.model_build()

    optimizer_, loss_, metrics_ = compile_info.compile_build()

    epochs_ = 10

    model.summary()

    accuracy_history = []

    class PlotCallback(keras.callbacks.Callback):
        def on_epoch_end(self, logs=None):
            accuracy_history.append(logs['acc'])
            plt.figure()
            plt.plot(accuracy_history, label='Accuracy')
            plt.xlabel('Epoch')
            plt.ylabel('Accuracy')
            plt.title('Training Accuracy')
            plt.legend()
            plt.show()

    model.compile(loss=loss_, optimizer=optimizer_, metrics=metrics_)

    plot_callback = PlotCallback()

    model.fit(train_generator, validation_data=validation_generator, epochs=epochs_, callbacks=[plot_callback])