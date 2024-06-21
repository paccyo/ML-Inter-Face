
import shutil

def CopyTrain(target_path):
    """
    実行ファイルをユーザープロジェクトにコピーします
    target_path->str: "プロジェクトフォルダ/Scripts"を指定
    """
    shutil.copy('packages/RunTrain.py', f'{target_path}/RunTrain.py')

def CopyModelGraph(target_path):
    """
    Graphvizを用いたモデルグラフアウトプットスクリプトをユーザープロジェクトにコピーします。
    target_path->str: "プロジェクトフォルダ/Scripts"を指定
    """
    shutil.copy('packages/output_model_graph.py', f'{target_path}/output_model_graph.py')

if __name__ == '__main__':
    CopyTrain(r'path')
    CopyModelGraph(r'path')