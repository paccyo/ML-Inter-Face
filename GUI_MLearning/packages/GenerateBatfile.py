
import subprocess

def generate(target_path, run_path, part_dict, data_type, epochs, batchs=None, project_path=None):
    """
    target_path->str: "プロジェクト名/Scripts"絶対パス
    run_path->str: "仮想環境のactivate.batのパス"
    project_path->str: 
    """
    train_part = part_dict['train']
    validatioin_part = part_dict['validation']
    test_part = part_dict['test']
    if data_type == 'image':
        with open(target_path+'/run.bat', 'w') as f:
            f.write(f'call "{run_path}"\n{target_path}/RunTrain.py {train_part} {validatioin_part} {test_part} {data_type} {epochs} {batchs} {project_path}')
        # f.write(f'echo trainstart\npause\n{run_path}\npause\nstart {target_path}/RunTrain.py\npause\necho fin\npause')

def Runbat(batfile_path):
    """
    batfile_path->str: バッチファイルのパス
    """
    batfile_path = batfile_path.replace('\\', '/')
    path = '/'.join(batfile_path.split('/')[:-1])
    with open(f'{path}/output.txt', 'w') as f:
        pass
    subprocess.run(batfile_path, 
                   stdout=f'{path}/output.txt', stderr=f'{path}/output.txt'
                     )
    
def generate_output_graph_bat(target_path, run_path, project_path):
    """
    target_path->str: "プロジェクト名/Scripts"絶対パス
    run_path->str: "仮想環境のactivate.batのパス"
    project_path->str: "プロジェクト名/Result"絶対パス
    """
    with open(target_path+'/output_model_graph_run.bat', 'w') as f:
            f.write(f'call "{run_path}"\n{target_path}/output_model_graph.py {project_path}')

