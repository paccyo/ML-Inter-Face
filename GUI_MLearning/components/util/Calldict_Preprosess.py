
DROPDOWN = "DropDown"
TEXTFIELD = "TextField"

preprocess_dicts = {
    'ImageDataGenerator': {
            'featurewise_center': ['False', DROPDOWN, ['True', 'False'], 'UNK'],
            'samplewise_center': ['False', DROPDOWN, ['True', 'False'], 'UNK'],
            'featurewise_std_normalization': ['False', DROPDOWN, ['True', 'False'], 'UNK'],
            'samplewise_std_normalization': ['False', DROPDOWN, ['True', 'False'], 'UNK'],
            'zca_whitening': ['False', DROPDOWN, ['True', 'False'], 'UNK'],
            'zca_epsilon': [1e-06, TEXTFIELD, 1, 'UNK'],
            'rotation_range': [0, TEXTFIELD, 1, 'UNK'],
            'width_shift_range': [0.0, TEXTFIELD, 1, 'UNK'],
            'height_shift_range': [0.0, TEXTFIELD, 1, 'UNK'],
            'brightness_range': [['None', [0.0, 1.0]], [DROPDOWN, TEXTFIELD], [['None', 'True'], 2], 'UNK'],
            'shear_range': [0.0, TEXTFIELD, 1, 'UNK'],
            'zoom_range': [0.0, TEXTFIELD, 1, 'UNK'],
            'channel_shift_range': [0.0, TEXTFIELD, 1, 'UNK'],
            'fill_mode': ['nearest', DROPDOWN, ['reflect', 'nearest'], 'UNK'],
            'cval': [0.0, TEXTFIELD, 1, 'UNK'],
            'horizontal_flip': ['False', DROPDOWN, ['True', 'False'], 'UNK'],
            'vertical_flip': ['False', DROPDOWN, ['True', 'False'], 'UNK'],
            'rescale': ['None', DROPDOWN, ['None', 1./255], 'UNK'],
            'data_format': ['channels_last', DROPDOWN, ['channels_first', 'channels_last'], 'UNK'],
            'interpolation_order': [1, DROPDOWN, [0, 1, 2, 3], 'UNK'],
            'dtype': ['None', DROPDOWN, ['None', 'float32', 'float64', 'uint8'], 'UNK']
        },
        'flow_from_directory': {
            'target_size': (256, 256),
            'color_mode': 'rgb',
            'classes': None,
            'class_mode': 'categorical',
            'batch_size': 32,
            'shuffle': True,
            'seed': None,
            'save_to_dir': None,
            'save_prefix': '',
            'save_format': 'png',
            'follow_links': False,
            'subset': None,
            'interpolation': 'nearest',
            'keep_aspect_ratio': False
        }
    }