import csv
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image
import skimage.io 
import os
import pandas as pd

def parse_csv(filename):

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
			for i in range(3):
				f.readline()
				line = f.readline()
				defectTypes[i] = line.strip().split()
				for j in range(len(defectTypes[i])):
					defectTypes[i][j] = int(defectTypes[i][j])
				f.readline()
				print(defectTypes)

with open('C:\\NextGen\\Resultlogstxt\\Logs\\list\\') as f:
	filename = f.readline()[:-5]
	while filename:
		print(filename)
		filetxt = 'dataset/txt/' + filename + '_log.txt'
		#filecsv = 'dataset/csv/' + filename + '_results.csv'
		defectTypes_gt = parsetxt(filetxt)
		#print(defectTypes_gt)
		labels_gt = parsecsv(filecsv, defectTypes_gt)
		outfile = filename + '.txt'
		fout = open(outfile, mode = 'w+')
		for i in range(1, len(labels_gt) + 1):
			if(labels_gt[i][0] == 0 or labels_gt[i][0] == 1 or labels_gt[i][0] == 2 ):
				mylist = calculateBoundingBoxes(labels_gt[i][0], labels_gt[i][1], labels_gt[i][2], labels_gt[i][3], labels_gt[i][4])
			fout.write(str(mylist[0]) +' ' + str(mylist[1]) + ' ' + str(mylist[2]) + ' ' + str(mylist[3]) + ' '+ str(mylist[4]) + '\n')
		fout.close()
		filename = f.readline()[:-5]