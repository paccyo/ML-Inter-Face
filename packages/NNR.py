
from keras.models import load_model
import os
import numpy as np
import matplotlib.pyplot as plt
import japanize_matplotlib
import math
from keras.models import load_model
import csv
import os


def Research(project_path):
    """
    project_path->str : user_project/Result
    """
    model_file_name = 'trained_model.h5'
    model = load_model(os.path.join(project_path, model_file_name))
    for i in range(len(model.layers)):
        deal_flag = False
        l = model.layers[i]
        layer_name = l.name
        if len(l.get_weights()) != 0:
            raw_weights = l.get_weights()[0]
            save_weight = generate_save_weights(raw_weights)
            save_csv(layer_name, save_weight, project_path)
        else:
            save_blank_csv(layer_name, project_path)
        if len(l.get_weights()) == 2 and i != len(model.layers)-1:
            weights = l.get_weights()[0][:3]
            bias = l.get_weights()[1]
            deal_flag = True
        if deal_flag:
            plt.figure()
            if len(weights.shape) == 4:
                # 重みを可視化
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


def generate_dimensions_list(data):
    if len(data.shape) > 2:
        d_loop = list(data.shape)[:-2]
        d_loop.insert(0, 1)
        d_loop.append(1)
        result = []
        d_loop = d_loop[::-1]
        for i, dim in enumerate(d_loop[1:-1]):
            i += 1
            inner_iter_num = math.prod(d_loop[:i-1])*d_loop[i-1]
            outer_iter_num = math.prod(d_loop[i+1:])
            if i == 1:
                r = [j*inner_iter_num for j in list(range(1, dim+1))]*outer_iter_num
            else:
                r = np.array([[j]*inner_iter_num for j in list(range(1, dim+1))]*outer_iter_num).reshape(-1,)
            result.append(r)
        result = result[::-1]
        result.append([data.shape[-2]]*len(result[0]))
        result.append([data.shape[-1]]*len(result[0]))
        result = list(np.array(result).T)
        print(result)
    else:
        result = list([np.array(data.shape)])
    return result

def convert_weights(data):
    reshaped_data = list(data.reshape(-1, data.shape[-1]))
    return reshaped_data

def generate_save_weights(raw_weights):
    converted_weights = convert_weights(raw_weights)
    dim_list = generate_dimensions_list(raw_weights)
    place_keeper = 0
    if len(raw_weights.shape) == 1:
        skip_iter = 1
    else:
        skip_iter = raw_weights.shape[-2]
    for j, weight_line_index in enumerate(range(0, len(converted_weights), skip_iter)):
        converted_weights.insert(weight_line_index+place_keeper, tuple(dim_list[j]))
        place_keeper += 1
    return converted_weights

def save_csv(layer_name, weights, project_path):
    with open(f'{project_path}/{layer_name}.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for weight_line in weights:
            if type(weight_line) == tuple:
                weight_line = str(weight_line).replace(' ', '')
            writer.writerow(weight_line)

def save_blank_csv(layer_name, project_path):
    with open(f'{project_path}/{layer_name}.csv', 'w', newline='') as csvfile:
        pass

class ReModel:

    def __init__(self, model_path):
        self.model = load_model(model_path)

    def csv_to_weights(self, file_path):
        read_weights = []
        shape_size = None
        with open(f'{file_path}', 'r') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                if '(' in row:
                    row.remove('(')
                    row.remove(')')
                    row = ''.join(row).split(',')
                    shape_size = tuple(map(int, row))
                else:
                    read_weights.append(row)
            read_weights = np.array(read_weights)
            read_weights = read_weights.reshape(shape_size)
        return read_weights

    def rewrite_model(self, file_name, weights):
        if len(self.model.get_layer(file_name).get_weights()) != 0:
            bias = self.model.get_layer(file_name).get_weights()[1]
            param = [weights, bias]
            self.model.get_layer(file_name).set_weights(param)
                
    def csv_to_model(self, csv_file_path, export_path):
        for path in csv_file_path:
            weights = self.csv_to_weights(path)
            file_name = os.path.splitext(os.path.basename(csv_file_path))[0]
            self.rewrite_model(file_name, weights)
        self.model.save(f'{export_path}/edited_model.h5')


if __name__ == '__main__':
    # Research(r"C:\Users\yuuki\Documents\GUI_MLearning\ML-Inter-Face\packages\image")
    remodel = ReModel(r"C:\Users\yuuki\Documents\GUI_MLearning\ML-Inter-Face\packages\image\trained_model.h5")
    remodel.csv_to_model(r"C:\Users\Yuuki\Documents\GUI_MLearning\ML-Inter-Face\packages\image\activation_1.csv", export_path=r"C:\Users\yuuki\Documents\GUI_MLearning\ML-Inter-Face\packages\image")
    
