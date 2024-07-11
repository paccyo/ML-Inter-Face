from sklearn.svm import SVC
import pandas as pd
from packages import evaluate


train_data_df = pd.read_csv('test_data/dataset/train_data.csv')
train_data = pd.read_csv('test_data/dataset/train_data.csv').values
validation_data = pd.read_csv('test_data/dataset/validation_data.csv').values

train_target = pd.read_csv('test_data/dataset/train_target.csv').values
validation_target = pd.read_csv('test_data/dataset/validation_target.csv').values
svm = SVC(probability=True,kernel='linear')
svm.fit(train_data, train_target.ravel())

evaluate.evaluate(svm, data_type='validation', train_mode='classifier', alg='SVM', data=validation_data, target=validation_target, columns=train_data_df.columns)