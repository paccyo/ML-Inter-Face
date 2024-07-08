

def conv_str_to_int(df_target):
    """
    dataframeの文字を数値化
    """
    labels_str = []
    labels = []
    for data in df_target:
        if data not in labels_str:
            labels_str.append(data)
    for data in df_target:
        labels.append(labels_str.index(data))
    return labels