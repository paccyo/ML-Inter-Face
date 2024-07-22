
import pandas as pd
import model_info
import sys
import numpy as np
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score, roc_curve, auc
from sklearn.preprocessing import label_binarize
import matplotlib.pyplot as plt
import japanize_matplotlib
from pydotplus import graph_from_dot_data
from sklearn.tree import export_graphviz
from sklearn.tree import plot_tree
import numpy as np
import seaborn as sns
import os
import shutil

FIRST = True

class TrainToolKit:
    """
    ML用学習ツールキット
    """

    def __init__(self, dataset_path, export_path, part):
        """
        project_path:str -> user_project/Result
        """
        self.dataset_path = dataset_path
        self.export_path = export_path
        self.train_part = part['train']
        self.validation_part = part['validation']
        self.test_part = part['test']

    def load_dataset(self):
        # 説明変数
        if self.train_part != 0:
            self.train_df_data = pd.read_csv(f'{self.dataset_path}/train_data.csv')
            self.train_df_target = pd.read_csv(f'{self.dataset_path}/train_target.csv')
            self.train_data = self.train_df_data.values
            self.train_target = np.array(self.train_df_target.values)
        
        if self.validation_part != 0:
            self.validation_df_data = pd.read_csv(f'{self.dataset_path}/validation_data.csv')
            self.validation_df_target = pd.read_csv(f'{self.dataset_path}/validation_target.csv')
            self.validation_data = self.validation_df_data.values
            self.validation_target = np.array(self.validation_df_target.values)

        if self.test_part != 0:
            self.test_df_data = pd.read_csv(f'{self.dataset_path}/test_data.csv')    
            self.test_df_target = pd.read_csv(f'{self.dataset_path}/test_target.csv')
            self.test_data = self.test_df_data.values
            self.test_target = np.array(self.test_df_target.values)
            
    def load_model(self):
        self.model = model_info.model_build()
        
    def train(self):
        self.model.fit(self.train_data, self.train_target.ravel())

def draw_border(clf, data, target, x_min=-6, x_max=6, y_min=-4, y_max=8, export_path=None):
    fig, ax = plt.subplots(figsize=(6, 6))

    xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.01), np.arange(y_min, y_max, 0.01))
    z = clf.predict(np.array([xx.ravel(), yy.ravel()]).T)
    z = np.array(conv_str_to_int(z))
    ax.contourf(xx, yy, z.reshape(xx.shape), cmap=plt.cm.coolwarm)
    ax.scatter(data[:, 0], data[:, 1], c=target, cmap=plt.cm.coolwarm)
    plt.savefig(f'{export_path}/border.png')

def draw_ROC(model, data, target, export_path):
    #ROC曲線の描画、AUCの計算（ROC曲線の下側の面積）の計算
    n_classes = len(model.classes_)
    classes = model.classes_
    y_test_one_hot = label_binarize(target, classes=classes)
    fpr = {}
    tpr = {}
    roc_auc = {}
    pred_proba = model.predict_proba(data)
    for i in range(n_classes):
        fpr[i], tpr[i], _ = roc_curve(y_test_one_hot[:, i], pred_proba[:, i])
        roc_auc[i] = auc(fpr[i], tpr[i])
    for i, class_ in enumerate(classes):
        plt.plot(fpr[i], tpr[i], label=f'{class_}')
    plt.legend()
    plt.savefig(f'{export_path}/ROC.png')

def export_score(target, pred, export_path):
    accuracy = str(accuracy_score(y_true=target, y_pred=pred))
    precision = str(precision_score(y_true=target, y_pred=pred, average='macro'))
    recall = str(recall_score(y_true=target, y_pred=pred, average='macro'))
    f1 = str(f1_score(y_true=target, y_pred=pred, average='macro'))
    matrix = confusion_matrix(y_true=target, y_pred=pred)
    with open(f'{export_path}/score_result.txt', 'w', encoding='utf-8') as f:
        f.write(f'{accuracy}\n{precision}\n{recall}\n{f1}')
    return matrix

def plot_confusion_matrix(cm, class_names, export_path):
    """
    プロット混同行列
    
    Args:
    cm (list of list of int): 混同行列
    class_names (list of str): クラス名のリスト
    """
    cm_array = np.array(cm)
    
    plt.figure(figsize=(8, 6))
    sns.heatmap(cm_array, annot=True, fmt="d", cmap="Blues", xticklabels=class_names, yticklabels=class_names)
    
    plt.xlabel('予測ラベル')
    plt.ylabel('正解ラベル')
    plt.title('混同行列')
    plt.savefig(f'{export_path}/confusion_matrix.png')

def reset_save_dir(export_path):
    if os.path.isdir(export_path):
        shutil.rmtree(export_path)
    os.makedirs(export_path, exist_ok=True)
    

def evaluate(model, data_type='validation', train_mode=None,  alg=None, data=None, target=None, columns=None, export_path=None):
    global FIRST
    """
    学習結果を評価/保存

    Parameters
    ----------
    model:model -> 学習したモデル
    data_type:str -> validation or test
    train_mode:str -> classifier or reg
    alg:str -> randomforest, decisiontree etc...
    data:any -> 推測させたいデータ
    target:any -> ターゲットラベル
    columns:pd.dataframe.columns -> カラム
    export_path:str -> 結果グラフ出力先
    """
    export_path = os.path.join(export_path, 'ML_result')
    if FIRST:
        reset_save_dir(export_path)
        FIRST = False
    data_class_num = len(columns)
    if data_type == 'validation' and train_mode == 'classifier':
        pred = model.predict(data)
        matrix = export_score(target, pred, export_path)
        draw_ROC(model, data, target, export_path)
        plot_confusion_matrix(matrix, model.classes_, export_path)
        if data_class_num == 2:
            draw_border(model, data, conv_str_to_int(target), export_path=export_path)
    
    if alg == 'randomforest':
        estimators = model.estimators_
        dot_data = export_graphviz(estimators[0], # 決定木オブジェクト
                                    out_file=None, # ファイルは介さずにGraphvizにdot言語データを渡す
                                    filled=True, # 分岐の際にどちらのノードに多く分類されたか
                                    rounded=True, # ノードの角を丸く描画
                                    # class_names=self.train_df_target.columns, #クラス名
                                    feature_names=columns, #説明変数
                                    special_characters=True # 特殊文字を扱える
                                    )
        graph = graph_from_dot_data(dot_data)
        file_name = "RandomForest.png"
        graph.write_png(f'{export_path}/{file_name}')

    if alg == 'decisiontree':
        if train_mode == 'classifier':
            plot_tree(model, feature_names=columns, class_names=model.classes_, filled=True)
        else:
            plot_tree(model, feature_names=columns, filled=True)
        plt.savefig(f'{export_path}/decisiontree.png')
        

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

_, dataset_path, export_path, train_part, validation_part, test_part, train_mode, alg  = sys.argv[0], sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6], sys.argv[7]
# _, dataset_path, export_path, train_part, validation_part, test_part, train_mode, alg  = None, r'test_data/dataset', r"test_data/test_dir", 6, 4, 0, 'classifier', 'decisiontree'
# train_mode = classifier or reg
# alg = decisiontree, randomforest, SVM
train_part, validation_part, test_part, int(train_part), int(validation_part), int(test_part)
kit = TrainToolKit(dataset_path, None, {'train':train_part, 'validation':validation_part, 'test':test_part})
kit.load_dataset()
kit.load_model()
kit.train()
evaluate(kit.model, data_type='validation', train_mode=train_mode, alg=alg, data=kit.validation_data, target=kit.validation_target, columns=kit.validation_df_data.columns, export_path=export_path)
if test_part != 0:
    evaluate(kit.model, data_type='test', train_mode=train_mode, alg=alg, data=kit.test_data, target=kit.test_target, columns=kit.test_df_data.columns, export_path=export_path)
