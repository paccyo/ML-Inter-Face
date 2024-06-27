
import pandas as pd
from sklearn.svm import SVC


class SVMToolKit:

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

    def set_params(self):
        self.svm = SVC()

    def train(self):
        self.svm.fit(self.train_df_data.values, self.train_df_target.values.ravel())

    def save_model_fig(self):
        pass

if __name__ == '__main__':
    lrkit = SVMToolKit()
    lrkit.load_dataset()
    lrkit.set_params()
    lrkit.train()
    lrkit.save_model_fig()
