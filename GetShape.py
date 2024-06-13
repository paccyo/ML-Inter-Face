
from PIL import Image
import numpy as np

def get(path):
    image = Image.open(path)
    array = np.array(image)
    return array.shape

if __name__ == '__main__':
    shape_size = get(r"path")
    print(shape_size)