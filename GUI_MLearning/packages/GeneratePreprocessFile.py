
import os

class PreprocessInfo:
    """
    前処理スクリプトファイル作成
    """
    def __init__(self):
        self.preps = ''
        self.params = ''
        self.imports = ''
        self.main_params_list = ['']
        self.load_import_info()

    def load_import_info(self):
        """
        importテキスト読み込み
        """
        with open('packages/preprocess_imports.txt') as f:
            imports_data = f.read()
        self.imports += imports_data + '\n\n'

    def send(self, dicts, data_type=None, dataset_type=None, dataset_path=None, project_path=None):
        """
        dicts->辞書
        data_type->str: image, text, etc....
        dataset_type->str: train, validation, test etc...
        dataset_path->str: datasetのpath
        """
        if data_type == 'image':
            self.Prep_image_dataset(dicts, dataset_type, dataset_path, project_path)

    def Prep_image_dataset(self, dicts, dataset_type, dataset_path, project_path):
        datagen_name = ''
        self.preps = ''
        self.params = ''
        if dicts:
            for i, (fanc_name, params) in enumerate(dicts.items()):
                self.params = ''
                if i == 1:
                    path = os.path.join(dataset_path, dataset_type)
                    self.params += f'r\'{path}\', '
                if dataset_type == 'train':
                    for params_name, params_value in params.items():
                        self.params += f'{params_name}={params_value}, '
                else:
                    for params_name, params_value in params.items():
                        if params_name == 'rescale' or \
                            params_name == 'dtype' or \
                            params_name == 'target_size' or \
                            params_name == 'color_mode' or \
                            params_name == 'class_mode' or \
                            params_name == 'batch_size':
                            self.params += f'{params_name}={params_value}, '
                self.params = self.params[:-2]
                if i == 0:
                    datagen_name = f'{fanc_name}_{dataset_type}'
                    self.preps += f'    {datagen_name} = {fanc_name}({self.params})\n'
                else:
                    self.preps += f'    {fanc_name}_{dataset_type} = {datagen_name}.{fanc_name}({self.params})\n'
            self.preps += f'    return {fanc_name}_{dataset_type}'
        else:
            self.preps += '    return False'
        self.write_Prepfile(dataset_type, project_path)
        self.loop_judge(dicts, dataset_type, dataset_path, project_path)

    def write_Prepfile(self, dataset_type, project_path):
        with open(f'{project_path}/{dataset_type}_preprocess_info.py', 'w') as f:
            f.write(f'{self.imports}\n\ndef preprocess_info():\n{self.preps}')

    def loop_judge(self, dicts, dataset_type, dataset_path, project_path):
        if dataset_type == 'train':
            self.Prep_image_dataset(dicts, 'validation', dataset_path, project_path)
        elif dataset_type == 'validation':
            self.Prep_image_dataset(dicts, 'test', dataset_path, project_path)
        else:
            return


if __name__ == '__main__':
    preprocess_dicts = {
        'ImageDataGenerator': {
            'featurewise_center':False,
            'samplewise_center': False,
        },
        'flow_from_directory': {
            'target_size': (256, 256),
            'color_mode': '\'rgb\''
        }
    }

    prep = PreprocessInfo(data_type='image')
    prep.Prep_dataset(preprocess_dicts)


    
