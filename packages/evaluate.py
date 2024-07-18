from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score, roc_curve, auc
from sklearn.preprocessing import label_binarize
import matplotlib.pyplot as plt
import japanize_matplotlib
from pydotplus import graph_from_dot_data
from sklearn.tree import export_graphviz
from sklearn.tree import plot_tree
import numpy as np
from packages import convert_type


def draw_border(clf, data, target, x_min=-6, x_max=6, y_min=-4, y_max=8, export_path=None):
    fig, ax = plt.subplots(figsize=(6, 6))

    xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.01), np.arange(y_min, y_max, 0.01))
    z = clf.predict(np.array([xx.ravel(), yy.ravel()]).T)
    z = np.array(convert_type.conv_str_to_int(z))
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
    matrix = f'{matrix[0, 0]} {matrix[0, 1]} {matrix[1, 0]} {matrix[1, 1]}'
    with open(f'{export_path}/score_result.txt', 'w', encoding='utf-8') as f:
        f.write(f'{accuracy}\n{precision}\n{recall}\n{f1}\n{matrix}')

def evaluate(model, data_type='validation', train_mode=None,  alg=None, data=None, target=None, columns=None, export_path=None):
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
    data_class_num = len(columns)
    if data_type == 'validation' and train_mode == 'classifier':
        pred = model.predict(data)
        export_score(target, pred, export_path)
        draw_ROC(model, data, target, export_path)
        if data_class_num == 2:
            draw_border(model, data, convert_type.conv_str_to_int(target), export_path=export_path)
    
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
        

