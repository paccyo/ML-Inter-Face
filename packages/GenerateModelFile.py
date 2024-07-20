
# 2024/06/04 BPS-sys ver1.0作成

import os
import pandas as pd

class ModelInfo:
    """
    モデル構造ファイル作成
    """
    def __init__(self, mode=None):
        self.model = ''
        self.imports = ''
        self.mode = mode
        self.load_import_info()
    
    def load_import_info(self):
        """
        importテキスト読み込み
        """
        if self.mode == 'NN':
            with open('packages/imports_txt/NNmodel_imports.txt') as f:
                imports_data = f.read()
        elif self.mode == 'ML':
            with open('packages/imports_txt/MLmodel_imports.txt') as f:
                imports_data = f.read()
        self.imports += imports_data + '\n\n'

    def send(self, model_dict, project_path, shape=None):
        """
        辞書からモデルを構築
        """
        if self.mode == 'NN':
            self.generate_NNmodel(model_dict, project_path, shape)
        elif self.mode == 'ML':
            self.generate_MLmodel(model_dict, project_path)

    def generate_MLmodel(self, model_dict, project_path):
        """
        MLモデルの作成

        Parameters
        ----------
        model_dict:dict -> パラメータが格納された辞書
        project_path:str -> モデルファイルの保存先(maybe user_project/Scripts)
        """
        alg_name = model_dict['alg']
        self.model += '    model = '+alg_name+'('
        del model_dict['alg']
        for param, value in model_dict.items():
            self.model += f'{param}={value}, '
        self.model = self.model[:-2] + ')\n'
        self.write_modelfile(project_path)

    def generate_NNmodel(self, model_dict, project_path, shape=None):
        """
        NNモデルの作成

        Parameters
        ----------
        model_dict:dict -> パラメータが格納された辞書
        project_path:str -> モデルファイルの保存先(maybe user_project/Scripts)
        shape:tuple -> 画像のサイズ
        """
        before_unique_layer_name = ''    # １つ前のレイヤー変数名(layername)
        first_unique_layer_name = ''     # 最初のレイヤー変数名(inputs)
        filal_unique_layer_name = ''     # 最後のレイヤー変数名(outputs)
        shape_flag = True
        for i, (unique_layer_name, layer_params) in enumerate(model_dict.items()):
            params = ''    # 各レイヤーパラメータの格納用変数
            if i == 0:
                first_unique_layer_name = unique_layer_name
            if i == len(model_dict)-1:
                filal_unique_layer_name = unique_layer_name
            
            # レイヤー関数名を取得
            layer_name = unique_layer_name[:-4]

            # パラメータ引数をセット
            for layer_param_name, layer_param_value in layer_params.items():
                if i == 0 and shape and shape_flag:
                    shape_flag = False
                    params += f'{layer_param_name}={shape}, '
                else:
                    params += f'{layer_param_name}={layer_param_value}, '
            
            # 不要なコンマを削除
            params = params[:-2]

            # 行ごとにレイヤー作成
            if before_unique_layer_name:
                self.model += f'    {unique_layer_name} = {layer_name}({params})({before_unique_layer_name})\n'
            else:
                self.model += f'    {unique_layer_name} = {layer_name}({params})\n'
            
            # １つ前のレイヤー名を更新
            before_unique_layer_name = unique_layer_name
            
        # 最終層作成
        self.model += f'    model = Model(inputs={first_unique_layer_name}, outputs={filal_unique_layer_name})\n'

        self.write_modelfile(project_path)
        
    def write_modelfile(self, project_path):
        """
        モデルファイル書き出し

        Parameters
        ----------
        project_path:str -> モデルファイル保存先(maybe user_project/Scripts)
        """
        if self.model:
            with open(f'{project_path}/model_info.py', 'w') as f:
                f.write(self.imports+'def model_build():\n'+self.model+'    return model')

    def get_image_shape(self, image_size=(None, None), color_mode='rgb'): 
        """
        画像のshapeを返す

        Parameters
        ----------
        image_size:tuple -> (width, height)
        color_mode:str -> rgb or gray
        """   
        if color_mode == 'rgb':
            color = 3
        else:
            color = 1
        return (image_size[0], image_size[1], color)
    
    def get_dataframe_shape(self, dataset_path):
        """
        dataframeのshapeを返す

        Parameters
        ----------
        dataset_path:str -> データセットのパス
        """
        train_data_path = os.path.join(dataset_path, 'train_data.csv')
        df = pd.read_csv(train_data_path)
        return (len(df.values[0]),)


if __name__ == '__main__':
    # テストケース
    test_dic = {
        'Dense0000': {
            'units': 0,
            'use_bias': True,
            'kernel_initializer': '\'glorot_uniform\'',
            'bias_initializer': '\'zeros\'',
            'kernel_regularizer': None,
            'bias_regularizer': None,
            'activity_regularizer': None,
            'kernel_constraint': None,
            'bias_constraint': None,
            'lora_rank': None
        },

        'Activation0000': {
            'activation':None
        },

        'Conv2D0000': {
            'filters': 0,
            'kernel_size': (0, 0),
            'strides': (1, 1),
            'padding': '\'valid\'',
            'data_format': None,
            'dilation_rate': (1, 1),
            'groups': 1,
            'activation': None,
            'use_bias': True,
            'kernel_initializer': '\'glorot_uniform\'',
            'bias_initializer': '\'zeros\'',
            'kernel_regularizer': None,
            'bias_regularizer': None,
            'activity_regularizer': None,
            'kernel_constraint': None,
            'bias_constraint': None
        },

        'Conv1D0000': {
            'filters': 0,
            'kernel_size': 0,
            'strides': 1,
            'padding': '\'valid\'',
            'data_format': None,
            'dilation_rate': 1,
            'groups': 1,
            'activation': None,
            'use_bias': True,
            'kernel_initializer': '\'glorot_uniform\'',
            'bias_initializer': '\'zeros\'',
            'kernel_regularizer': None,
            'bias_regularizer': None,
            'activity_regularizer': None,
            'kernel_constraint': None,
            'bias_constraint': None
        },

        'MaxPooling2D0000': {
            'pool_size': (2, 2),
            'strides': None,
            'padding': '\'valid\'',
            'data_format': None,
            'name': None
        },

        'MaxPooling1D0000': {
            'pool_size': 2,
            'strides': None,
            'padding': '\'valid\'',
            'data_format': None,
            'name': None
        },

        'Flatten0000': {
            'data_format': None
        },

        'GlobalAveragePooling2D0000': {
            'data_format': None,
            'keepdims': False
        },


    }


    # 実行

    model_info = ModelInfo('NN')
    model_info.send(test_dic, r"C:\Users\Yuuki\Documents\GUI_MLearning\ML-Inter-Face\packages\image")

    shape_size = model_info.get_image_shape(image_size=(256, 256), color_mode='rgb')
    print(shape_size)

