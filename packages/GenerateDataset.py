
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

    def send_dataframe(self, part, data_path, project_path, data_type='dataframe', shuffle=False):
        """
        project_path:str -> user_project/Data
        """
        self.generate_dataframe_dataset(part, data_path, project_path, data_type, shuffle)


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
            os.makedirs(f'{project_path}', exist_ok=True)

    def generate_image_dataset(self, part, data_path, project_path):
        self.delete_dir(project_path)
        part = [part['train'], part['validation'], part['test']]
        for i, label_path in enumerate(glob.glob(os.path.join(data_path, '*'))):
            # ラベルごとの画像枚数
            sum_n = len(glob.glob(os.path.join(label_path, '*.*')))
            # ラベル名
            label = label_path.split('\\')[-1]
            # フォルダ作成
            self.generate_dir(label, part, project_path)
            train_n, validation_n, test_n = self.calc_part(part, sum_n)
            # 画像を突っ込む
            for i, image_path in enumerate(glob.glob(os.path.join(label_path, '*.*'))):
                i += 1
                if i <= train_n:
                    shutil.copy(image_path, f'{project_path}/dataset/train/{label}/{os.path.basename(image_path)}')
                elif i <= (train_n+validation_n):
                    shutil.copy(image_path, f'{project_path}/dataset/validation/{label}/{os.path.basename(image_path)}')
                else:
                    shutil.copy(image_path, f'{project_path}/dataset/test/{label}/{os.path.basename(image_path)}')

    def calc_part(self, part, sum_n):
        # それぞれのデータ数
        train_n = int(sum_n*(part[0]/10))
        validation_n = int(sum_n*(part[1]/10))
        test_n = int(sum_n*(part[2]/10))
        # 余ったデータを0ではないところへin
        if train_n != 0:
            train_n += sum_n-(train_n+validation_n+test_n)
        elif validation_n != 0:
            validation_n += sum_n-(train_n+validation_n+test_n)
        else:
            test_n += sum_n-(train_n+validation_n+test_n)
        return train_n, validation_n, test_n

    
    def generate_dataframe_dataset(self, part, data_path, project_path, data_type, shuffle):
        self.delete_dir(project_path)
        self.generate_dir(None, None, project_path, data_type)
        part = [part['train'], part['validation'], part['test']]
        df = pd.read_csv(data_path)
        sum_n = len(list(df.index))
        train_n, validation_n, test_n = self.calc_part(part, sum_n)
        if shuffle:
            df = df.sample(frac=1)
        train_df = df.iloc[:train_n]
        validation_df = df.iloc[train_n:train_n+validation_n]
        test_df = df.iloc[train_n+validation_n:train_n+validation_n+test_n]
        if len(train_df.values):
            train_df.to_csv(os.path.join(project_path, 'train.csv'))
        if len(validation_df.values):
            validation_df.to_csv(os.path.join(project_path, 'validation.csv'))
        if len(test_df.values):
            test_df.to_csv(os.path.join(project_path, 'test.csv'))

        

# テストケース
if __name__ == '__main__':
    test_dict = {'train':6, 'validation':3, 'test':1}
    dataset_info = DatasetInfo()
    dataset_info.generate_dataframe_dataset(test_dict, r"C:\Users\yuuki\Documents\GUI_MLearning\ML-Inter-Face\test_data\data.csv", r"C:\Users\yuuki\Documents\GUI_MLearning\ML-Inter-Face\test_data", 'dataframe', True)
