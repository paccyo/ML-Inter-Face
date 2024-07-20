
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


def CHK(path=None, data_type=None, learning_way=None, export_path=None):
    """
    データの型が正しいかチェックします。

    Parameters
    ----------
    path:データのパス
    data_type:データの種類
    learning_way:学習方法
    export_path:dataframeの保存先
    """
    datasets_path = path
    results = {}
    if learning_way == 'categorical':
        if data_type == 'image':
            label_num = 0
            for label_path in glob.glob(os.path.join(datasets_path, '*')):
                label_num += 1
                temp = []
                if not os.path.isdir(label_path):
                    return False, {}
                for file_path in glob.glob(os.path.join(label_path, '*.*')):
                    guess = guess_type(os.path.basename(file_path))
                    if data_type in str(guess):
                        temp.append(file_path)
                    else:
                        return False, {}
                label_name = label_path.replace('\\', '/').split('/')[-1]
                results[label_name] = temp[:10]
            if label_num >= 2:
                return True, results
            else:
                return False, {}
        elif data_type == 'dataframe':
            if type(datasets_path) == list:
                data_list = []
                for file in datasets_path:
                    data_list.append(pd.read_csv(file))
                df = pd.concat(data_list, axis=0, sort=False)
                COPY(df, export_path)
                return True, df
            elif '.csv' == os.path.splitext(os.path.basename(datasets_path))[-1]:
                df = pd.read_csv(datasets_path)
                COPY(df, export_path)
                return True, df
            else:
                return False, {}
            
def COPY(df, project_path):
    """
    dataframeをuser_project/Dataへコピー

    Parameters
    ----------
    df:pd.DataFrame -> データフレーム
    project_path:str -> データセットコピー先パス(maybe user_project/Data)
    """
    df.to_csv(os.path.join(project_path, 'original_data.csv'), index=False)


if __name__ == '__main__':
    judge = CHK(path=[r"C:\Users\Yuuki\Documents\GUI_MLearning\ML-Inter-Face\test_data\dataset\train_data.csv", r"C:\Users\Yuuki\Documents\GUI_MLearning\ML-Inter-Face\test_data\dataset\test_data.csv"], data_type='dataframe', learning_way='categorical', export_path=r"C:\Users\Yuuki\Documents\GUI_MLearning\ML-Inter-Face\packages\image")
    print(judge)