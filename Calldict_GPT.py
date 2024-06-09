preprocess_dicts = {
    'ImageDataGenerator': {
        'featurewise_center': ['False', 'DropDown', ['True', 'False'], 'DETAIL', 'データセット全体の中心化を行うかどうかを指定します。'],
        'samplewise_center': ['False', 'DropDown', ['True', 'False'], 'DETAIL', '各サンプルの中心化を行うかどうかを指定します。'],
        'featurewise_std_normalization': ['False', 'DropDown', ['True', 'False'], 'DETAIL', 'データセット全体の標準偏差で正規化するかどうかを指定します。'],
        'samplewise_std_normalization': ['False', 'DropDown', ['True', 'False'], 'DETAIL', '各サンプルの標準偏差で正規化するかどうかを指定します。'],
        'zca_whitening': ['False', 'DropDown', ['True', 'False'], 'DETAIL', 'ZCA白色化を適用するかどうかを指定します。'],
        'zca_epsilon': [1e-06, 'TextField', 1, 'DETAIL', 'ZCA白色化のためのイプシロンを指定します。'],
        'rotation_range': [0, 'TextField', 1, 'DETAIL', 'ランダム回転の範囲を度単位で指定します。'],
        'width_shift_range': [0.0, 'TextField', 1, 'DETAIL', 'ランダム水平シフトの範囲を指定します。'],
        'height_shift_range': [0.0, 'TextField', 1, 'DETAIL', 'ランダム垂直シフトの範囲を指定します。'],
        'brightness_range': [['None', [0.0, 1.0]], ['DropDown', 'TextField'], [['None', 'True'], 2], 'DETAIL', 'ランダム明度シフトの範囲を指定します。'],
        'shear_range': [0.0, 'TextField', 1, 'DETAIL', 'ランダムせん断の範囲を指定します。'],
        'zoom_range': [0.0, 'TextField', 1, 'DETAIL', 'ランダムズームの範囲を指定します。'],
        'channel_shift_range': [0.0, 'TextField', 1, 'DETAIL', 'ランダムチャネルシフトの範囲を指定します。'],
        'fill_mode': ['nearest', 'DropDown', ['reflect', 'nearest'], 'DETAIL', '境界の埋め方を指定します。'],
        'cval': [0.0, 'TextField', 1, 'DETAIL', '境界外のピクセルに使用する値を指定します。'],
        'horizontal_flip': ['False', 'DropDown', ['True', 'False'], 'DETAIL', 'ランダムに水平反転を行うかどうかを指定します。'],
        'vertical_flip': ['False', 'DropDown', ['True', 'False'], 'DETAIL', 'ランダムに垂直反転を行うかどうかを指定します。'],
        'rescale': ['None', 'DropDown', ['None', 1./255], 'MAIN', '再スケーリング係数を指定します。'],
        'data_format': ['channels_last', 'DropDown', ['channels_first', 'channels_last'], 'DETAIL', 'データのフォーマットを指定します。'],
        'interpolation_order': [1, 'DropDown', [0, 1, 2, 3], 'DETAIL', '補間の順序を指定します。'],
        'dtype': ['None', 'DropDown', ['None', 'float32', 'float64', 'uint8'], 'MAIN', 'データ型を指定します。']
    },
    'flow_from_directory': {
        'target_size': [(256, 256), 'TextField', 2, 'MAIN', 'ターゲットサイズ（高さ、幅）を指定します。'],
        'color_mode': ['rgb', 'DropDown', ['rgb', 'grayscale'], 'MAIN', 'カラーモードを指定します。'],
        'class_mode': ['categorical', 'DropDown', ['categorical', 'binary', 'sparse', 'input', 'none'], 'MAIN', 'ラベルの種類を指定します。'],
        'batch_size': [32, 'TextField', 1, 'MAIN', 'バッチサイズを指定します。'],
        'shuffle': ['False', 'DropDown', ['True', 'False'], 'MAIN', 'シャッフルするかどうかを指定します。'],
        'seed': ['None', 'TextField', 1, 'DETAIL', '乱数シードを指定します。'],
        'interpolation': ['nearest', 'DropDown', ['nearest', 'bilinear', 'bicubic', 'lanczos', 'box', 'hamming'], 'DETAIL', '補間方法を指定します。']
    }
}

compile_dicts = {
    'optimizer': {
        'Adam': {
            'learning_rate': [0.001, 'TextField', 1, 'MAIN', '学習率を指定します。'],
            'beta_1': [0.9, 'TextField', 1, 'DETAIL', '1番目のモーメント推定の減衰率を指定します。'],
            'beta_2': [0.999, 'TextField', 1, 'DETAIL', '2番目のモーメント推定の減衰率を指定します。'],
            'epsilon': [1e-07, 'TextField', 1, 'DETAIL', '数値安定性のための小さな定数を指定します。'],
            'decay': ['None', 'TextField', 1, 'DETAIL', '学習率の減衰を指定します。'],
            'clipnorm': ['None', 'TextField', 1, 'DETAIL', '勾配ノルムクリッピングを指定します。'],
            'clipvalue': ['None', 'TextField', 1, 'DETAIL', '勾配値クリッピングを指定します。'],
            'global_clipnorm': ['None', 'TextField', 1, 'DETAIL', 'グローバル勾配ノルムクリッピングを指定します。']
        }
    },
    'loss': ['None', 'DropDown', ['None', 'categorical_crossentropy', 'binary_crossentropy'], 'MAIN', '損失関数を指定します。'],
    'metrics': ['None', 'DropDown', ['None', 'acc'], 'MAIN', '評価指標を指定します。']
}
