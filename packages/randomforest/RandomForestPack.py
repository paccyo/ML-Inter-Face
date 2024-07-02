
import pandas as pd
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor


class RandomForestToolKit:
    
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

    def set_params(self, train_type, n_estimators):
        if train_type == 'classifier':
            self.rf = RandomForestClassifier(n_estimators=n_estimators)
        else:
            self.rf = RandomForestRegressor(n_estimators=n_estimators)

    
    def train(self):
        self.rf.fit(self.train_df_data.values, self.train_df_target.values.ravel())
        

if __name__ == '__main__':
    rfkit = RandomForestToolKit(r'test_data/dataset', None, {'train':6, 'validation':3, 'test':0})
    rfkit.load_dataset()
    rfkit.set_params(train_type='reg', n_estimators=5)
    rfkit.train()
    # evaluate(rfkit.rf, data_type='validation', train_mode='reg', alg='randomforest', data=rfkit.validation_data, target=rfkit.validation_target, columns=rfkit.train_df_data.columns)
    
    
