import os
import shutil


print("当前目录为   {}".format(os.getcwd()))

suffix = ".html"

# rootDir = 'F:/我们温暖的家/MyWiki分享的文件/MyWiki/'.replace("\\", "/")
rootDir = os.getcwd()
if rootDir[-1] == "/":
    rootDir = rootDir[:-1]
afterDir = rootDir + "/" + suffix[1:]
gitDir = afterDir + "/.git"

for dirName, subdirList, fileList in os.walk(rootDir):  # 遍历目录
    dirName = dirName.replace("\\", "/")

    after_Dir = dirName[rootDir.__len__():]
    after_Dir = afterDir + after_Dir
    if not os.path.exists(after_Dir):  # 如果不存在映射的文件夹，则新建文件夹
        try:
            os.mkdir(after_Dir)
        except:
            print("创建文件夹失败   {}".format(after_Dir))
    shutil.copy("misty-light-windows.css", after_Dir)
    for fname in fileList:
        if os.path.splitext(fname)[-1] == ".md":  # 如果后缀是md则进行转换
            try:
                after_fname =((os.path.join(dirName, os.path.splitext(fname)[0])) + suffix).replace("\\", "/")[rootDir.__len__():]
                after_fname = afterDir + after_fname
                before_fname = (os.path.join(dirName, fname)).replace("\\", "/")
                os.system('pandoc --css="misty-light-windows.css" --metadata pagetitle={} -s -o {} {}'.format(after_fname, after_fname, before_fname))
                print("文件转换完成   {}".format(before_fname))
            except:
                print("文件转换失败   {}".format(os.path.join(dirName, fname)).replace("\\", "/"))

shutil.rmtree(gitDir)   # 删除git目录
# shutil.rmtree(afterDir + "/" + suffix[1:])   # 删除git目录


print("转换完成，任意键退出")
input()