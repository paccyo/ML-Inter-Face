
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

        データセット作成

        Parameters
        ----------

        part->str: 辞書
        data_path->str: データセットpath
        project_path:str -> "user_project/Data"
        data_type:str -> 'image' or 'text
        """
        if data_type == 'image':
            self.generate_image_dataset(part, data_path, project_path, data_type)

    def send_dataframe(self, part, dataframe, cols_dict, project_path, data_type='dataframe', shuffle=False):
        """

        データセット作成

        Parameters
        ----------

        part:dict -> {'train':7, 'validation':2, 'test':1}
        dataframe:pd.DataFrame -> DataFrame
        cols_dict:dict -> {'data':['AAA', 'BBB'], 'target':['CCC', 'DDD']}
        project_path:str -> user_project/Data
        data_type:str ->'dataframe'
        shuffle:bool -> True or False
        """
        self.generate_dataframe_dataset(part, dataframe, cols_dict, project_path, data_type, shuffle)


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

    
    def generate_dataframe_dataset(self, part, dataframe, cols_dict, project_path, data_type, shuffle):
        self.delete_dir(project_path)
        self.generate_dir(None, None, project_path, data_type)
        part = [part['train'], part['validation'], part['test']]
        df = dataframe
        if shuffle:
            df = df.sample(frac=1)
        df_data = df[cols_dict['data']]
        df_target = df[cols_dict['target']]
        sum_n = len(list(df.index))
        train_n, validation_n, test_n = self.calc_part(part, sum_n)
        # 説明変数
        train_df_data = df_data.iloc[:train_n]
        validation_df_data = df_data.iloc[train_n:train_n+validation_n]
        test_df_data = df_data.iloc[train_n+validation_n:train_n+validation_n+test_n]
        # 目的変数
        train_df_target = df_target.iloc[:train_n]
        validation_df_target = df_target.iloc[train_n:train_n+validation_n]
        test_df_target = df_target.iloc[train_n+validation_n:train_n+validation_n+test_n]
        # 説明変数
        if len(train_df_data.values):
            train_df_data.to_csv(os.path.join(project_path, 'dataset/train_data.csv'), index=False)
        if len(validation_df_data.values):
            validation_df_data.to_csv(os.path.join(project_path, 'dataset/validation_data.csv'), index=False)
        if len(test_df_data.values):
            test_df_data.to_csv(os.path.join(project_path, 'dataset/test_data.csv'), index=False)
        # 目的変数
        if len(train_df_target.values):
            train_df_target.to_csv(os.path.join(project_path, 'dataset/train_target.csv'), index=False)
        if len(validation_df_target.values):
            validation_df_target.to_csv(os.path.join(project_path, 'dataset/validation_target.csv'), index=False)
        if len(test_df_target.values):
            test_df_target.to_csv(os.path.join(project_path, 'dataset/test_target.csv'), index=False)


        

# テストケース
if __name__ == '__main__':
    test_dict = {'train':6, 'validation':3, 'test':1}
    dataset_info = DatasetInfo()
    df = pd.read_csv(r"C:\Users\yuuki\Documents\GUI_MLearning\ML-Inter-Face\test_data\data.csv")
    print(df)
    # 分類
    dataset_info.generate_dataframe_dataset(test_dict, df, {'data':['SepalLengthCm', 'SepalWidthCm', 'PetalWidthCm'], 'target':['Species']}, r"C:\Users\yuuki\Documents\GUI_MLearning\ML-Inter-Face\test_data", 'dataframe', True)
    # 回帰
    # dataset_info.generate_dataframe_dataset(test_dict, df, {'data':['SepalLengthCm', 'SepalWidthCm', 'PetalWidthCm'], 'target':['PetalLengthCm']}, r"C:\Users\yuuki\Documents\GUI_MLearning\ML-Inter-Face\test_data", 'dataframe', True)
