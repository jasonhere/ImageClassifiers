# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 16:08:49 2017

@author: dhavalma
"""
import tensorflow as tf
from PIL import Image
import os, sys
%pwd
os.chdir('C:/Users/dhavalma/AnacondaProjects/Image Classifier/2ndTrial/data/test/test-images/0')
def resizeImage(infile, output_dir="./test/", size=(255,255)):
     outfile = os.path.splitext(infile)[0]+"_resized"
     extension = os.path.splitext(infile)[1]

    # if (key(extension, ".jpg")):
    #    return

     if infile != outfile:
        try :
            im = Image.open(infile)
            im.thumbnail(size, Image.ANTIALIAS)
            im.save(output_dir+outfile+extension,"JPEG")
        except IOError:
            print("cannot reduce image for ", infile)


if __name__=="__main__":
    output_dir = "resized"
    dir = os.getcwd()

    if not os.path.exists(os.path.join(dir,output_dir)):
        os.mkdir(output_dir)

    for file in os.listdir(dir):
        resizeImage(file,output_dir)