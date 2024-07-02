
import pandas as pd
from sklearn.ensemble import RandomForestClassifier


class RandomForestToolKit:
    
    def __init__(self, dataset_path, project_path):
        """
        project_path:str -> user_project/Result
        """
        self.dataset_path = dataset_path
        self.project_path = project_path

    def load_dataset(self):
        # 説明変数
        self.train_df_data = pd.read_csv(f'{self.dataset_path}/train_data.csv')
        self.validation_df_data = pd.read_csv(f'{self.dataset_path}/validation_data.csv')
        self.test_df_data = pd.read_csv(f'{self.dataset_path}/test_data.csv')
        # 目的変数
        self.train_df_target = pd.read_csv(f'{self.dataset_path}/train_target.csv')
        self.validation_df_target = pd.read_csv(f'{self.dataset_path}/validation_target.csv')
        self.test_df_target = pd.read_csv(f'{self.dataset_path}/test_target.csv')
        # データセット作成
        self.train_data = self.train_df_data.values
        self.validation_data = self.validation_df_data.values
        self.test_data = self.test_df_data.values
        self.train_target = self.train_df_target.values
        self.validation_target = self.validation_df_target.values
        self.test_target = self.test_df_target.values

    def set_params(self, n_estimators):
        self.rf = RandomForestClassifier(n_estimators=n_estimators)

    def train(self):
        self.rf.fit(self.train_df_data.values, self.train_df_target.values.ravel())
        


if __name__ == '__main__':
    rfkit = RandomForestToolKit(r'test_data', None)
    rfkit.load_dataset()
    rfkit.set_params(n_estimators=5)
    rfkit.train()
    # rfkit.save_model_fig()
    rfkit.evaluate()
