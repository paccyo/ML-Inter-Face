import numpy as np
import pandas as pd
import math
import time


a = [-0.059280682,0.058615096,0.09117813,0.020459421,0.04510887,0.037429675,0.042110104,-0.019559938,-0.024425546,0.038655855,0.020860983,0.021883648,-0.03120617,0.07780125,-0.024075419,-0.07219774,-0.0032493684,0.062655635,-0.022691369,-0.031314023,0.07973798,0.04796437,-0.023371743,0.064071275,-0.015762465,0.00553486,-0.03520594,0.0315,-0.05898746,0.0147251,0.027714513,-0.059989907,0.037369937,0.007991392,0.008469145,-0.0145170605,0.07032497,-0.035304893,-0.014931377,-0.05293094,-0.05809139,0.019008549,-0.028819444,0.05113664,-0.063304506,-0.062599786,0.00067924825,0.011555208,0.019008698,-0.046696156,-0.013828173,0.05297825,-0.054301143,0.024645874,-0.062832616,0.06689897,-0.052238017,-0.017278599,0.035736393,-0.057138536,-0.053246237,-0.015210348,-0.061629087,-0.014502512]
print(len(a))
exit()

# サンプルデータの作成 (ランダムな値を持つ4次元データ)
data = np.random.rand(2, 3, 4, 2, 32)
data = np.random.rand(4, 2, 32)

# データの形状を確認
print("Original shape:", data.shape)

# データを2次元に変換 (2, 3, 4, 2, 32) -> (3*4*2, 2, 32) = (24, 2, 32)

d = (2, 3, 4, 2, 32)
d = (100, 100, 100, 100, 100, 32)
st = time.time()
if len(data.shape) > 2:
    d_loop = list(d)[:-2]
    # d_loop = list(data.shape)[:-2]
    d_loop.insert(0, 1)
    d_loop.append(1)
    result = []
    d_loop = d_loop[::-1]
    for i, dim in enumerate(d_loop[1:-1]):
        i += 1
        inner_iter_num = math.prod(d_loop[:i-1])*d_loop[i-1]
        outer_iter_num = math.prod(d_loop[i+1:])
        if i == 1:
            r = [j*inner_iter_num for j in list(range(1, dim+1))]*outer_iter_num
        else:
            r = np.array([[j]*inner_iter_num for j in list(range(1, dim+1))]*outer_iter_num).reshape(-1,)
        result.append(r)
    result = result[::-1]
    result.append([data.shape[-2]]*len(result[0]))
    result.append([data.shape[-1]]*len(result[0]))
et = time.time()
print(et-st)
    # print(np.array(result).T)
        


exit()
(1, 1, 1, 2, 32)
(1, 1, 2, 2, 32)
(1, 1, 3, 2, 32)
(1, 1, 4, 2, 32)
(1, 2, 1, 2, 32)
(1, 2, 2, 2, 32)
(1, 2, 3, 2, 32)
(1, 2, 4, 2, 32)
(1, 3, 1, 2, 32)
(1, 3, 2, 2, 32)
(1, 3, 3, 2, 32)
(1, 3, 4, 2, 32)
(2, 1, 1, 2, 32)
(2, 1, 2, 2, 32)
(2, 1, 3, 2, 32)
(2, 1, 4, 2, 32)
(2, 2, 1, 2, 32)
(2, 2, 2, 2, 32)
(2, 2, 3, 2, 32)
(2, 2, 4, 2, 32)
(2, 3, 1, 2, 32)
(2, 3, 2, 2, 32)
(2, 3, 3, 2, 32)
(2, 3, 4, 2, 32)

dims_num = len(data.shape)
if dims_num > 2:
    dims_num -= 2


data_2d = data.reshape(-1, 32)

# 2次元データの形状を確認
print("Reshaped shape:", data_2d.shape)

# データフレームに変換
df = pd.DataFrame(data_2d)

# CSVファイルに書き出し
df.to_csv('output.csv', index=False)

print("Data has been written to output.csv")
