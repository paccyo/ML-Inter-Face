
import pandas as pd
from autoviz.AutoViz_Class import AutoViz_Class
import matplotlib.pyplot as plt


class DS:
    
    def __init__(self):
        self.df = None
        self.file_name = 'DS_data.csv'
        self.file_path = None

    def send(self, data, export_dir_data, export_dir_result):
        self.load_dataframe(data, export_dir_data)
        self.analyze(export_dir_result)

    def load_dataframe(self, data, export_dir):
        if type(data) == str:
            self.df = pd.read_csv(data)
        elif type(data) == pd.DataFrame:
            self.df = data
        self.file_path = f'{export_dir}/{self.file_name}'
        self.df_to_csv()

    def df_to_csv(self):
        self.df.to_csv(self.file_path)
        
    def analyze(self, export_dir):
        # AutoVizのインスタンスを作成
        AV = AutoViz_Class()
        # AutoVizを使ってデータを可視化
        dft = AV.AutoViz(
            self.file_path,
            depVar="",  # 目的変数名（必要に応じて変更）
            dfte=None,
            header=0,
            sep=",",
            verbose=0,
            lowess=False,
            chart_format="html",
            save_plot_dir=f'{export_dir}/DS_result'
        )


if __name__ == '__main__':
    ds = DS()
    ds.send(data=r"C:\Users\Yuuki\Documents\GUI_MLearning\ML-Inter-Face\test_data\data.csv",
            export_dir_data=r"C:\Users\Yuuki\Documents\GUI_MLearning\ML-Inter-Face\test_data\test_dir",
            export_dir_result=r"C:\Users\Yuuki\Documents\GUI_MLearning\ML-Inter-Face\test_data\test_dir")