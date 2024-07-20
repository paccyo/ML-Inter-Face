
from util import Calldict

with open(r'C:\Users\Yuuki\Documents\GUI_MLearning\ML-Inter-Face\model_info_NN.py') as f:
    code_lines = f.readlines()

deal_start = False
for code_line in code_lines:
    if 'def model_build():' in code_line:
        deal_start = True
        continue
    if not deal_start:
        continue
    code_line = code_line.replace(' ', '')
    print(code_line)
