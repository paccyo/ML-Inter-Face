layer_dicts = {
    'Input': {
        'shape': ['None', 'DropDown', ['None'], 'MAIN', '入力データの形状を指定します。通常、バッチサイズを除いたデータの次元数を指定します。'],
        'batch_size': ['None', 'TextField', 1, 'DETAIL', 'バッチサイズを指定します。Noneを指定すると任意のバッチサイズで入力可能です。'],
        'dtype': ['None', 'DropDown', ['None', 'float32', 'int32'], 'DETAIL', '入力データのデータ型を指定します。'],
        'sparse': ['False', 'DropDown', ['True', 'False'], 'DETAIL', '入力がスパーステンソルであるかどうかを指定します。'],
        'batch_shape': ['None', 'DropDown', ['None'], 'DETAIL', '入力データの完全な形状（バッチサイズを含む）を指定します。'],
        'name': ['None', 'DropDown', ['None'], 'DETAIL', 'このレイヤーの名前を指定します。'],
        'tensor': ['None', 'DropDown', ['None'], 'DETAIL', 'テンソルを指定します。'],
        'color': ft.colors.GREY
    },
    
    'Dense': {
        'units': [0, 'TextField', 1, 'MAIN', '出力空間の次元数を指定します。'],
        'use_bias': ['True', 'DropDown', ['True', 'False'], 'DETAIL', 'バイアス項を使用するかどうかを指定します。'],
        'kernel_initializer': ['glorot_uniform', 'DropDown', ['None', 'ones', 'he_normal()', 'truncated_normal()', 'random_normal'], 'DETAIL', 'カーネルの初期化方法を指定します。'],
        'bias_initializer': ['zeros', 'DropDown', ['None', 'zeros'], 'DETAIL', 'バイアスの初期化方法を指定します。'],
        'kernel_regularizer': ['None', 'DropDown', ['None', 'L1L2(l1=1e-4, l2=1e-4)', 'L1(1e-4)', 'L2(1e-4)'], 'DETAIL', 'カーネルに対する正則化を指定します。'],
        'bias_regularizer': ['None', 'DropDown', ['None', 'L1L2(l1=1e-4, l2=1e-4)', 'L1(1e-4)', 'L2(1e-4)'], 'DETAIL', 'バイアスに対する正則化を指定します。'],
        'activity_regularizer': ['None', 'DropDown', ['None', 'L1L2(l1=1e-4, l2=1e-4)', 'L1(1e-4)', 'L2(1e-4)'], 'DETAIL', '出力に対する正則化を指定します。'],
        'kernel_constraint': ['None', 'DropDown', ['None', 'max_norm(2.)'], 'DETAIL', 'カーネルに対する制約を指定します。'],
        'bias_constraint': ['None', 'DropDown', ['None'], 'DETAIL', 'バイアスに対する制約を指定します。'],
        'color': ft.colors.AMBER
    },
    
    'Activation': {
        'activation': ['None', 'DropDown', ['None', 'relu', 'sigmoid', 'gelu', 'softmax', 'tanh'], 'MAIN', '適用するアクティベーション関数を指定します。'],
        'color': ft.colors.YELLOW
    },
    
    'Conv2D': {
        'filters': [0, 'TextField', 1, 'MAIN', '出力フィルタの数を指定します。'],
        'kernel_size': [(1, 1), 'TextField', 2, 'MAIN', 'カーネル（フィルタ）のサイズを指定します。'],
        'strides': [(1, 1), 'TextField', 2, 'MAIN', 'ストライドのサイズを指定します。'],
        'padding': ['valid', 'DropDown', ['valid', 'same'], 'MAIN', 'パディングの方法を指定します。'],
        'data_format': ['channels_last', 'DropDown', ['channels_first', 'channels_last'], 'DETAIL', 'データのフォーマットを指定します。'],
        'dilation_rate': [(1, 1), 'TextField', 2, 'DETAIL', '畳み込みを行う際の拡張率を指定します。'],
        'groups': [1, 'TextField', 1, 'DETAIL', 'グループ数を指定します。'],
        'use_bias': ['True', 'DropDown', ['True', 'False'], 'DETAIL', 'バイアス項を使用するかどうかを指定します。'],
        'kernel_initializer': ['glorot_uniform', 'DropDown', ['None', 'ones', 'he_normal()', 'truncated_normal()', 'random_normal'], 'DETAIL', 'カーネルの初期化方法を指定します。'],
        'bias_initializer': ['zeros', 'DropDown', ['None', 'zeros'], 'DETAIL', 'バイアスの初期化方法を指定します。'],
        'kernel_regularizer': ['None', 'DropDown', ['None', 'L1L2(l1=1e-4, l2=1e-4)', 'L1(1e-4)', 'L2(1e-4)'], 'DETAIL', 'カーネルに対する正則化を指定します。'],
        'bias_regularizer': ['None', 'DropDown', ['None', 'L1L2(l1=1e-4, l2=1e-4)', 'L1(1e-4)', 'L2(1e-4)'], 'DETAIL', 'バイアスに対する正則化を指定します。'],
        'activity_regularizer': ['None', 'DropDown', ['None', 'L1L2(l1=1e-4, l2=1e-4)', 'L1(1e-4)', 'L2(1e-4)'], 'DETAIL', '出力に対する正則化を指定します。'],
        'kernel_constraint': ['None', 'DropDown', ['None', 'max_norm(2.)'], 'DETAIL', 'カーネルに対する制約を指定します。'],
        'bias_constraint': ['None', 'DropDown', ['None'], 'DETAIL', 'バイアスに対する制約を指定します。'],
        'color': ft.colors.GREEN_100
    },
    
    'MaxPooling2D': {
        'pool_size': [(2, 2), 'TextField', 2, 'MAIN', 'プーリング窓のサイズを指定します。'],
        'strides': [(1, 1), 'TextField', 2, 'MAIN', 'ストライドのサイズを指定します。'],
        'padding': ['valid', 'DropDown', ['valid', 'same'], 'MAIN', 'パディングの方法を指定します。'],
        'data_format': ['channels_last', 'DropDown', ['channels_first', 'channels_last'], 'DETAIL', 'データのフォーマットを指定します。'],
        'name': ['None', 'DropDown', ['None'], 'DETAIL', 'このレイヤーの名前を指定します。'],
        'color': ft.colors.BLUE_100
    },
    
    'AveragePooling2D': {
        'pool_size': [(2, 2), 'TextField', 2, 'MAIN', 'プーリング窓のサイズを指定します。'],
        'strides': [(1, 1), 'TextField', 2, 'MAIN', 'ストライドのサイズを指定します。'],
        'padding': ['valid', 'DropDown', ['valid', 'same'], 'MAIN', 'パディングの方法を指定します。'],
        'data_format': ['channels_last', 'DropDown', ['channels_first', 'channels_last'], 'DETAIL', 'データのフォーマットを指定します。'],
        'name': ['None', 'DropDown', ['None'], 'DETAIL', 'このレイヤーの名前を指定します。'],
        'color': ft.colors.BLUE_GREY_100
    },
    
    'GlobalMaxPooling2D': {
        'data_format': ['channels_last', 'DropDown', ['channels_first', 'channels_last'], 'DETAIL', 'データのフォーマットを指定します。'],
        'keepdims': ['False', 'DropDown', ['False', 'True'], 'DETAIL', '次元を保持するかどうかを指定します。'],
        'color': ft.colors.BLUE_ACCENT_100
    },
    
    'GlobalAveragePooling2D': {
        'data_format': ['channels_last', 'DropDown', ['channels_first', 'channels_last'], 'DETAIL', 'データのフォーマットを指定します。'],
        'keepdims': ['False', 'DropDown', ['False', 'True'], 'DETAIL', '次元を保持するかどうかを指定します。'],
        'color': ft.colors.LIGHT_BLUE_ACCENT_100
    },
    
    'Dropout': {
        'rate': [0.0, 'TextField', 0.01, 'MAIN', 'ドロップアウト率を指定します。0から1の間の浮動小数点数。'],
        'noise_shape': ['None', 'TextField', 1, 'DETAIL', '入力のどの要素がドロップアウトされるかを指定します。'],
        'seed': ['None', 'TextField', 1, 'DETAIL', 'ランダムシードを指定します。'],
        'color': ft.colors.TEAL_100
    },
    
    'Flatten': {
        'data_format': ['None', 'DropDown', ['None', 'channels_first', 'channels_last'], 'DETAIL', 'データのフォーマットを指定します。'],
        'color': ft.colors.PINK_100
    },
    
    'Reshape': {
        'target_shape': ['None', 'TextField', 1, 'MAIN', 'ターゲットの形状を指定します。バッチサイズを含めずに指定します。'],
        'color': ft.colors.PURPLE_100
    },
    
    'BatchNormalization': {
        'axis': [-1, 'TextField', 1, 'MAIN', '正規化を行う軸を指定します。'],
        'momentum': [0.99, 'TextField', 0.01, 'MAIN', '移動平均のモメンタムを指定します。'],
        'epsilon': [0.001, 'TextField', 0.0001, 'MAIN', '分母に追加される小さな定数を指定します。'],
        'center': ['True', 'DropDown', ['True', 'False'], 'DETAIL', 'バイアス項を追加するかどうかを指定します。'],
        'scale': ['True', 'DropDown', ['True', 'False'], 'DETAIL', 'スケーリングを行うかどうかを指定します。'],
        'beta_initializer': ['zeros', 'DropDown', ['zeros', 'ones', 'random_normal', 'random_uniform'], 'DETAIL', 'バイアスの初期化方法を指定します。'],
        'gamma_initializer': ['ones', 'DropDown', ['zeros', 'ones', 'random_normal', 'random_uniform'], 'DETAIL', 'スケーリング係数の初期化方法を指定します。'],
        'moving_mean_initializer': ['zeros', 'DropDown', ['zeros', 'ones', 'random_normal', 'random_uniform'], 'DETAIL', '移動平均の初期化方法を指定します。'],
        'moving_variance_initializer': ['ones', 'DropDown', ['zeros', 'ones', 'random_normal', 'random_uniform'], 'DETAIL', '移動分散の初期化方法を指定します。'],
        'color': ft.colors.LIGHT_GREEN_100
    }
}
