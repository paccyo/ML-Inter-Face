
import subprocess

def generate(target_path, run_path):
    """
    target_path->str: "プロジェクト名/Scripts"絶対パス
    run_path->str: "仮想環境のactivate.batのパス"
    """
    with open('run.bat', 'w') as f:
        f.write(f'"{run_path}"\nstart {target_path}/RunTrain.py')

def Runbat(batfile_path):
    """
    batfile_path->str: バッチファイルのパス
    """
    batfile_path = batfile_path.replace('\\', '/')
    path = '/'.join(batfile_path.split('/')[:-1])
    with open(f'{path}/output.txt', 'w') as f:
        pass
    subprocess.Popen(batfile_path, stdout=f'{path}/output.txt', stderr=f'{path}/output.txt')
