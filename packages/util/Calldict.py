import flet as ft

DROPDOWN = "DropDown"
TEXTFIELD = "TextField"
MAIN = "MAIN"
DETAIL = "DETAIL"

layer_dicts = {
        'Input': {
            'shape': ['None', 'DropDown', ['None'], 'MAIN', '入力データの形状を指定します。通常、バッチサイズを除いたデータの次元数を指定します。'],
            'batch_size': ['None', 'TextField', 1, 'DETAIL', 'バッチサイズを指定します。Noneを指定すると任意のバッチサイズで入力可能です。'],
            'dtype': ['None', 'DropDown', ['None', 'float32', 'int32'], 'DETAIL', '入力データのデータ型を指定します。'],
            'sparse': ['False', 'DropDown', ['True', 'False'], 'DETAIL', '入力がスパーステンソルであるかどうかを指定します。'],
            'batch_shape': ['None', 'DropDown', ['None'], 'DETAIL', '入力データの完全な形状（バッチサイズを含む）を指定します。'],
            'name': ['None', 'DropDown', ['None'], 'DETAIL', 'このレイヤーの名前を指定します。'],
            'tensor': ['None', 'DropDown', ['None'], 'DETAIL', 'テンソルを指定します。'],
            'color':ft.colors.GREY,
            'detail_view':'False',
            'description':'入力データの形状を定義するためのレイヤーです。'
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
            'color':ft.colors.AMBER,
            'detail_view':'False',
            'description':'全結合（フルコネクション）ニューラルネットワークレイヤーで、各入力ノードをすべての出力ノードに接続します。'
        },
        
        'Activation': {
            'activation': ['None', 'DropDown', ['None', 'relu', 'sigmoid', 'gelu', 'softmax', 'tanh'], 'MAIN', '適用するアクティベーション関数を指定します。'],
            'color':ft.colors.YELLOW,
            'detail_view':'False',
            'description':'指定されたアクティベーション関数を適用して、入力に非線形性を導入するためのレイヤーです。'
        },
        # 'Embedding': {
        #     'input_dim': None,
        #     'output_dim': None,
        #     'embeddings_initializer': 'uniform',
        #     'embeddings_regularizer': None,
        #     'embeddings_constraint': None,
        #     'mask_zero': False,
        #     'weights': None,
        #     'lora_rank': None,
        #     'color':ft.colors.BLACK
        # },
        # 'Conv1D': {
        #     'filters': None,
        #     'kernel_size': None,
        #     'strides': 1,
        #     'padding': 'valid',
        #     'data_format': None,
        #     'dilation_rate': 1,
        #     'groups': 1,
        #     'activation': None,
        #     'use_bias': True,
        #     'kernel_initializer': 'glorot_uniform',
        #     'bias_initializer': 'zeros',
        #     'kernel_regularizer': None,
        #     'bias_regularizer': None,
        #     'activity_regularizer': None,
        #     'kernel_constraint': None,
        #     'bias_constraint': None,
        #     'color':ft.colors.GREEN
        # },
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
            'bias_initializer': ['zeros', 'DropDown', ['None', 'zeros'], 'DETAL', 'バイアスの初期化方法を指定します。'],
            'kernel_regularizer': ['None', 'DropDown', ['None', 'L1L2(l1=1e-4, l2=1e-4)', 'L1(1e-4)', 'L2(1e-4)'], 'DETAIL', 'カーネルに対する正則化を指定します。'],
            'bias_regularizer': ['None', 'DropDown', ['None', 'L1L2(l1=1e-4, l2=1e-4)', 'L1(1e-4)', 'L2(1e-4)'], 'DETAIL', 'バイアスに対する正則化を指定します。'],
            'activity_regularizer': ['None', 'DropDown', ['None', 'L1L2(l1=1e-4, l2=1e-4)', 'L1(1e-4)', 'L2(1e-4)'], 'DETAIL', '出力に対する正則化を指定します。'],
            'kernel_constraint': ['None', 'DropDown', ['None', 'max_norm(2.)'], 'DETAIL', 'カーネルに対する制約を指定します。'],
            'bias_constraint': ['None', 'DropDown', ['None'], 'DETAIL', 'バイアスに対する制約を指定します。'],
            'color':ft.colors.GREEN_100,
            'detail_view':'False',
            'description':'2次元の畳み込み操作を行い、フィルタを使って入力画像から特徴マップを抽出するためのレイヤーです。'

        },
        # 'Conv3D': {
        #     'filters': None,
        #     'kernel_size': None,
        #     'strides': (1, 1, 1),
        #     'padding': 'valid',
        #     'data_format': None,
        #     'dilation_rate': (1, 1, 1),
        #     'groups': 1,
        #     'activation': None,
        #     'use_bias': True,
        #     'kernel_initializer': 'glorot_uniform',
        #     'bias_initializer': 'zeros',
        #     'kernel_regularizer': None,
        #     'bias_regularizer': None,
        #     'activity_regularizer': None,
        #     'kernel_constraint': None,
        #     'bias_constraint': None,
        #     'color':ft.colors.GREEN_200
        # },
        # 'MaxPooling1D': {
        #     'pool_size': 2,
        #     'strides': None,
        #     'padding': 'valid',
        #     'data_format': None,
        #     'name': None,
        #     'color':ft.colors.BLUE
        # },
        'MaxPooling2D': {
            'pool_size': [(2, 2), 'TextField', 2, 'MAIN', 'プーリング窓のサイズを指定します。'],
            'strides': [(1, 1), 'TextField', 2, 'MAIN', 'ストライドのサイズを指定します。'],
            'padding': ['valid', 'DropDown', ['valid', 'same'], 'MAIN', 'パディングの方法を指定します。'],
            'data_format': ['channels_last', 'DropDown', ['channels_first', 'channels_last'], 'DETAIL', 'データのフォーマットを指定します。'],
            'name': ['None', 'DropDown', ['None'], 'DETAIL', 'このレイヤーの名前を指定します。'],
            'color':ft.colors.BLUE_100,
            'detail_view':'False',
            'description':'2次元の入力データに対して最大値プーリング操作を行い、空間的なサイズを縮小するためのレイヤーです。'
        },
        # 'MaxPooling3D': {
        #     'pool_size': (2, 2, 2),
        #     'strides': None,
        #     'padding': 'valid',
        #     'data_format': None,
        #     'name': None,
        #     'color':ft.colors.BLUE_200
        # },
        # 'AveragePooling1D': {
        #     'pool_size': None,
        #     'strides': None,
        #     'padding': 'valid',
        #     'data_format': None,
        #     'name': None,
        #     'color':ft.colors.BLUE_GREY
        # },
        'AveragePooling2D': {
            'pool_size': [(2, 2), 'TextField', 2, 'MAIN', 'プーリング窓のサイズを指定します。'],
            'strides': [(1, 1), 'TextField', 2, 'MAIN', 'ストライドのサイズを指定します。'],
            'padding': ['valid', 'DropDown', ['valid', 'same'], 'MAIN', 'パディングの方法を指定します。'],
            'data_format': ['channels_last', 'DropDown', ['channels_first', 'channels_last'], 'DETAIL', 'データのフォーマットを指定します。'],
            'name': ['None', 'DropDown', ['None'], 'DETAIL', 'このレイヤーの名前を指定します。'],
            'color':ft.colors.BLUE_GREY_100,
            'detail_view':'False',
            'description':'2次元の入力データに対して平均値プーリング操作を行い、空間的なサイズを縮小するためのレイヤーです。'
        },
        # 'AveragePooling3D': {
        #     'pool_size': None,
        #     'strides': None,
        #     'padding': 'valid',
        #     'data_format': None,
        #     'name': None,
        #     'color':ft.colors.BLUE_GREY_200
        # },
        # 'GlobalMaxPooling1D': {
        #     'data_format': None,
        #     'keepdims': False,
        #     'color':ft.colors.BLUE_ACCENT
        # },
        'GlobalMaxPooling2D': {
            'data_format': ['channels_last', 'DropDown', ['channels_first', 'channels_last'], 'DETAIL', 'データのフォーマットを指定します。'],
            'keepdims': ['False', 'DropDown', ['False', 'True'], 'DETAIL', '次元を保持するかどうかを指定します。'],
            'color':ft.colors.BLUE_ACCENT_100,
            'detail_view':'False',
            'description':'入力の全空間領域で最大値を取ることで、2次元の特徴マップを1次元の特徴ベクトルに変換するためのレイヤーです。'
        },
        # 'GlobalMaxPooling3D': {
        #     'data_format': None,
        #     'keepdims': False,
        #     'color':ft.colors.BLUE_ACCENT_200
        # },
        # 'GlobalAveragePooling1D': {
        #     'data_format': None,
        #     'keepdims': False,
        #     'color':ft.colors.BLUE_500
        # },
        'GlobalAveragePooling2D': {
            'data_format': ['channels_last', 'DropDown', ['channels_first', 'channels_last'], 'DETAIL', 'データのフォーマットを指定します。'],
            'keepdims': ['False', 'DropDown', ['False', 'True'], 'DETAIL', '次元を保持するかどうかを指定します。'],
            'color':ft.colors.BLUE_600,
            'detail_view':'False',
            'description':'入力の全空間領域で平均値を取ることで、2次元の特徴マップを1次元の特徴ベクトルに変換するためのレイヤーです。'
        },
        # 'GlobalAveragePooling3D': {
        #     'data_format': None,
        #     'keepdims': False,
        #     'color':ft.colors.BLUE_700
        # },
        'LSTM': {
            'units': ['None', 'TextField', 1, 'MAIN', ''],
            'recurrent_activation': 'sigmoid',
            'use_bias': ['True', 'DropDown', ['True',  'False'], 'DETAIL', ''],
            'kernel_initializer': ['glorot_uniform', 'DropDown', ['None', 'ones', 'he_normal', 'truncated_normal', 'random_normal'], 'DETAIL', 'カーネルの初期化方法を指定します。'],
            'recurrent_initializer': ['orthogonal', 'DropDown', ['RandomNormal', 'RandomUniform', 'glorot_normal', 'glorot_uniform', 'he_normal', 'he_uniform', 'lecun_normal', 'lecun_uniform', 'Orthogonal', 'Identity', 'Zeros', 'Ones'], 'DETAIL', 'リカレントカーネルの初期化方法を指定します。'],
            'bias_initializer': ['zeros', 'DropDown', ['None', 'zeros'], 'DETAL', 'バイアスの初期化方法を指定します。'],
            'unit_forget_bias': ['True', 'DropDown', ['True', 'False'], 'DETAIL', 'LSTMセルの忘却ゲートのバイアス項に関する設定をします。'],
            'kernel_regularizer': ['None', 'DropDown', ['None', 'L1L2(l1=1e-4, l2=1e-4)', 'L1(1e-4)', 'L2(1e-4)'], 'DETAIL', 'カーネルに対する正則化を指定します。'],
            'recurrent_regularizer': ['None', 'DropDown', ['None', 'L1L2(l1=1e-4, l2=1e-4)', 'L1(1e-4)', 'L2(1e-4)'], 'DETAIL', 'リカレントカーネルに対して正則化を適用します。'],
            'bias_regularizer': ['None', 'DropDown', ['None', 'L1L2(l1=1e-4, l2=1e-4)', 'L1(1e-4)', 'L2(1e-4)'], 'DETAIL', 'バイアス項に対して正則化を適用します。'],
            'activity_regularizer': ['None', 'DropDown', ['None', 'L1L2(l1=1e-4, l2=1e-4)', 'L1(1e-4)', 'L2(1e-4)'], 'DETAIL', 'レイヤーの出力に対して正則化を適用します。'],
            'kernel_constraint': ['None', 'DropDown', ['None', 'MaxNorm(max_value=2, axis=0)', 'NonNeg()', 'UnitNorm(axis=0)', 'MinMaxNorm(min_value=0.0, max_value=1.0, rate=1.0, axis=0)'], 'DETAIL', 'カーネル（入力に対する重み行列）に対して制約を適用します。'],
            'recurrent_constraint': ['None', 'DropDown', ['None', 'MaxNorm(max_value=2, axis=0)', 'NonNeg()', 'UnitNorm(axis=0)', 'MinMaxNorm(min_value=0.0, max_value=1.0, rate=1.0, axis=0)'], 'DETAIL', 'リカレントカーネル（隠れ状態に対する重み行列）に対して制約を適用するためのものです。'],
            'bias_constraint': ['None', 'DropDown', ['None', 'MaxNorm(max_value=2, axis=0)', 'NonNeg()', 'UnitNorm(axis=0)', 'MinMaxNorm(min_value=0.0, max_value=1.0, rate=1.0, axis=0)'], 'DETAIL', 'バイアス項に対して制約を適用します。'],
            'dropout': [0.0, 'TextField', 1, 'DETAIL', '入力に対してドロップアウト正則化を適用します。'],
            'recurrent_dropout': [0.0, 'TextField', 1, 'DETAIL', 'LSTMレイヤーにおいてリカレントステートがドロップアウトされる確率を指定します。'],
            'seed': ['None', 'TextField', 1, 'DETAIL', 'ドロップアウトおよびリカレントドロップアウトに関するランダム性の再現性を確保します。'],
            'return_sequences': ['False', 'DropDown', ['True', 'False'], 'DETAIL', 'LSTMレイヤーが出力するシーケンスの形状を制御します。'],
            'return_state': ['False', 'DropDown', ['True', 'False'], 'MAIN', 'LSTMレイヤーがリカレント状態（隠れ状態とセル状態）も出力するかどうかを制御します。'],
            'go_backwards': ['False', 'DropDown', ['True', 'False'], 'DETAIL', 'LSTMレイヤーがシーケンスを逆順に処理するかどうかを指定します。'],
            'stateful': ['False', 'DropDown', ['True', 'False'], 'MAIN', 'LSTMレイヤーが状態をシーケンス間で保持するかどうかを制御します。通常、LSTMレイヤーはバッチごとに状態をリセットしますが、stateful=Trueに設定することで、シーケンスの状態をバッチ間で保持し、連続的なシーケンスを処理する際に役立ちます。'],
            'unroll': ['False', 'DropDown', ['True', 'False'], 'DETAIL', 'LSTMレイヤーの計算を展開（アンロール）するかどうかを制御します。これにより、計算の効率を改善することができますが、メモリ使用量が増加することがあります。'],
            'use_cudnn': ['auto', 'DropDown', ['None', 'True', 'False'], 'DETAIL', 'LSTMレイヤーがGPUのCuDNN（CUDA Deep Neural Network library）最適化を使用するかどうかを指定します。'],
            'color':ft.colors.DEEP_ORANGE,
            'detail_view':'False',
            'description':"リカレントニューラルネットワーク（RNN）の一種で、時系列データやシーケンスデータの処理に特化しています。"
        },
        # 'GRU': {
        #     'units': None,
        #     'activation': 'tanh',
        #     'recurrent_activation': 'sigmoid',
        #     'use_bias': True,
        #     'kernel_initializer': 'glorot_uniform',
        #     'recurrent_initializer': 'orthogonal',
        #     'bias_initializer': 'zeros',
        #     'kernel_regularizer': None,
        #     'recurrent_regularizer': None,
        #     'bias_regularizer': None,
        #     'activity_regularizer': None,
        #     'kernel_constraint': None,
        #     'recurrent_constraint': None,
        #     'bias_constraint': None,
        #     'dropout': 0.0,
        #     'recurrent_dropout': 0.0,
        #     'seed': None,
        #     'return_sequences': False,
        #     'return_state': False,
        #     'go_backwards': False,
        #     'stateful': False,
        #     'unroll': False,
        #     'reset_after': True,
        #     'use_cudnn': 'auto',
        #     'color':ft.colors.INDIGO
        # },
        # 'SimpleRNN': {
        #     'units': None,
        #     'activation': 'tanh',
        #     'use_bias': True,
        #     'kernel_initializer': 'glorot_uniform',
        #     'recurrent_initializer': 'orthogonal',
        #     'bias_initializer': 'zeros',
        #     'kernel_regularizer': None,
        #     'recurrent_regularizer': None,
        #     'bias_regularizer': None,
        #     'activity_regularizer': None,
        #     'kernel_constraint': None,
        #     'recurrent_constraint': None,
        #     'bias_constraint': None,
        #     'dropout': 0.0,
        #     'recurrent_dropout': 0.0,
        #     'return_sequences': False,
        #     'return_state': False,
        #     'go_backwards': False,
        #     'stateful': False,
        #     'unroll': False,
        #     'seed': None,
        #     'color':ft.colors.LIME
        # },
        # 'Bidirectional': {
        #     'layer': None,
        #     'merge_mode': 'concat',
        #     'weights': None,
        #     'backward_layer': None,
        #     'color':ft.colors.RED
        # },
        # 'ConvLSTM1D': {
        #     'filters': None,
        #     'kernel_size': None,
        #     'strides': 1,
        #     'padding': 'valid',
        #     'data_format': None,
        #     'dilation_rate': 1,
        #     'activation': 'tanh',
        #     'recurrent_activation': 'sigmoid',
        #     'use_bias': True,
        #     'kernel_initializer': 'glorot_uniform',
        #     'recurrent_initializer': 'orthogonal',
        #     'bias_initializer': 'zeros',
        #     'unit_forget_bias': True,
        #     'kernel_regularizer': None,
        #     'recurrent_regularizer': None,
        #     'bias_regularizer': None,
        #     'activity_regularizer': None,
        #     'kernel_constraint': None,
        #     'recurrent_constraint': None,
        #     'bias_constraint': None,
        #     'dropout': 0.0,
        #     'recurrent_dropout': 0.0,
        #     'seed': None,
        #     'return_sequences': False,
        #     'return_state': False,
        #     'go_backwards': False,
        #     'stateful': False,
        #     'color':ft.colors.ORANGE
        # },
        # 'ConvLSTM2D': {
        #     'filters': None,
        #     'kernel_size': None,
        #     'strides': 1,
        #     'padding': 'valid',
        #     'data_format': None,
        #     'dilation_rate': 1,
        #     'activation': 'tanh',
        #     'recurrent_activation': 'sigmoid',
        #     'use_bias': True,
        #     'kernel_initializer': 'glorot_uniform',
        #     'recurrent_initializer': 'orthogonal',
        #     'bias_initializer': 'zeros',
        #     'unit_forget_bias': True,
        #     'kernel_regularizer': None,
        #     'recurrent_regularizer': None,
        #     'bias_regularizer': None,
        #     'activity_regularizer': None,
        #     'kernel_constraint': None,
        #     'recurrent_constraint': None,
        #     'bias_constraint': None,
        #     'dropout': 0.0,
        #     'recurrent_dropout': 0.0,
        #     'seed': None,
        #     'return_sequences': False,
        #     'return_state': False,
        #     'go_backwards': False,
        #     'stateful': False,
        #     'color':ft.colors.BROWN
        # },
        # 'ConvLSTM3D': {
        #     'filters': None,
        #     'kernel_size': None,
        #     'strides': 1,
        #     'padding': 'valid',
        #     'data_format': None,
        #     'dilation_rate': 1,
        #     'activation': 'tanh',
        #     'recurrent_activation': 'sigmoid',
        #     'use_bias': True,
        #     'kernel_initializer': 'glorot_uniform',
        #     'recurrent_initializer': 'orthogonal',
        #     'bias_initializer': 'zeros',
        #     'unit_forget_bias': True,
        #     'kernel_regularizer': None,
        #     'recurrent_regularizer': None,
        #     'bias_regularizer': None,
        #     'activity_regularizer': None,
        #     'kernel_constraint': None,
        #     'recurrent_constraint': None,
        #     'bias_constraint': None,
        #     'dropout': 0.0,
        #     'recurrent_dropout': 0.0,
        #     'seed': None,
        #     'return_sequences': False,
        #     'return_state': False,
        #     'go_backwards': False,
        #     'stateful': False,
        #     'color':ft.colors.ON_SURFACE
        # },
        # 'RNN': {
        #     'cell': None,
        #     'return_sequences': False,
        #     'return_state': False,
        #     'go_backwards': False,
        #     'stateful': False,
        #     'unroll': False,
        #     'zero_output_for_mask': False,
        #     'color':ft.colors.PINK
        # },
        'BatchNormalization': {
            'axis': [-1, 'TextField', 1, 'DETAIL', '正規化を行う軸を指定します。'],
            'momentum': [0.99, 'TextField', 1, 'DETAIL', '移動平均のモメンタムを指定します。'],
            'epsilon': [0.001, 'TextField', 1, 'DETAIL', '分母に追加される小さな定数を指定します。'],
            'center': ['True', 'DropDown', ['True', 'False'], 'DETAIL', 'バイアス項を追加するかどうかを指定します。'],
            'scale': ['True', 'DropDown', ['True', 'False'], 'DETAIL', 'スケーリングを行うかどうかを指定します。'],
            'beta_initializer': ['zeros', 'DropDown', ['zeros'], 'DETAIL', 'バイアスの初期化方法を指定します。'],
            'gamma_initializer': ['ones', 'DropDown', ['ones'], 'DETAIL', 'スケーリング係数の初期化方法を指定します。'],
            'moving_mean_initializer': ['zeros', 'DropDown', ['zeros'], 'DETAIL', '移動平均の初期化方法を指定します。'],
            'moving_variance_initializer': ['ones', 'DropDown', ['ones'], 'DETAIL', '移動分散の初期化方法を指定します。'],
            'beta_regularizer': ['None', 'DropDown', ['None', 'L1L2(l1=1e-4, l2=1e-4)', 'L1(1e-4)', 'L2(1e-4)'], 'DETAIL', 'バイアスの正則化を指定します。'],
            'gamma_regularizer': ['None', 'DropDown', ['None', 'L1L2(l1=1e-4, l2=1e-4)', 'L1(1e-4)', 'L2(1e-4)'], 'DETAIL', 'スケーリング係数の正則化を指定します。'],
            'beta_constraint': ['None', 'DropDown', ['None', 'MaxNorm(max_value=2, axis=0)', 'NonNeg()', 'UnitNorm(axis=0), MinMaxNorm(min_value=0.5, max_value=2.0, rate=1.0, axis=0)', 'DETAIL', 'バイアスの制約を指定します。']],
            'gamma_constraint': ['None', 'DropDown', ['None', 'MaxNorm(max_value=2, axis=0)', 'NonNeg()', 'UnitNorm(axis=0), MinMaxNorm(min_value=0.5, max_value=2.0, rate=1.0, axis=0)', 'DETAIL', 'スケーリング係数の制約を指定します。']],
            'synchronized': ['False', 'DropDown', ['False', 'True'], 'DETAIL', 'バッチ正規化の同期を有効にするかどうかを指定します。'],
            'color':ft.colors.GREY_600,
            'detail_view':'False',
            'description':'ミニバッチごとに入力データを正規化して、学習の安定化と加速を図るためのレイヤーです。'
        },
        'LayerNormalization': {
            'axis': [-1, 'TextField', 1, 'DETAIL', '正規化を行う軸を指定します。'],
            'epsilon': [0.001, 'TextField', 1, 'DETAIL', '分母に追加される小さな定数を指定します。'],
            'center': ['True', 'DropDown', ['True', 'False'], 'DETAIL', 'バイアス項を追加するかどうかを指定します。'],
            'scale': ['True', 'DropDown', ['True', 'False'], 'DETAIL', 'スケーリングを行うかどうかを指定します。'],
            'rms_scaling': ['True', 'DropDown', ['True', 'False'], 'DETAIL', 'RMSスケーリングを行うかどうかを指定します。'],
            'beta_initializer': ['zeros', 'DropDown', ['zeros'], 'DETAIL', 'バイアスの初期化方法を指定します。'],
            'gamma_initializer': ['ones', 'DropDown', ['ones'], 'DETAIL', 'スケーリング係数の初期化方法を指定します。'],
            'beta_regularizer': ['None', 'DropDown', ['None', 'L1L2(l1=1e-4, l2=1e-4)', 'L1(1e-4)', 'L2(1e-4)'], 'DETAIL', 'バイアスに適用する正則化を指定します。'],
            'gamma_regularizer': ['None', 'DropDown', ['None', 'L1L2(l1=1e-4, l2=1e-4)', 'L1(1e-4)', 'L2(1e-4)'], 'DETAIL', 'スケーリング係数に適用する正則化を指定します。'],
            'beta_constraint': ['None', 'DropDown', ['None', 'MaxNorm(max_value=2, axis=0)', 'NonNeg()', 'UnitNorm(axis=0), MinMaxNorm(min_value=0.5, max_value=2.0, rate=1.0, axis=0)', 'DETAIL', 'バイアスに適用する制約を指定します。']],
            'gamma_constraint': ['None', 'DropDown', ['None', 'MaxNorm(max_value=2, axis=0)', 'NonNeg()', 'UnitNorm(axis=0), MinMaxNorm(min_value=0.5, max_value=2.0, rate=1.0, axis=0)', 'DETAIL', 'スケーリング係数に適用する制約を指定します。']],
            'color':ft.colors.PURPLE,
            'detail_view':'False',
            'description':'各入力サンプルごとに特徴を正規化して、学習の安定化と加速を図るためのレイヤーです。'
        },
        'Dropout': {
            'rate': [0, 'TextField', 1, 'MAIN', 'ドロップアウト率を指定します。0から1の間の浮動小数点数。'],
            'noise_shape': ['None', 'DropDown', ['None'], 'DETAIL', '入力のどの要素がドロップアウトされるかを指定します。'],
            'seed': ['None', 'TextField', 1, 'DETAIL', 'ランダムシードを指定します。'],
            'color':ft.colors.BLACK,
            'detail_view':'False',
            'description':'過学習を防ぐために、学習時にランダムに一部のノードを無効にする正則化手法です。'
        },
        # 'SpatialDropout1D': {
        #     'rate': None,
        #     'seed': None,
        #     'name': None,
        #     'dtype': None,
        #     'color':ft.colors.CYAN
        # },
        'SpatialDropout2D': {
            'rate': [0, 'TextField', 1, 'MAIN', 'ドロップアウトする率を指定します。'],
            'data_format': ['channels_last', 'DropDown', ['channels_first', 'channels_last'], 'DETAIL', '入力のデータフォーマットを指定します。'],
            'seed': ['None', 'TextField', 1, 'DETAIL', 'ランダムシードを指定します。'],
            'name': ['None', 'DropDown', ['None'], 'DETAIL', 'レイヤーの名前を指定します。'],
            'dtype': ['None', 'DropDown', ['None', 'float32', 'int32'], 'DETAIL', 'レイヤーのデータ型を指定します。'],
            'color':ft.colors.CYAN,
            'detail_view':'False',
            'description':'2次元の空間データに対して、特定のフィルタ全体をランダムに無効にすることで、畳み込みニューラルネットワークの過学習を防ぐための正則化手法です。'
        },
        # 'SpatialDropout3D': {
        #     'rate': None,
        #     'data_format': None,
        #     'seed': None,
        #     'name': None,
        #     'dtype': None,
        #     'color':ft.colors.CYAN
        # },
        # 'MultiHeadAttention': {
        #     'num_heads': None,
        #     'key_dim': None,
        #     'value_dim': None,
        #     'dropout': 0.0,
        #     'use_bias': True,
        #     'output_shape': None,
        #     'attention_axes': None,
        #     'kernel_initializer': 'glorot_uniform',
        #     'bias_initializer': 'zeros',
        #     'kernel_regularizer': None,
        #     'bias_regularizer': None,
        #     'activity_regularizer': None,
        #     'kernel_constraint': None,
        #     'bias_constraint': None,
        #     'color':ft.colors.CYAN
        # },
        # 'Attention': {
        #     'use_scale': False,
        #     'score_mode': 'dot',
        #     'dropout': 0.0,
        #     'seed': None,
        #     'color':ft.colors.CYAN
        # },
        # 'Reshape': {
        #     'target_shape': None,
        #     'color':ft.colors.CYAN
        # },
        'Flatten': {
            'data_format': ['channels_last', 'DropDown', ['channels_first', 'channels_last'], 'DETAIL', 'データのフォーマットを指定します。'],
            'color':ft.colors.CYAN,
            'detail_view':'False',
            'description':'入力の多次元データを1次元のベクトルに変換するためのレイヤーです。'
        },

    }

preprocess_dicts = {
        'ImageDataGenerator': {
                'featurewise_center': ['False', 'DropDown', ['True', 'False'], 'DETAIL', 'データセット全体の中心化を行うかどうかを指定します。', 'None'],
                'samplewise_center': ['False', 'DropDown', ['True', 'False'], 'DETAIL', '各サンプルの中心化を行うかどうかを指定します。', 'None'],
                'featurewise_std_normalization': ['False', 'DropDown', ['True', 'False'], 'DETAIL', 'データセット全体の標準偏差で正規化するかどうかを指定します。', 'None'],
                'samplewise_std_normalization': ['False', 'DropDown', ['True', 'False'], 'DETAIL', '各サンプルの標準偏差で正規化するかどうかを指定します。', 'None'],
                'zca_whitening': ['False', 'DropDown', ['True', 'False'], 'DETAIL', 'ZCA白色化を適用するかどうかを指定します。', 'packages/data_expansion_video/zca_whitening.mp4'],
                'zca_epsilon': [1e-06, 'TextField', 1, 'DETAIL', 'ZCA白色化のためのイプシロンを指定します。', 'packages/data_expansion_video/zca_whitening.mp4'],
                'rotation_range': [0, 'TextField', 1, 'DETAIL', 'ランダム回転の範囲を度単位で指定します。', 'packages/data_expansion_video/rotation_range.mp4'],
                'width_shift_range': [0.0, 'TextField', 1, 'DETAIL', 'ランダム水平シフトの範囲を指定します。', 'packages/data_expansion_video/width_shift_range.mp4'],
                'height_shift_range': [0.0, 'TextField', 1, 'DETAIL', 'ランダム垂直シフトの範囲を指定します。', 'packages/data_expansion_video/height_shift_range.mp4'],
                'brightness_range': [(0.0, 10.0), 'TextField', 2, 'DETAIL', 'ランダム明度シフトの範囲を指定します。', 'packages/data_expansion_video/brightness_range.mp4'],
                'shear_range': [0.0, 'TextField', 1, 'DETAIL', 'ランダムせん断の範囲を指定します。', 'packages/data_expansion_video/shear_range.mp4'],
                'zoom_range': [0.0, 'TextField', 1, 'DETAIL', 'ランダムズームの範囲を指定します。', 'packages/data_expansion_video/zoom_range.mp4'],
                'channel_shift_range': [0, 'TextField', 1, 'DETAIL', 'ランダムチャネルシフトの範囲を指定します。', 'packages/data_expansion_video/channel_shift_range.mp4'],
                'fill_mode': ['nearest', 'DropDown', ['reflect', 'nearest'], 'DETAIL', '境界の埋め方を指定します。', 'None'],
                'cval': [0.0, 'TextField', 1, 'DETAIL', '境界外のピクセルに使用する値を指定します。', 'None'],
                'horizontal_flip': ['False', 'DropDown', ['True', 'False'], 'DETAIL', 'ランダムに水平反転を行うかどうかを指定します。', 'packages/data_expansion_video/horizontal_flip.mp4'],
                'vertical_flip': ['False', 'DropDown', ['True', 'False'], 'DETAIL', 'ランダムに垂直反転を行うかどうかを指定します。', 'packages/data_expansion_video/vertical_flip.mp4'],
                'rescale': [1./255, 'DropDown', [1./255], 'MAIN', '再スケーリング係数を指定します。', 'None'],
                'data_format': ['channels_last', 'DropDown', ['channels_first', 'channels_last'], 'DETAIL', 'データのフォーマットを指定します。', 'None'],
                'interpolation_order': [1, 'DropDown', [0, 1, 2, 3], 'DETAIL', '補間の順序を指定します。', 'None'],
                'dtype': ['None', 'DropDown', ['None', 'float32', 'float64', 'uint8'], 'MAIN', 'データ型を指定します。', 'None']
            },
            'flow_from_directory': {
                'target_size': [(256, 256), 'TextField', 2, 'MAIN', 'ターゲットサイズ（高さ、幅）を指定します。', 'None'],
                'color_mode': ['rgb', 'DropDown', ['rgb', 'grayscale'], 'MAIN', 'カラーモードを指定します。', 'None'],
                'class_mode': ['categorical', 'DropDown', ['categorical', 'binary', 'sparse', 'input', 'none'], 'MAIN', 'ラベルの種類を指定します。', 'None'],
                'batch_size': [32, 'TextField', 1, 'MAIN', 'バッチサイズを指定します。', 'None'],
                'shuffle': ['False', 'DropDown', ['True', 'False'], 'MAIN', 'シャッフルするかどうかを指定します。', 'None'],
                'seed': ['None', 'TextField', 1, 'DETAIL', '乱数シードを指定します。', 'None'],
                'interpolation': ['nearest', 'DropDown', ['nearest', 'bilinear', 'bicubic', 'lanczos', 'box', 'hamming', 'UNK'], 'DETAIL', '補間方法を指定します。', 'None']
            }
    }


compile_dicts = {
        "select_optimizer":['None', 'DropDown', ['None','Adam'], 'MAIN', 'UNK'],
        'optimizer':{
            'None':{'detail_view':'False'},
            'Adam':{
                'learning_rate':[0.001, 'TextField', 1, 'DETAIL', '学習率を指定します。'],
                'beta_1':[0.9, 'TextField', 1, 'DETAIL', '1番目のモーメント推定の減衰率を指定します。'],
                'beta_2':[0.999, 'TextField', 1, 'DETAIL', '2番目のモーメント推定の減衰率を指定します。'],
                'epsilon':[1e-07, 'TextField', 1, 'DETAIL', '数値安定性のための小さな定数を指定します。'],
                'decay':['None', 'TextField', 1, 'DETAIL', '学習率の減衰を指定します。'],
                'clipnorm':['None', 'TextField', 1, 'DETAIL', '勾配ノルムクリッピングを指定します。'],
                'clipvalue':['None', 'TextField', 1, 'DETAIL', '勾配値クリッピングを指定します。'],
                'global_clipnorm':['None', 'TextField', 1, 'DETAIL', 'グローバル勾配ノルムクリッピングを指定します。'],
                'detail_view':'False'
            }
        },
        'loss':['None', 'DropDown', ['None', 'categorical_crossentropy', 'binary_crossentropy'], 'MAIN', '損失関数を指定します。'],
        'metrics':['None', 'DropDown', ['None', 'acc'], 'MAIN', '評価指標を指定します。'],
    }

ML_dicts = {
    'DecisionTreeClassifier':{'max_depth':['None', 'TextField', 1, 'MAIN', '木の深さを指定します。', 'packages/alg_param_video/max_depth.mp4'],
                              'min_samples_split':[2, 'TextField', 1, 'DETAIL', 'UNK', 'None'],
                              'min_samples_leaf':[1, 'TextField', 1, 'DETAIL', 'UNK', 'None'],
                              },
    'DecisionTreeRegressor':{'max_depth':['None', 'TextField', 1, 'MAIN', '木の深さを指定します。', 'None'],
                             'min_samples_split':[2, 'TextField', 1, 'DETAIL', 'UNK', 'None'],
                             'min_samples_leaf':[1, 'TextField', 1, 'DETAIL', 'UNK', 'None'],
                             },
    'LogisticRegression':{'penalty':['l2', 'DropDown', ['None', 'l1', 'l2', 'elasticnet'], 'DETAIL', 'UNK', 'None']},
    'RandomForestClassifier':{'n_estimators':[100, 'TextField', 1, 'DETAIL', 'UNK', 'None'],
                              'max_depth':['None', 'TextField', 1, 'MAIN', '木の深さを指定します。', 'None']},
    'RandomForestRegressor':{'n_estimators':[100, 'TextField', 1, 'DETAIL', 'UNK', 'None'],
                              'max_depth':['None', 'TextField', 1, 'MAIN', '木の深さを指定します。', 'None']},
    'SVC':{'kernel':['rbf', 'DropDown', ['linear', 'poly', 'rbf', 'sigmoid', 'precomputed'], 'DETAIL', 'UNK', 'None'],
           'probability':['True', 'DropDown', ['True'], 'MAIN', 'UNK', 'None']},
    'SVR':{'kernel':['rbf', 'DropDown', ['linear', 'poly', 'rbf', 'sigmoid', 'precomputed'], 'DETAIL', 'UNK', 'None']},
}

ML_display_dicts = {
    'ニューラルネットワーク':{
        'regression':'True',
        'categorical':'True',
        'alg':'NN',
        'image':'None',
        "check":False, 
        "index":0,
        'path':'packages/alg_image/NN.png'
    },
    '決定木':{
        'regression':'False',
        'categorical':'True',
        'alg':'DecisionTreeClassifier',
        'image':'None',
        "check":False, 
        "index":1,
        'path':'packages/alg_image/tree.png'
    },
    '回帰木':{
        'regression':'True',
        'categorical':'False',
        'alg':'DecisionTreeRegressor',
        'image':'None',
        "check":False, 
        "index":2,
        'path':'packages/alg_image/tree.png'
    },
    'ロジスティック回帰':{
        'regression':'False',
        'categorical':'True',
        'alg':'LogisticRegression',
        'image':'None',
        "check":False, 
        "index":3,
        'path':'packages/alg_image/logistic.png'
    },
    'ランダムフォレスト分類':{
        'regression':'False',
        'categorical':'True',
        'alg':'RandomForestClassifier',
        'image':'None',
        "check":False, 
        "index":4,
        'path':'packages/alg_image/randomforest.png'
    },
    'ランダムフォレスト回帰':{
        'regression':'True',
        'categorical':'False',
        'alg':'RandomForestRegressor',
        'image':'None',
        "check":False, 
        "index":5,
        'path':'packages/alg_image/randomforest.png'
    },
    'サポートベクターマシン分類':{
        'regression':'False',
        'categorical':'True',
        'alg':'SVC',
        'image':'None',
        "check":False, 
        "index":6,
        'path':'packages/alg_image/SVM.png'
    },
    'サポートベクターマシン回帰':{
        'regression':'True',
        'categorical':'False',
        'alg':'SVR',
        'image':'None',
        "check":False, 
        "index":7,
        'path':'packages/alg_image/SVM.png'
    }

 
}
