
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
        欠損値処理を行います。指定したカラム部分のみ返します。

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
    
    def MarginFrame(original, edit_part, target_col):
        """
        dataframeの更新を行う

        Parameters
        ----------
        original:pd.dataframe -> 基となるdataframe
        edit_part:pd.dataframe -> 更新したいカラムのdataframe
        target_col:str -> 更新したいカラム名
        """
        original[target_col] = edit_part
        return original


if __name__ == '__main__':
    pre = Preprocess(r"C:\Users\yuuki\Documents\GUI_MLearning\ML-Inter-Face\test_data\data.csv")
    dd = pre.deal_null('Id', 'average')
    original_df = pd.read_csv(r"C:\Users\yuuki\Documents\GUI_MLearning\ML-Inter-Face\test_data\data.csv")
    dd2 = pre.MarginFrame(original_df, dd, 'Id')
    print(dd2)