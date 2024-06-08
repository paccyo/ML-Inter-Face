
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
    break_flag = False
    datasets_path = path
    results = []
    if learning_way == 'categorical':
        if data_type == 'image':
            label_num = 0
            for label_name in glob.glob(os.path.join(datasets_path, '*')):
                label_num += 1
                for filename in glob.glob(os.path.join(os.path.join(datasets_path, label_name), '*.*')):
                    guess = guess_type(os.path.basename(filename))
                    if data_type in str(guess):
                        image_path = os.path.join(os.path.join(datasets_path, label_name), filename)
                        results.append(image_path)
                    else:
                        break_flag = True
                        break
                if break_flag:
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
    judge = CHK(path='data.csv', data_type='text', learning_way='categorical', target='data')
    print(judge)