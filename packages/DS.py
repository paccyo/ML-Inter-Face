
import pandas as pd
from autoviz.AutoViz_Class import AutoViz_Class
import matplotlib.pyplot as plt
from io import StringIO


class DS:
    
    def __init__(self):
        self.df = None
        self.file_name = 'DS_data.csv'
        
    def send(self, data, export_dir_result):
        self.load_dataframe(data)
        self.analyze(export_dir_result)

    def load_dataframe(self, data):
        if type(data) == str:
            self.df = pd.read_csv(data)
        elif type(data) == pd.DataFrame:
            self.df = data
        
    def analyze(self, export_dir):
        # AutoVizのインスタンスを作成
        AV = AutoViz_Class()
        # AutoVizを使ってデータを可視化
        print(self.df)
        dft = AV.AutoViz(
            filename=None,
            dfte=self.df,
            depVar="",  # 目的変数名（必要に応じて変更）
            header=0,
            verbose=1,
            lowess=True,
            chart_format="html",
            save_plot_dir=f'{export_dir}/DS_result'
        )


if __name__ == '__main__':
    ds = DS()
    ds.send(data=r"C:\Users\Yuuki\Documents\GUI_MLearning\ML-Inter-Face\test_data\train_data.csv",
            export_dir_result=r"C:\Users\Yuuki\Documents\GUI_MLearning\ML-Inter-Face\test_data\test_dir")