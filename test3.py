import numpy as np
import pandas as pd

# サンプルデータの作成 (ランダムな値を持つ4次元データ)
data = np.random.rand(3, 3, 2, 32)

# データの形状を確認
print("Original shape:", data.shape)

# データを2次元に変換 (3, 3, 2, 32) -> (3*3*2, 32) = (18, 32)
dims_num = len(data.shape)
data_2d = data.reshape(-1, 32)

# 2次元データの形状を確認
print("Reshaped shape:", data_2d.shape)

# データフレームに変換
df = pd.DataFrame(data_2d)

# CSVファイルに書き出し
df.to_csv('output.csv', index=False)

print("Data has been written to output.csv")
