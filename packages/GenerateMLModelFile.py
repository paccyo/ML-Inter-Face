
# 2024/06/04 BPS-sys ver1.0作成


class MLModelInfo:
    """
    モデル構造ファイル作成
    """
    def __init__(self):
        self.model = ''
        self.imports = ''
        self.load_import_info()
    
    def load_import_info(self):
        """
        importテキスト読み込み
        """
        with open('packages/MLmodel_imports.txt') as f:
            imports_data = f.read()
        self.imports += imports_data + '\n\n'

    def send(self, model_dict, project_path, shape=None):
        """
        辞書からモデルを構築
        """
        self.generate_model(model_dict, project_path)


    def generate_model(self, model_dict, project_path):
        alg_name = model_dict['alg']
        self.model += '    model = '+alg_name+'('
        for param, value in model_dict.items():
            self.model += f'{param}={value}, '
        self.model = self.model[:-2] + ')\n'
        self.write_modelfile(project_path)
        
    def write_modelfile(self, project_path):
        """
        モデルファイル書き出し
        """
        if self.model:
            with open(f'{project_path}/model_info.py', 'w') as f:
                f.write(self.imports+'def model_build():\n'+self.model+'    return model')

        
            
if __name__ == '__main__':
    # テストケース
    test_dic = {'alg':'DecisionTreeRegressor', 'max_depth':5}

    # 実行

    model_info = MLModelInfo()
    model_info.send(test_dic, 'test_data')

