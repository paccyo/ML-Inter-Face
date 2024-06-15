import model_info
from keras.utils import plot_model
import sys


_, project_path = sys.argv[0], sys.argv[1]
model = model_info.model_build(project_path)
plot_model(model, show_shapes=True, expand_nested=True, to_file=f'{project_path}/model.png')
