
import pandas as pd
from packages import evaluate
from packages import convert_type
import model_info
import sys
import numpy as np


class TrainToolKit:
    """
    ML用学習ツールキット
    """

    def __init__(self, dataset_path, export_path, part):
        """
        project_path:str -> user_project/Result
        """
        self.dataset_path = dataset_path
        self.export_path = export_path
        self.train_part = part['train']
        self.validation_part = part['validation']
        self.test_part = part['test']

    def load_dataset(self):
        # 説明変数
        if self.train_part != 0:
            self.train_df_data = pd.read_csv(f'{self.dataset_path}/train_data.csv')
            self.train_df_target = pd.read_csv(f'{self.dataset_path}/train_target.csv')
            self.train_data = self.train_df_data.values
            self.train_target = np.array(self.train_df_target.values)
        
        if self.validation_part != 0:
            self.validation_df_data = pd.read_csv(f'{self.dataset_path}/validation_data.csv')
            self.validation_df_target = pd.read_csv(f'{self.dataset_path}/validation_target.csv')
            self.validation_data = self.validation_df_data.values
            self.validation_target = np.array(self.validation_df_target.values)

        if self.test_part != 0:
            self.test_df_data = pd.read_csv(f'{self.dataset_path}/test_data.csv')    
            self.test_df_target = pd.read_csv(f'{self.dataset_path}/test_target.csv')
            self.test_data = self.test_df_data.values
            self.test_target = np.array(self.test_df_target.values)
            
    def load_model(self):
        self.model = model_info.model_build()
        
    def train(self):
        self.model.fit(self.train_data, self.train_target.ravel())


# _, dataset_path, export_path, train_part, validation_part, test_part, train_mode, alg  = sys.argv[0], sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6], sys.argv[7]
_, dataset_path, export_path, train_part, validation_part, test_part, train_mode, alg  = None, r'test_data/dataset', r"test_data/test_dir", 6, 4, 0, 'classifier', 'decisiontree'
# train_mode = classifier or reg
# alg = decisiontree, randomforest, SVM
train_part, validation_part, test_part, int(train_part), int(validation_part), int(test_part)
kit = TrainToolKit(dataset_path, None, {'train':train_part, 'validation':validation_part, 'test':test_part})
kit.load_dataset()
kit.load_model()
kit.train()
evaluate.evaluate(kit.model, data_type='validation', train_mode=train_mode, alg=alg, data=kit.validation_data, target=kit.validation_target, columns=kit.validation_df_data.columns, export_path=export_path)
if test_part != 0:
    evaluate.evaluate(kit.model, data_type='test', train_mode=train_mode, alg=alg, data=kit.test_data, target=kit.test_target, columns=kit.test_df_data.columns, export_path=export_path)
