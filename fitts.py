from sklearn.linear_model import LinearRegression
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

# 空のリストを作成
mt_list = []
id_list = []

# CSVファイルを開いてデータを追加
def add_data(filename, distance, width):
    df = pd.read_csv(filename)
    time = df['time']
    mt_list.append(sum(time) / len(time))
    id_list.append(np.log2((distance / width) + 1))

# データを追加
add_data('d250w40.csv', 250, 40)
add_data('d250w90.csv', 250, 90)
add_data('d250w120.csv', 250, 120)
add_data('d450w40.csv', 450, 40)
add_data('d450w90.csv', 450, 90)
add_data('d450w120.csv', 450, 120)
add_data('d650w40.csv', 650, 40)
add_data('d650w90.csv', 650, 90)
add_data('d650w120.csv', 650, 120)

# リストをNumPy配列に変換
mt = np.array(mt_list).reshape(-1, 1)  # 2次元配列に変換
id = np.array(id_list)

# 線形回帰モデルの作成とフィッティング
model = LinearRegression()
model.fit(mt, id)

# モデルの係数と切片を表示
print(f"係数: {model.coef_}")
print(f"切片: {model.intercept_}")
print (f"スループット：{1 / model.coef_[0]}")

# プロット（オプション）
plt.scatter(mt, id, color='blue')
plt.plot(mt, model.predict(mt), color='red')
plt.xlabel('MT')
plt.ylabel('ID')
plt.show()