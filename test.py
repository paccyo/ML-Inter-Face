
from keras import models
from keras import layers
from keras.datasets import mnist
from keras.utils import to_categorical


(train_data, train_label), (test_data, test_label) = mnist.load_data()
train_data = train_data.reshape(60000, 28*28)
test_data = test_data.reshape(10000, 28*28)
train_data = train_data.astype('float32') / 255
test_data = test_data.astype('float32') / 255
train_label = to_categorical(train_label, 10)
test_label = to_categorical(test_label, 10)
model = models.Sequential()
model.add(layers.Dense(512, activation='relu', input_shape=(28*28,)))
model.add(layers.Dropout(0.2))
model.add(layers.Dense(256))
model.add(layers.Dropout(0.5))
model.add(layers.Dense(10, activation='softmax'))
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(train_data, train_label, epochs=1, batch_size=64)
loss, acc = model.evaluate(test_data,test_label)

