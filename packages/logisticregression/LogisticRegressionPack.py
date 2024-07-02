
import pandas as pd
from sklearn.linear_model import LogisticRegression


class LogisticRegressionToolKit:

    def __init__(self, dataset_path, project_path, part):
        """
        project_path:str -> user_project/Result
        """
        self.dataset_path = dataset_path
        self.project_path = project_path
        self.train_part = part['train']
        self.validation_part = part['validation']
        self.test_part = part['test']

    def load_dataset(self):
        if self.train_part != 0:
            self.train_df_data = pd.read_csv(f'{self.dataset_path}/train_data.csv')
            self.train_df_target = pd.read_csv(f'{self.dataset_path}/train_target.csv')
            self.train_data = self.train_df_data.values
            self.train_target = self.train_df_target.values
        
        if self.validation_part != 0:
            self.validation_df_data = pd.read_csv(f'{self.dataset_path}/validation_data.csv')
            self.validation_df_target = pd.read_csv(f'{self.dataset_path}/validation_target.csv')
            self.validation_data = self.validation_df_data.values
            self.validation_target = self.validation_df_target.values

        if self.test_part != 0:
            self.test_df_data = pd.read_csv(f'{self.dataset_path}/test_data.csv')    
            self.test_df_target = pd.read_csv(f'{self.dataset_path}/test_target.csv')
            self.test_data = self.test_df_data.values
            self.test_target = self.test_df_target.values
        
    def set_params(self):
        self.lr = LogisticRegression()

    def train(self):
        self.lr.fit(self.train_data, self.train_target.ravel())

if __name__ == '__main__':
    lrkit = LogisticRegressionToolKit(dataset_path=r'test_data', project_path=None)
    lrkit.load_dataset()
    lrkit.set_params()
    lrkit.train()
    lrkit.evaluate()
