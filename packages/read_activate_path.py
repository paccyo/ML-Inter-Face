

def read_activ_path():
    """
    activateパスを返します。
    """
    with open('packages/activate_path.txt') as f:
        path = f.read()
    return path