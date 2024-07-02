
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import DecisionTreeRegressor
# from packages import evaluate


class DecisionTreeToolKit:

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
        # 説明変数
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

    def set_params(self, train_type, max_depth):
        if train_type == 'classifier':
            self.clf = DecisionTreeClassifier(max_depth=max_depth)
        else:
            self.clf = DecisionTreeRegressor(max_depth=max_depth)
        
    def train(self):
        self.clf.fit(self.train_df_data.values, self.train_df_target.values)



if __name__ == '__main__':
    dtkit = DecisionTreeToolKit(r'test_data/dataset', None, {'train':6, 'validation':3, 'test':0})
    dtkit.load_dataset()
    dtkit.set_params(train_type='reg', max_depth=8)
    dtkit.train()
    # evaluate(dtkit.clf, data_type='validation', train_mode='reg', alg='decisiontree', data=dtkit.validation_data, target=dtkit.validation_target, columns=dtkit.train_df_data.columns)
