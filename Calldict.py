import flet as ft

DROPDOWN = "DropDown"
TEXTFIELD = "TextField"

layer_dicts = {
        'Input': {
            'shape': ['None', 'DropDown', ['None'], 'UNK'],
            'batch_size': ['None', 'TextField', 1, 'UNK'],
            'dtype': ['None', 'DropDown', ['None', 'float32', 'int32'], 'UNK'],
            'sparse': ['False', 'DropDown', ['True', 'False'], 'UNK'],
            'batch_shape': ['None', 'DropDown', ['None'], 'UNK'],
            'name': ['None', 'DropDown', ['None'], 'UNK'],
            'tensor': ['None', 'DropDown', ['None'], 'UNK'],
            'color':ft.colors.GREY
        },
        
        'Dense': {
            'units': [0, 'TextField', 1, 'UNK'],
            'use_bias': ['True', 'DropDown', ['True', 'False'], 'UNK'],
            'kernel_initializer': ['glorot_uniform', 'DropDown', ['None', 'ones', 'he_normal()', 'truncated_normal()', 'random_normal'], 'UNK'],
            'bias_initializer': ['zeros', 'DropDown', ['None', 'zeros'], 'UNK'],
            'kernel_regularizer': ['None', 'DropDown', ['None', 'L1L2(l1=1e-4, l2=1e-4)', 'L1(1e-4)', 'L2(1e-4)'], 'UNK'],
            'bias_regularizer': ['None', 'DropDown', ['None', 'L1L2(l1=1e-4, l2=1e-4)', 'L1(1e-4)', 'L2(1e-4)'], 'UNK'],
            'activity_regularizer': ['None', 'DropDown', ['None', 'L1L2(l1=1e-4, l2=1e-4)', 'L1(1e-4)', 'L2(1e-4)'], 'UNK'],
            'kernel_constraint': ['None', 'DropDown', ['None', 'max_norm(2.)'], 'UNK'],
            'bias_constraint': ['None', 'DropDown', ['None'], 'UNK'],
            'lora_rank': ['None', 'DropDown', ['None'], 'UNK'],
            'color':ft.colors.AMBER
        },
        
        'Activation': {
            'activation': ['None', 'DropDown', ['None', 'relu', 'sigmoid', 'gelu', 'softmax', 'tanh'], 'UNK'],
            'color':ft.colors.YELLOW
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
            'filters': [0, 'TextField', 1, 'UNK'],
            'kernel_size': [(1, 1), 'TextField', 2, 'UNK'],
            'strides': [(1, 1), 'TextField', 2, 'UNK'],
            'padding': ['valid', 'DropDown', ['valid', 'same'], 'UNK'],
            'data_format': ['channels_last', 'DropDown', ['channels_first', 'channels_last'], 'UNK'],
            'dilation_rate': [(1, 1), 'TextField', 2, 'UNK'],
            'groups': [1, 'TextField', 1, 'UNK'],
            'use_bias': ['True', 'DropDown', ['True', 'False'], 'UNK'],
            'kernel_initializer': ['glorot_uniform', 'DropDown', ['None', 'ones', 'he_normal()', 'truncated_normal()', 'random_normal'], 'UNK'],
            'bias_initializer': ['zeros', 'DropDown', ['None', 'zeros'], 'UNK'],
            'kernel_regularizer': ['None', 'DropDown', ['None', 'L1L2(l1=1e-4, l2=1e-4)', 'L1(1e-4)', 'L2(1e-4)'], 'UNK'],
            'bias_regularizer': ['None', 'DropDown', ['None', 'L1L2(l1=1e-4, l2=1e-4)', 'L1(1e-4)', 'L2(1e-4)'], 'UNK'],
            'activity_regularizer': ['None', 'DropDown', ['None', 'L1L2(l1=1e-4, l2=1e-4)', 'L1(1e-4)', 'L2(1e-4)'], 'UNK'],
            'kernel_constraint': ['None', 'DropDown', ['None', 'max_norm(2.)'], 'UNK'],
            'bias_constraint': ['None', 'DropDown', ['None'], 'UNK'],
            'color':ft.colors.GREEN_100
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
            'pool_size': [(2, 2), 'TextField', 2, 'UNK'],
            'strides': [(1, 1), 'TextField', 2, 'UNK'],
            'padding': ['valid', 'DropDown', ['valid', 'same'], 'UNK'],
            'data_format': ['channels_last', 'DropDown', ['channels_first', 'channels_last'], 'UNK'],
            'name': ['None', 'DropDown', ['None'], 'UNK'],
            'color':ft.colors.BLUE_100
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
            'pool_size': [(2, 2), 'TextField', 2, 'UNK'],
            'strides': [(1, 1), 'TextField', 2, 'UNK'],
            'padding': ['valid', 'DropDown', ['valid', 'same'], 'UNK'],
            'data_format': ['channels_last', 'DropDown', ['channels_first', 'channels_last'], 'UNK'],
            'name': ['None', 'DropDown', ['None'], 'UNK'],
            'color':ft.colors.BLUE_GREY_100
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
            'data_format': ['channels_last', 'DropDown', ['channels_first', 'channels_last'], 'UNK'],
            'keepdims': ['False', 'DropDown', ['False', 'True'], 'UNK'],
            'color':ft.colors.BLUE_ACCENT_100
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
            'data_format': ['channels_last', 'DropDown', ['channels_first', 'channels_last'], 'UNK'],
            'keepdims': ['False', 'DropDown', ['False', 'True'], 'UNK'],
            'color':ft.colors.BLUE_600
        },
        # 'GlobalAveragePooling3D': {
        #     'data_format': None,
        #     'keepdims': False,
        #     'color':ft.colors.BLUE_700
        # },
        # 'LSTM': {
        #     'units': None,
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
        #     'unroll': False,
        #     'use_cudnn': 'auto',
        #     'color':ft.colors.DEEP_ORANGE
        # },
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
            'axis': [-1, 'TextField', 1, 'UNK'],
            'momentum': [0.99, 'TextField', 1, 'UNK'],
            'epsilon': [0.001, 'TextField', 1, 'UNK'],
            'center': ['True', 'DropDown', ['True', 'False'], 'UNK'],
            'scale': ['True', 'DropDown', ['True', 'False'], 'UNK'],
            'beta_initializer': ['zeros', 'DropDown', ['zeros'], 'UNK'],
            'gamma_initializer': ['ones', 'DropDown', ['ones'], 'UNK'],
            'moving_mean_initializer': ['zeros', 'DropDown', ['zeros'], 'UNK'],
            'moving_variance_initializer': ['ones', 'DropDown', ['ones'], 'UNK'],
            'beta_regularizer': ['None', 'DropDown', ['None', 'L1L2(l1=1e-4, l2=1e-4)', 'L1(1e-4)', 'L2(1e-4)'], 'UNK'],
            'gamma_regularizer': ['None', 'DropDown', ['None', 'L1L2(l1=1e-4, l2=1e-4)', 'L1(1e-4)', 'L2(1e-4)'], 'UNK'],
            'beta_constraint': ['None', 'DropDown', ['None', 'MaxNorm(max_value=2, axis=0)', 'NonNeg()', 'UnitNorm(axis=0), MinMaxNorm(min_value=0.5, max_value=2.0, rate=1.0, axis=0)', 'UNK']],
            'gamma_constraint': ['None', 'DropDown', ['None', 'MaxNorm(max_value=2, axis=0)', 'NonNeg()', 'UnitNorm(axis=0), MinMaxNorm(min_value=0.5, max_value=2.0, rate=1.0, axis=0)', 'UNK']],
            'synchronized': ['False', 'DropDown', ['False', 'True'], 'UNK'],
            'color':ft.colors.GREY_600
        },
        'LayerNormalization': {
            'axis': [-1, 'TextField', 1, 'UNK'],
            'epsilon': [0.001, 'TextField', 1, 'UNK'],
            'center': ['True', 'DropDown', ['True', 'False'], 'UNK'],
            'scale': ['True', 'DropDown', ['True', 'False'], 'UNK'],
            'rms_scaling': ['True', 'DropDown', ['True', 'False'], 'UNK'],
            'beta_initializer': ['zeros', 'DropDown', ['zeros'], 'UNK'],
            'gamma_initializer': ['ones', 'DropDown', ['ones'], 'UNK'],
            'beta_regularizer': ['None', 'DropDown', ['None', 'L1L2(l1=1e-4, l2=1e-4)', 'L1(1e-4)', 'L2(1e-4)'], 'UNK'],
            'gamma_regularizer': ['None', 'DropDown', ['None', 'L1L2(l1=1e-4, l2=1e-4)', 'L1(1e-4)', 'L2(1e-4)'], 'UNK'],
            'beta_constraint': ['None', 'DropDown', ['None', 'MaxNorm(max_value=2, axis=0)', 'NonNeg()', 'UnitNorm(axis=0), MinMaxNorm(min_value=0.5, max_value=2.0, rate=1.0, axis=0)', 'UNK']],
            'gamma_constraint': ['None', 'DropDown', ['None', 'MaxNorm(max_value=2, axis=0)', 'NonNeg()', 'UnitNorm(axis=0), MinMaxNorm(min_value=0.5, max_value=2.0, rate=1.0, axis=0)', 'UNK']],
            'color':ft.colors.PURPLE
        },
        'Dropout': {
            'rate': [-1, 'TextField', 1, 'UNK'],
            'noise_shape': ['None', 'DropDown', ['None'], 'UNK'],
            'seed': ['None', 'TextField', 1, 'UNK'],
            'color':ft.colors.BLACK
        },
        # 'SpatialDropout1D': {
        #     'rate': None,
        #     'seed': None,
        #     'name': None,
        #     'dtype': None,
        #     'color':ft.colors.CYAN
        # },
        'SpatialDropout2D': {
            'rate': ['None', 'TextField', 1, 'UNK'],
            'data_format': ['channels_last', 'DropDown', ['channels_first', 'channels_last'], 'UNK'],
            'seed': ['None', 'TextField', 1, 'UNK'],
            'name': ['None', 'DropDown', ['None'], 'UNK'],
            'dtype': ['None', 'DropDown', ['None', 'float32', 'int32'], 'UNK'],
            'color':ft.colors.CYAN
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
            'data_format': ['channels_last', 'DropDown', ['channels_first', 'channels_last'], 'UNK'],
            'color':ft.colors.CYAN
        },

    }

preprocess_dicts = {
        'ImageDataGenerator': {
                'featurewise_center': ['False', 'DropDown', ['True', 'False'], 'UNK'],
                'samplewise_center': ['False', 'DropDown', ['True', 'False'], 'UNK'],
                'featurewise_std_normalization': ['False', 'DropDown', ['True', 'False'], 'UNK'],
                'samplewise_std_normalization': ['False', 'DropDown', ['True', 'False'], 'UNK'],
                'zca_whitening': ['False', 'DropDown', ['True', 'False'], 'UNK'],
                'zca_epsilon': [1e-06, 'TextField', 1, 'UNK'],
                'rotation_range': [0, 'TextField', 1, 'UNK'],
                'width_shift_range': [0.0, 'TextField', 1, 'UNK'],
                'height_shift_range': [0.0, 'TextField', 1, 'UNK'],
                'brightness_range': [['None', [0.0, 1.0]], ['DropDown', 'TextField'], [['None', 'True'], 2], 'UNK'],
                'shear_range': [0.0, 'TextField', 1, 'UNK'],
                'zoom_range': [0.0, 'TextField', 1, 'UNK'],
                'channel_shift_range': [0.0, 'TextField', 1, 'UNK'],
                'fill_mode': ['nearest', 'DropDown', ['reflect', 'nearest'], 'UNK'],
                'cval': [0.0, 'TextField', 1, 'UNK'],
                'horizontal_flip': ['False', 'DropDown', ['True', 'False'], 'UNK'],
                'vertical_flip': ['False', 'DropDown', ['True', 'False'], 'UNK'],
                'rescale': ['None', 'DropDown', ['None', 1./255]],
                'data_format': ['channels_last', 'DropDown', ['channels_first', 'channels_last'], 'UNK'],
                'interpolation_order': [1, 'DropDown', [0, 1, 2, 3]],
                'dtype': ['None', 'DropDown', ['None', 'float32', 'float64', 'uint8']]
            },
            'flow_from_directory': {
                'target_size': [(256, 256), 'TextField', 2, 'UNK'],
                'color_mode': ['rgb', 'DropDown', ['rgb', 'grayscale'], 'UNK'],
                'class_mode': ['categorical', 'DropDown', ['categorical', 'binary', 'sparse', 'input', 'none'], 'UNK'],
                'batch_size': [32, 'TextField', 1, 'UNK'],
                'shuffle': ['False', 'DropDown', ['True', 'False'], 'UNK'],
                'seed': ['None', 'TextField', 1, 'UNK'],
                'save_to_dir': ['None', 'TextField', 1, 'UNK'],
                'save_prefix': ['', 'TextField', 1, 'UNK'],
                'save_format': ['png', 'DropDown', ['png', 'jpeg'], 'UNK'],
                'interpolation': ['nearest', 'DropDown', ['nearest', 'bilinear', 'bicubic', 'lanczos', 'box', 'hamming', 'UNK']]
            }
    }


compile_dicts = {
        'optimizer':{
            'Adam':{
                'learning_rate':[0.001, 'TextField', 1, 'UNK'],
                'beta_1':[0.9, 'TextField', 1, 'UNK'],
                'beta_2':[0.999, 'TextField', 1, 'UNK'],
                'epsilon':[1e-07, 'TextField', 1, 'UNK'],
                'amsgrad':['False', 'DropDown', ['True', 'False'], 'UNK'],
                'weight_decay':['None', 'TextField', 1, 'UNK'],
                'clipnorm':['None', 'TextField', 1, 'UNK'],
                'clipvalue':['None', 'TextField', 1, 'UNK'],
                'global_clipnorm':['None', 'TextField', 1, 'UNK'],
                'use_ema':['False', 'TextField', ['True', 'False'], 'UNK'],
                'ema_momentum':[0.99, 'TextField', 1, 'UNK'],
                'ema_overwrite_frequency':['None', 'TextField', 1, 'UNK'],
                'loss_scale_factor':['None', 'TextField', 1, 'UNK'],
                'gradient_accumulation_steps':['None', 'TextField', 1, 'UNK'],
                'name':['adam', 'DropDown', ['adam'], 'UNK']
            }
        },
        'loss':{
            'CategoricalCrossentropy':{
                'from_logits':['False', 'DropDown', ['False'], 'UNK'],
                'label_smoothing':[0.0, 'DropDown', [0.0], 'UNK'],
                'axis':[-1, 'DropDown', [-1], 'UNK'],
                'reduction':['sum_over_batch_size', 'DropDown', ['sum_over_batch_size'], 'UNK'],
                'name':['categorical_crossentropy', 'DropDown', ['categorical_crossentropy'], 'UNK']
            }
        },
        'metrics':{
            'Accuracy':{
                'name':['accuracy', 'DropDown', ['accuracy'], 'UNK']
            }
        }
    }
