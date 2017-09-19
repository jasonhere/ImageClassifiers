import os
import glob
from PIL import Image
from array import *
from random import shuffle
import numpy as np
os.chdir('C:/Users/dhavalma/AnacondaProjects/Image Classifier/2ndTrial/data/test/binary/')
# Load from and save to

#Names = [['C:/Users/dhavalma/AnacondaProjects/Image Classifier/2ndTrial/data/test/training-images/0/resized','train'], ['C:/Users/dhavalma/AnacondaProjects/Image Classifier/2ndTrial/data/test/training-images/1/','test']]
Names = [['C:/Users/dhavalma/AnacondaProjects/Image Classifier/2ndTrial/data/test/0/','train'],['C:/Users/dhavalma/AnacondaProjects/Image Classifier/2ndTrial/data/test/training-images/1/','test']]
#%pwd

print(os.listdir('C:/Users/dhavalma/AnacondaProjects/Image Classifier/2ndTrial/data'))


for name in Names:
	#B=[]
	data_image = array('B')
	data_label = array('B')
#print(data_image)
#print(data_label)
	FileList = []
	for dirname in os.listdir(name[0])[1:]: # [1:] Excludes .DS_Store from Mac OS
		path = os.path.join(name[0],dirname)
		for filename in glob.glob(path):
			if filename.endswith(".jpg"):
				FileList.append(os.path.join(name[0],dirname,filename))

	shuffle(FileList) # Usefull for further segmenting the validation set
#print(FileList)
#print(filename)
	for filename in FileList:

		label = int(filename.split('/')[8])

		Im = Image.open(filename)

		pixel = Im.load()

		width, height = Im.size
pixel_values = list(Im.getdata())
print(Im.mode)
#matrix = np.array(Im.getdata()).reshape(Im.size)
print(pixel_values)
#print(label)
        if Im.mode== 'RGB':
            channels = 3
        elif Im.mode == 'L':
            channels = 1
        else:
            print("Unknown mode: %s" % image.mode)
#            return None
print(channels)        
        data_image = np.array(pixel_values).reshape((width, height, channels))
print(data_image)

#		for x in range(0,width):
#			for y in range(0,height):
#                #data_image.append(tuple([int(x) for x in row ]))
#                data_image.append(pixel[y, x][1])
                
		data_label.append(label) # labels start (one unsigned byte each)

	#hexval = "{0:#0{1}x}".format(len(FileList),6) # number of files in HEX
    hexval = "{0:#0{1}x}".format(len(FileList),10) # number of files in HEX

	# header for label array

	#header = array('B')
	#header.extend([0,0,8,1,0,0])
	#header.append(int('0x'+hexval[2:][:2],16))
	#header.append(int('0x'+hexval[2:][2:],16))
	
   header.extend([0,0,8,1])
   header.append(int('0x'+hexval[2:][:2],16))
   header.append(int('0x'+hexval[4:][:2],16))
   header.append(int('0x'+hexval[6:][:2],16))
   header.append(int('0x'+hexval[8:][:2],16))
    
	data_label = header + data_label

	# additional header for images array
#print(max([width,height]))	

	#if max([width,height]) <= 256:
	#	header.extend([0,0,0,width,0,0,0,height])
	#else:
	#	raise ValueError('Image exceeds maximum size: 256x256 pixels');
    hexval = "{0:#0{1}x}".format(width,10) # width in HEX
    header.append(int('0x'+hexval[2:][:2],16))
    header.append(int('0x'+hexval[4:][:2],16))
    header.append(int('0x'+hexval[6:][:2],16))
    header.append(int('0x'+hexval[8:][:2],16))
    hexval = "{0:#0{1}x}".format(height,10) # height in HEX
    header.append(int('0x'+hexval[2:][:2],16))
    header.append(int('0x'+hexval[4:][:2],16))
    header.append(int('0x'+hexval[6:][:2],16))
    header.append(int('0x'+hexval[8:][:2],16))
	header[3] = 3 # Changing MSB for image data (0x00000803)

print(header)
	
	data_image = header + data_image

	output_file = open(name[1]+'-images-idx3-ubyte', 'wb')
	data_image.tofile(output_file)
	output_file.close()

	output_file = open(name[1]+'-labels-idx1-ubyte', 'wb')
	data_label.tofile(output_file)
	output_file.close()

# gzip resulting files

for name in Names:
	os.system('gzip '+name[1]+'-images-idx3-ubyte')
	os.system('gzip '+name[1]+'-labels-idx1-ubyte')
