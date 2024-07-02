
import pandas as pd
from sklearn.tree import DecisionTreeClassifier


class DecisionTreeClassifierToolKit:

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

    def set_params(self, max_depth):
        self.clf = DecisionTreeClassifier(max_depth=max_depth)

    def train(self):
        self.clf.fit(self.train_df_data.values, self.train_df_target.values)

        


if __name__ == '__main__':
    dtkit = DecisionTreeClassifierToolKit(r'test_data', None)
    dtkit.load_dataset()
    dtkit.set_params(max_depth=8)
    dtkit.train()
    dtkit.save_model_fig()
    dtkit.evaluate()
