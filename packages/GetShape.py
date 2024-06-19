
import numpy as np

def get(image_size=(None, None), color_mode='rgb'):    
    if color_mode == 'rgb':
        color = 3
    else:
        color = 1
    return (image_size[0], image_size[1], color)

if __name__ == '__main__':
    shape_size = get(image_size=(256, 256), color_mode='rgb')
    print(shape_size)