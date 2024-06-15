
import shutil

def CopyModelGraph(target_path):
    """
    target_path->str: "プロジェクトフォルダ/Scripts"を指定
    """
    shutil.copy('packages/output_model_graph.py', f'{target_path}/output_model_graph.py')

if __name__ == '__main__':
    CopyModelGraph(r'path')