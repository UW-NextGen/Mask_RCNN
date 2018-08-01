import csv
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image
import skimage.io 
import os
import pandas as pd
import numpy as np

def parsecsv(filename):

	for file in os.listdir(os.path.join(mainfolder,folder)):
			datasheet = pd.read_csv(os.path.join(mainfolder, os.path.join(folder, file)))

			major_axis = datasheet['Major'] 
			minor_axis = datasheet['Minor']
			theta = datasheet['Angle']
			h = datasheet['X']
			k = datasheet['Y']
			label = pd.read_csv(os.path.join(mainfolder, os.path.join(folder, file)), usecols=[0])


def parsetext(filename):
	with open(filename) as f:
			defectTypes = {}
			for i in range(6):
				f.readline()
				line = f.readline()
				defectTypes[i] = line.strip().split()
				for j in range(len(defectTypes[i])):
					defectTypes[i][j] = int(defectTypes[i][j])
				f.readline()
			print(defectTypes)







# TEXT LABEL EXTRACTOR

txtfolder = "C:\\Users\\Owner\\Documents\\GitHub\\Mask_RCNN\\MixALL\\logs\\" 


with open('C:\\Users\\Owner\\Documents\\GitHub\\Mask_RCNN\\MixALL\\filenames.txt') as f:
	filename = txtfolder + f.readline()[:-1]

	
	#for folder in os.listdir(txtfolder):
	#for filename in os.listdir(os.path.join(txtfolder,folder)):
		
	while filename != txtfolder:
		#print(filename[54:])
		filetxt = filename + '_log.txt'
		defectTypes_gt = parsetext(filetxt)
		#print(defectTypes_gt)
		filename = txtfolder + f.readline()[:-1]
		print(filename[54:])

	print('Labels Gathered')




#LABELING OBJECT
	#should bring labels gathered by TXT extractor to the CSV into a single array

#JSON MAKER
	#should take all the data from TXT LABELLING OBJECT AND parsecsv and concatenate all of them into a JSON.

