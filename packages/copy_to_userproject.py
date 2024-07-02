
import shutil

def CopyNNTrain(target_path):
    """
    実行ファイルをユーザープロジェクトにコピーします
    target_path->str: "プロジェクトフォルダ/Scripts"を指定
    """
    shutil.copy('packages/NNTrain.py', f'{target_path}/NNTrain.py')

def CopyMLTrain(target_path):
    """
    実行ファイルをユーザープロジェクトにコピーします
    target_path->str: "プロジェクトフォルダ/Scripts"を指定
    """
    shutil.copy('packages/MLTrain.py', f'{target_path}/MLTrain.py')

def CopyModelGraph(target_path):
    """
    Graphvizを用いたモデルグラフアウトプットスクリプトをユーザープロジェクトにコピーします。
    target_path->str: "プロジェクトフォルダ/Scripts"を指定
    """
    shutil.copy('packages/output_model_graph.py', f'{target_path}/output_model_graph.py')

if __name__ == '__main__':
    CopyNNTrain(r'path')
    CopyModelGraph(r'path')