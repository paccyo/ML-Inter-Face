import tensorflow as tf
import keras
import numpy as np
import matplotlib.pyplot as plt
import japanize_matplotlib
from PIL import Image



def plot_augmentation_image(train_sample, params):

    # 同じ画像を16個複製する
    train_samples = np.repeat(train_sample.reshape((1, train_sample.shape[0], train_sample.shape[1], train_sample.shape[2])), 1, axis=0)

    # 16個に対してparamsで与えられた変換を実施
    data_generator = keras.preprocessing.image.ImageDataGenerator(**params)
    generator = data_generator.flow(train_samples, batch_size=16)

    # 変換後のデータを取得
    batch_x = generator.next()

    # 変換後はfloat32となっているため、uint8に変換
    batch_x = batch_x.astype(np.uint8)
    img = batch_x[0]
    img = Image.fromarray(img)
    img.save(r"C:\Users\yuuki\Documents\GUI_MLearning\ML-Inter-Face\packages\image\test\vertical_flip.jpg")
    # # 描画処理
    # # plt.figure(figsize=(10,10))
    # for i in range(1):
    #     # plt.subplot(4,4,i+1)
        
    #     plt.imshow(batch_x[i])
    #     plt.tick_params(labelbottom='off')
    #     plt.tick_params(labelleft='off')
    # plt.show()




train_sample = np.array(Image.open(r"C:\Users\yuuki\Documents\GUI_MLearning\ML-Inter-Face\packages\image\test\sample.jpg"))

params = {
    'vertical_flip':True
}
plot_augmentation_image(train_sample, params)

