
import os
import glob
from mimetypes import guess_type
import pandas as pd

"""
image:
dataset----train------cat---~~.png
        |          |--dog---~~.png
        | 
        |--test~~~~
        |--validation~~~~
"""


def CHK(path=None, data_type=None, learning_way=None, target=None):
    """
    データの型が正しいかチェックします。
    path:データのパス
    data_type:データの種類
    learning_way:学習方法
    """
    datasets_path = path
    results = []
    if learning_way == 'categorical':
        if data_type == 'image':
            label_num = 0
            for label_path in glob.glob(os.path.join(datasets_path, '*')):
                label_num += 1
                if not os.path.isdir(label_path):
                    return False, []
                for file_path in glob.glob(os.path.join(label_path, '*.*')):
                    guess = guess_type(os.path.basename(file_path))
                    if data_type in str(guess):
                        results.append(file_path)
                    else:
                        return False, []
            
            if label_num >= 2:
                return True, results
            else:
                return False, []

        elif data_type == 'text':
            if '.csv' == os.path.splitext(os.path.basename(datasets_path))[-1]:
                df = pd.read_csv(datasets_path)
                try:
                    target_df = df[target]
                    df.pop(target)
                    results.append([df, target_df])
                except KeyError:
                    return False, []
                else:
                    return True, results
            else:
                return False, []
            


if __name__ == '__main__':
    judge = CHK(path='data3', data_type='image', learning_way='categorical', target='data')
    print(judge)