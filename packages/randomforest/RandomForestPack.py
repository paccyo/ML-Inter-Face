
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from pydotplus import graph_from_dot_data
from sklearn.tree import export_graphviz
import matplotlib.pyplot as plt


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

    def set_params(self, n_estimators):
        self.rf = RandomForestClassifier(n_estimators=n_estimators)

    def train(self):
        self.rf.fit(self.train_df_data.values, self.train_df_target.values.ravel())

    def save_model_fig(self):
        estimators = self.rf.estimators_
        dot_data = export_graphviz(estimators[0], # 決定木オブジェクト
                                    out_file=None, # ファイルは介さずにGraphvizにdot言語データを渡す
                                    filled=True, # 分岐の際にどちらのノードに多く分類されたか
                                    rounded=True, # ノードの角を丸く描画
                                    # class_names=self.train_df_target.columns, #クラス名
                                    feature_names=self.train_df_data.columns, #説明変数
                                    special_characters=True # 特殊文字を扱える
                                    )
        graph = graph_from_dot_data(dot_data)
        file_name = "RandomForest_visualization.png"
        graph.write_png(file_name)


if __name__ == '__main__':
    rfkit = RandomForestToolKit()
    rfkit.load_dataset()
    rfkit.set_params(n_estimators=5)
    rfkit.train()
    rfkit.save_model_fig()
