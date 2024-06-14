
import shutil

def CopyTrain(target_path):
    """
    target_path->str: "プロジェクトフォルダ/Scripts"を指定
    """
    shutil.copy('RunTrain.py', f'{target_path}/RunTrain.py')

if __name__ == '__main__':
    CopyTrain(r'path')