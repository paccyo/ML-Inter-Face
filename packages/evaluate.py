from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score, roc_curve, auc
from sklearn.preprocessing import label_binarize
import matplotlib.pyplot as plt
import japanize_matplotlib
from pydotplus import graph_from_dot_data
from sklearn.tree import export_graphviz
from sklearn.tree import plot_tree
import numpy as np

def simulate(clf, data, target, x_min=-6, x_max=6, y_min=-4, y_max=8):
    fig, ax = plt.subplots(1, 2, figsize=(18, 6))

    xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.01), np.arange(y_min, y_max, 0.01))
    z = clf.predict(np.array([xx.ravel(), yy.ravel()]).T)
    ax[0].contourf(xx, yy, z.reshape(xx.shape), alpha=0.2, cmap=plt.cm.coolwarm)
    ax[0].scatter(data[:, 0], data[:, 1], c=target, s=10, cmap=plt.cm.coolwarm)
    plt.show()


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
        print('accuracy：', accuracy_score(y_true=target, y_pred=pred))
        print('precision：', precision_score(y_true=target, y_pred=pred, average='macro'))
        print('recall：', recall_score(y_true=target, y_pred=pred, average='macro'))
        print('f1 score：', f1_score(y_true=target, y_pred=pred, average='macro'))
        print('confusion matrix = \n', confusion_matrix(y_true=target, y_pred=pred))
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
        plt.show()

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
        file_name = "RandomForest_visualization.png"
        graph.write_png(file_name)

    if alg == 'decisiontree':
        if train_mode == 'classifier':
            plot_tree(model, feature_names=columns, class_names=model.classes_, filled=True)
        else:
            plot_tree(model, feature_names=columns, filled=True)
        plt.show()

    if alg == 'SVM' and data_class_num == 2:
