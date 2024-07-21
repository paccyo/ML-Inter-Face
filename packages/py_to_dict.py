
from util import Calldict

with open(r'C:\Users\Yuuki\Documents\GUI_MLearning\ML-Inter-Face\model_info_NN.py') as f:
    code_lines = f.readlines()
original_dic = Calldict.layer_dicts
deal_start = False
first = True
for i, code_line in enumerate(code_lines):
    if 'def model_build():' in code_line:
        deal_start = True
        continue
    elif 'return' in code_line:
        continue
    elif 'Model' in code_line:
        continue
    if not deal_start:
        continue
    code_line = code_line.replace(' ', '').replace('\n', '')
    layer_name = code_line.split('=')[1].split('(')[0]

    start_index = None
    end_index = None
    c = 0
    for j, letter in enumerate(code_line):
        if letter == '(':
            start_index = j+1
            break
    for j, letter in enumerate(code_line[::-1]):
        if letter == ')':
            c += 1
            if c == 2 or first:
                end_index = -(j+1)
                first = False
                break
    print(code_line[start_index:end_index])
    # for j, param in enumerate(code_line[start_index:end_index].split('=')):
    #     if j == 0:
    #         param_name = param
        



if __name__ == '__main__':
    [{'Input': {
                'shape': ['None', 'DropDown', ['None'], 'MAIN', '入力データの形状を指定します。通常、バッチサイズを除いたデータの次元数を指定します。'],
                'batch_size': ['None', 'TextField', 1, 'DETAIL', 'バッチサイズを指定します。Noneを指定すると任意のバッチサイズで入力可能です。'],
                'dtype': ['None', 'DropDown', ['None', 'float32', 'int32'], 'DETAIL', '入力データのデータ型を指定します。'],
                'sparse': ['False', 'DropDown', ['True', 'False'], 'DETAIL', '入力がスパーステンソルであるかどうかを指定します。'],
                'batch_shape': ['None', 'DropDown', ['None'], 'DETAIL', '入力データの完全な形状（バッチサイズを含む）を指定します。'],
                'name': ['None', 'DropDown', ['None'], 'DETAIL', 'このレイヤーの名前を指定します。'],
                'tensor': ['None', 'DropDown', ['None'], 'DETAIL', 'テンソルを指定します。'],
                'color':'AAAA',
                'detail_view':'False'
            }},
    {'Input': {
                'shape': ['None', 'DropDown', ['None'], 'MAIN', '入力データの形状を指定します。通常、バッチサイズを除いたデータの次元数を指定します。'],
                'batch_size': ['None', 'TextField', 1, 'DETAIL', 'バッチサイズを指定します。Noneを指定すると任意のバッチサイズで入力可能です。'],
                'dtype': ['None', 'DropDown', ['None', 'float32', 'int32'], 'DETAIL', '入力データのデータ型を指定します。'],
                'sparse': ['False', 'DropDown', ['True', 'False'], 'DETAIL', '入力がスパーステンソルであるかどうかを指定します。'],
                'batch_shape': ['None', 'DropDown', ['None'], 'DETAIL', '入力データの完全な形状（バッチサイズを含む）を指定します。'],
                'name': ['None', 'DropDown', ['None'], 'DETAIL', 'このレイヤーの名前を指定します。'],
                'tensor': ['None', 'DropDown', ['None'], 'DETAIL', 'テンソルを指定します。'],
                'color':'AAA',
                'detail_view':'False'
            }}]