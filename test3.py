import numpy as np
import pandas as pd
import math
import time


# サンプルデータの作成 (ランダムな値を持つ4次元データ)
data = np.random.rand(2, 3, 4, 2, 32)
data = np.random.rand(4, 2, 32)

# データの形状を確認
print("Original shape:", data.shape)

# データを2次元に変換 (2, 3, 4, 2, 32) -> (3*4*2, 2, 32) = (24, 2, 32)

d = (3, 3, 1, 32)
# d = (100, 100, 100, 100, 100, 32)
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
print(np.array(result).T)
        


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
