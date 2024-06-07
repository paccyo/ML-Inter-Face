

class PreprocessInfo:
    """
    前処理スクリプトファイル作成
    """
    def __init__(self, data_type='image'):
        self.data_type = data_type
        self.preps = ''
        self.params = ''
        self.imports = ''
        self.load_import_info()

    def load_import_info(self):
        """
        importテキスト読み込み
        """
        with open('imports_file.txt') as f:
            imports_data = f.read()
        self.imports += imports_data + '\n\n'

    def Prep_dataset(self, dicts, dataset_type=None):
        if self.data_type == 'image':
            self.Prep_image_dataset(dicts, dataset_type)

    def Prep_image_dataset(self, dicts, dataset_type):
        datagen_name = ''
        for i, (fanc_name, params) in enumerate(dicts.items()):
            self.params = ''
            for params_name, params_value in params.items():
                self.params += f'{params_name}={params_value}, '
            self.params = self.params[:-1]
            if i == 0:
                datagen_name = f'{fanc_name}_{dataset_type}'
                self.preps += f'    {datagen_name} = {fanc_name}({self.params})\n'
            else:
                self.preps += f'    {fanc_name}_{dataset_type} = {datagen_name}.{fanc_name}({self.params})\n'
        self.preps += f'    return {fanc_name}_{dataset_type}'
        self.write_Prepfile(dataset_type)

    def write_Prepfile(self, dataset_type):
        with open(f'{dataset_type}_preprocess_info.py', 'w') as f:
            f.write(f'{self.imports}\n\ndef preprocess_info():\n{self.preps}')

        


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


    
