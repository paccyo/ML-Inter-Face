
import pandas as pd

class Preprocess:
    """
    dataframeの前処理を行います

    Parameters
    ----------
    data_path:str -> csvファイルのパスを指定
    """
    def __init__(self, data_path):
        self.df = pd.read_csv(data_path)

    def deal_null(self, col_name, deal_type):
        """
        欠損値処理を行います

        Parameters
        ----------
        col_name:str -> カラム名
        deal_type:str -> average, median
        """
        deal_df = self.df[col_name]
        if deal_type == 'average':
            deal_df = deal_df.fillna(deal_df.mean())
        elif deal_type == 'median':
            deal_df = deal_df.fillna(deal_df.median())
        return deal_df
    


if __name__ == '__main__':
    pre = Preprocess(r"C:\Users\yuuki\Documents\GUI_MLearning\ML-Inter-Face\test_data\data.csv")
    dd = pre.deal_null('Id', 'average')
    print(dd)