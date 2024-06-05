
import os
import glob
from mimetypes import guess_type

"""
dataset----train------cat---~~.png
        |          |--dog---~~.png
        | 
        |--test~~~~
        |--validation~~~~
"""


def CHK(path=None, data_type=None, learning_way=None):
    """
    データの型が正しいかチェックします。
    path:データのパス
    data_type:データの種類
    learning_way:学習方法
    """
    break_flag = False
    if data_type == 'image' and learning_way == 'categorical':
        datasets_path = path
        for label_name in glob.glob(os.path.join(datasets_path, '*')):
            for filename in glob.glob(os.path.join(os.path.join(datasets_path, label_name), '*.*')):
                guess = guess_type(os.path.basename(filename))
                if 'image' not in str(guess):
                    break_flag = True
                    break
            if break_flag:
                return False
        return True
            

if __name__ == '__main__':
    judge = CHK(path=None, data_type='image', learning_way='categorical')
    print(judge)