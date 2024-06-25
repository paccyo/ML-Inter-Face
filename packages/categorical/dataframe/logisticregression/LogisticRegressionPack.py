
import pandas as pd
from sklearn.linear_model import LogisticRegression


class LogisticRegressionToolKit:

    def load_dataset(self):
        # 説明変数
        self.train_df_data = pd.read_csv('test_data/train_data.csv')
        self.validation_df_data = pd.read_csv('test_data/validation_data.csv')
        self.test_df_data = pd.read_csv('test_data/test_data.csv')
        # 目的変数
        self.train_df_target = pd.read_csv('test_data/train_target.csv')
        self.validation_df_target = pd.read_csv('test_data/validation_target.csv')
        self.test_df_target = pd.read_csv('test_data/test_target.csv')

    def set_params(self):
        self.lr = LogisticRegression()

    def train(self):
        self.lr.fit(self.train_df_data.values, self.train_df_target.values.ravel())

    def save_model_fig(self):
        pass

if __name__ == '__main__':
    lrkit = LogisticRegressionToolKit()
    lrkit.load_dataset()
    lrkit.set_params()
    lrkit.train()
    lrkit.save_model_fig()
