
import os
import pandas as pd



mainfoldert = "C:\\NextGen\\Resultlogstxt\\Logs\\"
for folder in os.listdir(mainfoldert):

def parsetxt(file)
	with open(filename) as ft:
		defectType = {}
		for i in range(3):
			ft.readline()
			line = ft.readline
			defectTypes[i][j] = line.strip().strip()
			for j in range(len(defectTypes[i]))
				defectTypes[i][j] = int(defectTypes[i][j])
			ft.readline()
		return defectTypes