import os
import time

dirpath = "/home/denis/test/"

for path,dirs,files in os.walk(dirpath):
    for file in files:
        fullname=path+"/"+file
        mtime=os.stat(fullname).st_mtime
        mtimestring=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(mtime))
        print ("\"" + fullname + "\"," + mtimestring)
