
import glob
import os
import shutil


class DatasetInfo:
    """
    データセット作成
    """
    def send(self, dicts, dataset_path):
        """
        dicts->str: 辞書
        dataset_path->str: データセットpath
        """
        self.banana(dicts, dataset_path)

    def delete_dir(self):
        """
        ディレクトリ削除
        """
        try:
            shutil.rmtree('dataset')
        except FileNotFoundError:
            pass

    def generate_dir(self, label, part):
        """
        ディレクトリ作成
        """
        if part[0] != 0:
            os.makedirs(f'dataset/train/{label}', exist_ok=True)
        if part[1] != 0:
            os.makedirs(f'dataset/validation/{label}', exist_ok=True)
        if part[2] != 0:
            os.makedirs(f'dataset/test/{label}', exist_ok=True)

    def banana(self, dicts, dataset_path):
        self.delete_dir()
        # それぞれの画像割合
        part = [dicts['train'], dicts['validation'], dicts['test']]
        for i, label_path in enumerate(glob.glob(os.path.join(dataset_path, '*'))):
            # ラベルごとの画像枚数
            sum_n = len(glob.glob(os.path.join(label_path, '*.*')))
            # ラベル名
            label = label_path.split('\\')[-1]
            # フォルダ作成
            self.generate_dir(label, part)
            # それぞれの画像枚数
            train_n = sum_n*(part[0]/10)
            validation_n = sum_n*(part[1]/10)
            test_n = sum_n*(part[2]/10)
            # 余った画像を0ではないところへin
            if train_n != 0:
                train_n += sum_n-(train_n+validation_n+test_n)
            elif validation_n != 0:
                validation_n += sum_n-(train_n+validation_n+test_n)
            else:
                test_n += sum_n-(train_n+validation_n+test_n)

            # 画像を突っ込む
            for i, image_path in enumerate(glob.glob(os.path.join(label_path, '*.*'))):
                i += 1
                if i <= train_n:
                    shutil.copy(image_path, f'dataset/train/{label}/{os.path.basename(image_path)}')
                elif i <= (train_n+validation_n):
                    shutil.copy(image_path, f'dataset/validation/{label}/{os.path.basename(image_path)}')
                else:
                    shutil.copy(image_path, f'dataset/test/{label}/{os.path.basename(image_path)}')
    

# テストケース
if __name__ == '__main__':
    test_dict = {'train':6, 'validation':4, 'test':0}
    dataset_info = DatasetInfo()
    dataset_info.send(test_dict, r"C:\Users\yuuki\Documents\GUI_MLearning\GUI_MLearning-main\data3")