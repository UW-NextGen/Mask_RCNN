import csv
import matplotlib
import pandas as pd

#reach into the text file and take defect information and make it available for the ellipse maker...?




#text reader widget
	#create defect classification info for the ellipse maker

#CSV READER TOOL#


#h= x
#k= y
# angle = theta
#defect number

data = pd.read_csv("csv_name.csv")

mainfolder = "C:\\NextGen\\Resultlogstxt\\measurement table" 
for folder in os.listdir(mainfolder):

	for file in os.listdir(folder):
		datasheet = pd.read_csv(os.path.join(mainfolder, os.path.join(folder, file)))

   		major_axis = datasheet['Major'] 
   		minor_axis = datasheet['Minor']
   		theta = datasheet['Angle']
   		h = datasheet['X']
   		k= datasheet['Y']

print(h)
print(k)
print(major_axis)
print(minor_axis)
print(theta) 