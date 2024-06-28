
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score, roc_curve, auc
from sklearn.preprocessing import label_binarize
import matplotlib.pyplot as plt
import japanize_matplotlib


class LogisticRegressionToolKit:

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
        
    def set_params(self):
        self.lr = LogisticRegression()

    def train(self):
        self.lr.fit(self.train_data, self.train_target.ravel())

    def save_model_fig(self):
        pass

    def evaluate(self, mode='validation'):
        if mode == 'validation':
            pred = self.lr.predict(self.validation_data)
            print('accuracy：', accuracy_score(y_true=self.validation_target, y_pred=pred))
            print('precision：', precision_score(y_true=self.validation_target, y_pred=pred, average='macro'))
            print('recall：', recall_score(y_true=self.validation_target, y_pred=pred, average='macro'))
            print('f1 score：', f1_score(y_true=self.validation_target, y_pred=pred, average='macro'))
            print('confusion matrix = \n', confusion_matrix(y_true=self.validation_target, y_pred=pred))
            #ROC曲線の描画、AUCの計算（ROC曲線の下側の面積）の計算
            n_classes = len(self.lr.classes_)
            classes = self.lr.classes_
            y_test_one_hot = label_binarize(self.validation_target, classes=classes)
            fpr = {}
            tpr = {}
            roc_auc = {}
            pred_proba = self.lr.predict_proba(self.validation_data)
            for i in range(n_classes):
                fpr[i], tpr[i], _ = roc_curve(y_test_one_hot[:, i], pred_proba[:, i])
                roc_auc[i] = auc(fpr[i], tpr[i])
            for i, class_ in enumerate(classes):
                plt.plot(fpr[i], tpr[i], label=f'{class_}')
            plt.legend()   
            plt.show()

    def save_result_data(self):
        with open(f'{self.project_path}/result.txt', 'w') as f:
            f.write()

if __name__ == '__main__':
    lrkit = LogisticRegressionToolKit(dataset_path=r'test_data', project_path=None)
    lrkit.load_dataset()
    lrkit.set_params()
    lrkit.train()
    lrkit.evaluate()
