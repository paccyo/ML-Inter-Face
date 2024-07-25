
import matplotlib.pyplot as plt
import japanize_matplotlib
import seaborn as sns
import numpy as np


def plot_confusion_matrix(cm, class_names=None, export_path=None):
    """
    プロット混同行列
    
    Args:
    cm (list of list of int): 混同行列
    class_names (list of str): クラス名のリスト
    """
    cm_array = np.array(cm)
    
    plt.figure(figsize=(8, 6))
    if class_names:
        sns.heatmap(cm_array, annot=True, fmt="d", cmap="Blues", xticklabels=class_names, yticklabels=class_names)
    else:
        sns.heatmap(cm_array, annot=True, fmt="d", cmap="Blues")
    
    plt.xlabel('予測ラベル')
    plt.ylabel('正解ラベル')
    plt.title('混同行列')
    plt.show()
    # plt.savefig(f'{export_path}/confusion_matrix.png')

matrix = [[0, 0],
          [0, 0]]
plot_confusion_matrix(matrix)