
# 2024/06/04 BPS-sys ver1.0作成


class CompileInfo:
    """
    コンパイルファイル作成
    """
    def __init__(self):
        self.compiles = ''
        self.imports = ''
        self.load_import_info()

    def load_import_info(self):
        """
        モデルファイル読み込み
        """
        with open('imports_file.txt') as f:
            imports_data = f.read()
        self.imports += imports_data + '\n\n'

    def send_compile(self, compile_dict):
        """
        辞書からコンパイルを作成
        """
        # コメントはわかりやすくするための例
        for compile_option_name, compile_option_info in compile_dict.items():
            # Adam, Adamのパラメータ
            for compile_algo_name, compile_params in compile_option_info.items():
                params = ''
                # Adamのパラメータを格納
                for param_name, param_value in compile_params.items():
                    params += f'{param_name}={param_value}, '
                break
            # 不要なコンマ削除
            params = params[:-2]

            # 行の作成
            self.compiles += f'    {compile_option_name} = {compile_algo_name}({params})\n'

        self.write_compilefile()

    def write_compilefile(self):
        """
        コンパイルファイルの書き出し
        """
        with open('compile_info.py', 'w') as f:
            f.write(self.imports+'def compile_build():\n'+self.compiles+'    return optimizer, loss, metrics')

if __name__ == '__main__':
    # テストケース
    test_dict = {
        'optimizer':{
            'Adam':{
                'learning_rate':0.001,
                'beta_1':0.9,
                'beta_2':0.999,
                'epsilon':1e-07,
                'amsgrad':False,
                'weight_decay':None,
                'clipnorm':None,
                'clipvalue':None,
                'global_clipnorm':None,
                'use_ema':False,
                'ema_momentum':0.99,
                'ema_overwrite_frequency':None,
                'loss_scale_factor':None,
                'gradient_accumulation_steps':None,
                'name':"\'adam\'"
            }
        },
        'loss':{
            'CategoricalCrossentropy':{
                'from_logits':False,
                'label_smoothing':0.0,
                'axis':-1,
                'reduction':"\'sum_over_batch_size\'",
                'name':"\'categorical_crossentropy\'"
            }
        },
        'metrics':{
            'Accuracy':{
                'name':"\'accuracy\'",
                'dtype':None
            }
        }
    }

    # 実行

    compile_info = CompileInfo()
    compile_info.send_compile(test_dict)
