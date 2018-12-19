import shutil, os
import main
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
import os

rootdir = r"F:\BaiduNetdiskDownload"


def list_all_files(rootdir):
    import os
    _files = []
    dirs = os.listdir(rootdir) #列出文件夹下所有的目录与文件
    for i in range(0, len(dirs)):
        path = os.path.join(rootdir, dirs[i])
        if os.path.isdir(path):
            _files.extend(list_all_files(path))
        if os.path.isfile(path):
            _files.append(path)
    return _files

res = list_all_files(rootdir=rootdir)
for i in range(0, len(res)):
    cmd = "ffmpeg.exe -i %s -f wav -ar 16000 %s" % (res[i], res[i] + ".wav")
    os.system(cmd)
    print(cmd)
