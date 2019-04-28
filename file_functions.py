# coding:utf-8
import os


# 删除文件夹里面的文件，如果存在子文件夹，同时删除子文件夹中的文件（不会删除文件夹）
def del_filesByPath(path):
    ls = os.listdir(path)
    for i in ls:
        c_path = os.path.join(path, i)
        if os.path.isdir(c_path):
            del_filesByPath(c_path)
        else:
            os.remove(c_path)


# if __name__ == '__main__':
#     # 输入路径
#     CUR_PATH = r'D:\lw_workspace\DataCollection\D_liudan_M_A_20190425\3D'.replace("\\", "/") + "/"
#     del_file(CUR_PATH)
