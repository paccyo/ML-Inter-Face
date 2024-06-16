import model_info
from keras.utils import plot_model
import sys
import glob
import os


_, project_path = sys.argv[0], sys.argv[1]
model = model_info.model_build()

model_img_path = None
for model_img_path in glob.glob(f'{project_path}/model_*.png'):
    pass
if model_img_path == None:
    model_id = 0
else:
    model_id = int(os.path.splitext(os.path.basename(model_img_path))[0].split('_')[1])
    os.remove(f'{project_path}/model_{model_id-1}.png')
plot_model(model, show_shapes=True, expand_nested=True, to_file=f'{project_path}/model_{model_id}.png')
