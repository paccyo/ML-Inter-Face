import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from keras.models import Sequential
from keras.layers import Dense
from keras.utils import to_categorical

# データのロード
iris = load_iris()
X = iris.data
y = iris.target

# ラベルをOne-Hotエンコーディング
y = to_categorical(y, num_classes=3)

# データの分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 特徴量の標準化
# scaler = StandardScaler()
# X_train = scaler.fit_transform(X_train)
# X_test = scaler.transform(X_test)

# モデルの構築
# model = Sequential()
# model.add(Dense(10, input_shape=(X_train.shape[1],), activation='relu'))
# model.add(Dense(10, activation='relu'))
# model.add(Dense(3, activation='softmax'))

from keras.models import Model
from keras.layers import *

def model_build():
    Input0000 = Input(shape=(4,))
    Dense0001 = Dense(units=10)(Input0000)
    Activation0002 = Activation(activation='relu')(Dense0001)
    Dense0003 = Dense(units=10)(Activation0002)
    Activation0004 = Activation(activation='relu')(Dense0003)
    Dense0005 = Dense(units=3)(Activation0004)
    Activation0006 = Activation(activation='softmax')(Dense0005)
    model = Model(inputs=Input0000, outputs=Activation0006)
    return model

model = model_build()

# モデルのコンパイル
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# モデルの訓練
model.fit(X_train, y_train, epochs=50, batch_size=5, validation_split=0.1)

# モデルの評価
loss, accuracy = model.evaluate(X_test, y_test)
print(f'Test loss: {loss}')
print(f'Test accuracy: {accuracy}')
