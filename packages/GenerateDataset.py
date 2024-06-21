
import glob
import os
import shutil
import pandas as pd


class DatasetInfo:
    """
    データセット作成
    """
    def send_image(self, part, data_path, project_path, data_type='image'):
        """
        part->str: 辞書
        data_path->str: データセットpath
        project_path:str -> "user_project/Data"
        data_type:str -> 'image' or 'text
        """
        if data_type == 'image':
            self.generate_image_dataset(part, data_path, project_path, data_type)

    def send_dataframe(self, part, data_path, project_path, data_type='dataframe'):
        """
        project_path:str -> user_project/Data
        """
        self.generate_dataframe_dataset(part, data_path, project_path, data_type)


    def delete_dir(self, project_path):
        """
        ディレクトリ削除
        """
        try:
            shutil.rmtree(f'{project_path}/dataset')
        except FileNotFoundError:
            pass

    def generate_dir(self, label, part, project_path, data_type):
        """
        ディレクトリ作成
        """
        if data_type == 'image':
            if part[0] != 0:
                os.makedirs(f'{project_path}/dataset/train/{label}', exist_ok=True)
            if part[1] != 0:
                os.makedirs(f'{project_path}/dataset/validation/{label}', exist_ok=True)
            if part[2] != 0:
                os.makedirs(f'{project_path}/dataset/test/{label}', exist_ok=True)
        elif data_type == 'dataframe':
            os.makedirs(f'{project_path}/dataset', exist_ok=True)

    def generate_image_dataset(self, part, data_path, project_path):
        self.delete_dir(project_path)
        # それぞれの画像割合
        part = [part['train'], part['validation'], part['test']]
        for i, label_path in enumerate(glob.glob(os.path.join(data_path, '*'))):
            # ラベルごとの画像枚数
            sum_n = len(glob.glob(os.path.join(label_path, '*.*')))
            # ラベル名
            label = label_path.split('\\')[-1]
            # フォルダ作成
            self.generate_dir(label, part, project_path)
            # それぞれの画像枚数
            train_n = sum_n*(part[0]/10)
            validation_n = sum_n*(part[1]/10)
            test_n = sum_n*(part[2]/10)
            # 余った画像を0ではないところへin
            if train_n != 0:
                train_n += sum_n-(train_n+validation_n+test_n)
            elif validation_n != 0:
                validation_n += sum_n-(train_n+validation_n+test_n)
            else:
                test_n += sum_n-(train_n+validation_n+test_n)

            # 画像を突っ込む
            for i, image_path in enumerate(glob.glob(os.path.join(label_path, '*.*'))):
                i += 1
                if i <= train_n:
                    shutil.copy(image_path, f'{project_path}/dataset/train/{label}/{os.path.basename(image_path)}')
                elif i <= (train_n+validation_n):
                    shutil.copy(image_path, f'{project_path}/dataset/validation/{label}/{os.path.basename(image_path)}')
                else:
                    shutil.copy(image_path, f'{project_path}/dataset/test/{label}/{os.path.basename(image_path)}')
    
    def generate_dataframe_dataset(self, part, data_path, project_path, data_type):
        self.delete_dir(project_path)
        self.generate_dir(None, None, project_path, data_type)
        



# テストケース
if __name__ == '__main__':
    test_dict = {'train':6, 'validation':4, 'test':0}
    dataset_info = DatasetInfo()
    dataset_info.send(test_dict, r"C:\Users\yuuki\Documents\GUI_MLearning\GUI_MLearning-main\data3")
