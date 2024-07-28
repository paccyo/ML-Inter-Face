
import glob
import os
import webbrowser


def view_DS(path):
    path = os.path.join(path, '*.html')
    print(path)
    for html_path in glob.glob(path):
        webbrowser.open(html_path)


if __name__ == '__main__':
    view_DS(r"C:\Users\yuuki\Documents\GUI_MLearning\ML-Inter-Face\test_data\test_dir\DS_result\AutoViz")