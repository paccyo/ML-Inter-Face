
from packages.util import Calldict
import re


def convert_model_to_dict(path):
    """
    model_info.pyをdictに変換します。
    """
    with open(path) as f:
        code_lines = f.readlines()
    original_layer_dic = Calldict.layer_dicts
    deal_start = False
    first = True
    result = []
    temp_result = {}
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
        # レイヤ名
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
        text = code_line[start_index:end_index]
        pattern = r'\(([^)]+)\)'
        pattern_list = []
        # パターンに一致する部分をすべて見つける
        matches = re.findall(pattern, text)
        for m in matches:
            pattern_list.append(m)
        for j, pat in enumerate(pattern_list):
            text = text.replace(pat, f'#{j}')
        text_list = text.split(',')
        for txt in text_list:
            # パラメータ名, パラメータ値
            param_name, param_value = txt.split('=')
            param_dic = original_layer_dic[layer_name]
            try:
                int(param_value)
            except:
                param_value = param_value.replace('\'', '').replace('\"', '')
                if '#' in param_value:
                    index = param_value[2:-1]
                    param_value_text = pattern_list[int(index)]
                    param_value = tuple(map(int, param_value_text.split(',')))
                param_dic[param_name][0] = param_value
            else:
                if '.' in param_value:
                    param_value = float(param_value)
                else:
                    param_value = int(param_value)
                param_dic[param_name][0] = param_value
        temp_result[layer_name] = param_dic
        result.append(temp_result)
    return result
        
    

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
    
result = convert_model_to_dict(r'C:\Users\Yuuki\Documents\GUI_MLearning\ML-Inter-Face\model_info_NN.py')
print(result)
