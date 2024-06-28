
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from pydotplus import graph_from_dot_data
from sklearn.tree import export_graphviz
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score, roc_curve, auc
from sklearn.preprocessing import label_binarize


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

    def evaluate(self, mode='validation'):
        if mode == 'validation':
            pred = self.rf.predict(self.validation_data)
            print('accuracy：', accuracy_score(y_true=self.validation_target, y_pred=pred))
            print('precision：', precision_score(y_true=self.validation_target, y_pred=pred, average='macro'))
            print('recall：', recall_score(y_true=self.validation_target, y_pred=pred, average='macro'))
            print('f1 score：', f1_score(y_true=self.validation_target, y_pred=pred, average='macro'))
            print('confusion matrix = \n', confusion_matrix(y_true=self.validation_target, y_pred=pred))
            #ROC曲線の描画、AUCの計算（ROC曲線の下側の面積）の計算
            n_classes = len(self.rf.classes_)
            classes = self.rf.classes_
            y_test_one_hot = label_binarize(self.validation_target, classes=classes)
            fpr = {}
            tpr = {}
            roc_auc = {}
            pred_proba = self.rf.predict_proba(self.validation_data)
            for i in range(n_classes):
                fpr[i], tpr[i], _ = roc_curve(y_test_one_hot[:, i], pred_proba[:, i])
                roc_auc[i] = auc(fpr[i], tpr[i])
            for i, class_ in enumerate(classes):
                plt.plot(fpr[i], tpr[i], label=f'{class_}')
            plt.legend()   
            plt.show()

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
    rfkit = RandomForestToolKit(r'test_data', None)
    rfkit.load_dataset()
    rfkit.set_params(n_estimators=5)
    rfkit.train()
    # rfkit.save_model_fig()
    rfkit.evaluate()
