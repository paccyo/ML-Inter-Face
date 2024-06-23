
import pandas as pd


def MarginFrame(original, edit_part, target_col):
    original[target_col] = edit_part
    return original


if __name__ == '__main__':
    import preprocessing_dataframe
    pre = preprocessing_dataframe.Preprocess(r"C:\Users\yuuki\Documents\GUI_MLearning\ML-Inter-Face\test_data\data.csv")
    dd = pre.deal_null('Id', 'average')
    df = pd.read_csv(r"C:\Users\yuuki\Documents\GUI_MLearning\ML-Inter-Face\test_data\data.csv")
    dd2 = MarginFrame(df, dd, 'Id')
    print(dd2)