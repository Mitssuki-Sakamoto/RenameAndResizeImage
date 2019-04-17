# -*- coding: utf-8 -*-
import sys
import glob
import os
import shutil
from PIL import Image
IMG_WIDTH = 640;

args = sys.argv
print(args)
if len(args) == 4 :
    inputDirPath = args[1]
    title = args[2]
    outputDirPath = args[3]
else :
    print("入力形式が間違っています")

if os.path.exists(outputDirPath) :
    shutil.rmtree(outputDirPath)

os.mkdir(outputDirPath)
files = glob.glob(inputDirPath + '/*')
print(files)

for i, f in enumerate(files):
    img = Image.open(f)
    img_resize = img.resize((IMG_WIDTH, int(img.height * (IMG_WIDTH / img.width))))
    ftitle, fext = os.path.splitext(f)
    img_resize.save(outputDirPath + '/' + title + '_' + str(i) + fext)

#files = glob.glob(outputDirPath + '/*')
#print(files)