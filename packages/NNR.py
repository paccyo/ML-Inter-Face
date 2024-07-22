
from keras.models import load_model
import os
import numpy as np
import matplotlib.pyplot as plt
import japanize_matplotlib


def Research(project_path):
    """
    project_path->str : user_project/Result
    """
    model_file_name = 'trained_model.h5'
    model = load_model(os.path.join(project_path, model_file_name))
    for i in range(len(model.layers)):
        deal_flag = False
        l = model.layers[i]
        if len(l.get_weights()) == 2 and i != len(model.layers)-1:
            weights = l.get_weights()[0][:3]
            print(weights)
            break
            bias = l.get_weights()[1]
            deal_flag = True
        if deal_flag:
            plt.figure()
            if len(weights.shape) == 4:
                # 重みを可視化
                print(weights)
                fig, axes = plt.subplots(nrows=weights.shape[0], ncols=weights.shape[1], figsize=(12, 8))
                for j in range(weights.shape[0]):
                    for k in range(weights.shape[1]):
                        ax = axes[j, k]
                        im = ax.imshow(weights[j, k], cmap='viridis', aspect='auto')
                        ax.set_title(f'Weight [{j}][{k}]')
                        fig.colorbar(im, ax=ax)
            
            elif len(weights.shape) == 2: 
                num_matrices, num_elements = weights.shape
                # サブプロットの列数を計算（各行列を正方形に近い形で表示するため）
                grid_size = int(np.ceil(np.sqrt(num_elements)))
                fig, axes = plt.subplots(nrows=1, ncols=num_matrices, figsize=(15, 5))
                for j in range(num_matrices):
                    ax = axes[j]
                    im = ax.imshow(weights[j].reshape((grid_size, grid_size)), cmap='viridis', aspect='auto')
                    ax.set_title(f'Weight [{j}]')
                    fig.colorbar(im, ax=ax)
            plt.tight_layout()
            plt.savefig(f'{project_path}/weights{i}.png')


if __name__ == '__main__':
    Research(r"C:\Users\yuuki\Documents\GUI_MLearning\ML-Inter-Face\packages\image")
