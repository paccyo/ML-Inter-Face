
import pandas as pd
from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt


class DecisionTreeClassifierToolKit:

    def load_dataset(self):
        # 説明変数
        self.train_df_data = pd.read_csv('test_data/train_data.csv')
        self.validation_df_data = pd.read_csv('test_data/validation_data.csv')
        self.test_df_data = pd.read_csv('test_data/test_data.csv')
        # 目的変数
        self.train_df_target = pd.read_csv('test_data/train_target.csv')
        self.validation_df_target = pd.read_csv('test_data/validation_target.csv')
        self.test_df_target = pd.read_csv('test_data/test_target.csv')

    def set_params(self, max_depth):
        self.clf = DecisionTreeClassifier(max_depth=max_depth)

    def train(self):
        self.clf.fit(self.train_df_data.values, self.train_df_target.values)

    def save_model_fig(self):
        plot_tree(self.clf, feature_names=self.train_df_data.columns, class_names=self.train_df_target.columns, filled=True)
        plt.show()


if __name__ == '__main__':
    dtkit = DecisionTreeClassifierToolKit()
    dtkit.load_dataset()
    dtkit.set_params()
    dtkit.train()
    dtkit.save_model_fig()
