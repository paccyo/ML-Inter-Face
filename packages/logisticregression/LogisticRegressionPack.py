
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score


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

        
    def set_params(self):
        self.lr = LogisticRegression()

    def train(self):
        self.lr.fit(self.train_data, self.train_df_target.values.ravel())

    def save_model_fig(self):
        pass

    def evaluate(self, mode='validation'):
        print(self.lr.predict(self.validation_data[0]))
        # if mode == 'validation':
        #     accuracy_score(y_true=self.validation)
        #     print('accuracy：', accuracy_score(y_true=y_train, y_pred=y_pred_train))
        #     print('precision：', precision_score(y_true=y_train, y_pred=y_pred_train))
        #     print('recall：', recall_score(y_true=y_train, y_pred=y_pred_train))
        #     print('f1 score：', f1_score(y_true=y_train, y_pred=y_pred_train))
        #     print('confusion matrix = \n', confusion_matrix(y_true=y_train, y_pred=y_pred_train))
        

    def save_result_data(self):
        with open(f'{self.project_path}/result.txt', 'w') as f:
            f.write()

if __name__ == '__main__':
    lrkit = LogisticRegressionToolKit(dataset_path=r'test_data', project_path=None)
    lrkit.load_dataset()
    lrkit.set_params()
    lrkit.train()
    lrkit.evaluate()
