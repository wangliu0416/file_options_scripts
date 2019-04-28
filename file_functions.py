# coding:utf-8
import os
import zipfile


# 删除文件夹里面的文件，如果存在子文件夹，同时删除子文件夹中的文件（不会删除文件夹）
def del_filesByPath(path):
    ls = os.listdir(path)
    for i in ls:
        c_path = os.path.join(path, i)
        if os.path.isdir(c_path):
            del_filesByPath(c_path)
        else:
            os.remove(c_path)


# 解压文件（参数1：输出目录，参数2：输入要解压的文件）
def unpack_file(output_path, file_name):
    """unzip zip file"""
    zip_file = zipfile.ZipFile(file_name)
    if os.path.isdir(output_path):
        pass
    else:
        os.mkdir(output_path)
    for names in zip_file.namelist():
        zip_file.extract(names, output_path)
    zip_file.close()


# if __name__ == '__main__':
#     # 输入路径
#     CUR_PATH = r'D:\lw_workspace\DataCollection\D_liudan_M_A_20190425\3D'.replace("\\", "/") + "/"
#     del_file(CUR_PATH)
