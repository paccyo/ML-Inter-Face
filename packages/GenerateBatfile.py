
import subprocess

def generateNN(target_path, run_path, train_part, validation_part, test_part, data_type, epochs, batchs=None, project_path=None, dataset_path=None, class_nums=None, train_type=None):
    """
    NN用バッチファイル作成

    Parameters
    ----------
    target_path->str: "プロジェクト名/Scripts"絶対パス
    run_path->str: "仮想環境のactivate.batのパス"
    project_path->str: 
    """
    with open(target_path+'/run.bat', 'w') as f:
        f.write(f'call "{run_path}"\npython {target_path}/NNTrain.py {train_part} {validation_part} {test_part} {data_type} {epochs} {batchs} {project_path} {dataset_path} {class_nums} {train_type}')

def generateML(target_path, run_path, part_dict, dataset_path, export_path, train_mode, alg):
    """
    ML用バッチファイル作成

    Parameters
    ----------
    target_path->str: "プロジェクト名/Scripts"絶対パス
    run_path->str: "仮想環境のactivate.batのパス"
    project_path->str: 
    """
    train_part = part_dict['train']
    validation_part = part_dict['validation']
    test_part = part_dict['test']
    with open(target_path+'/run.bat', 'w') as f:
        f.write(f'call "{run_path}"\npython {target_path}/MLTrain.py {dataset_path} {export_path} {train_part} {validation_part} {test_part} {train_mode} {alg}')
    
def Runbat(batfile_path):
    """
    batfile_path->str: バッチファイルのパス
    """
    batfile_path = batfile_path.replace('\\', '/')
    path = '/'.join(batfile_path.split('/')[:-1])
    with open(f'{path}/output.txt', 'w') as f:
        pass
    subprocess.Popen(batfile_path)
    
def generate_output_graph_bat(target_path, run_path, project_path):
    """
    target_path->str: "プロジェクト名/Scripts"絶対パス
    run_path->str: "仮想環境のactivate.batのパス"
    project_path->str: "プロジェクト名/Result"絶対パス
    """
    with open(target_path+'/output_model_graph_run.bat', 'w') as f:
            f.write(f'call "{run_path}"\npython {target_path}/output_model_graph.py {project_path}')

