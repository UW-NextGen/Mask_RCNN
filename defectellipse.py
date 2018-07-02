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

   		major_axis = datasheet['X'] 
   		minor_axis = datasheet['Y']
   		theta = datasheet['Angle']
   		h = pd.read_csv(os.path.join(folder, file))
   		k= pd.read_csv(os.path.join(folder, file))

   		
   		form = 
   		tg = datasheet['Property Tg']





def main():



	"""
	creates masks for all my TIFFS

	"""
	#read in all files
	#extract labels from txts
	#extract a,b, theta, h ,k and label from csvs.
		#define elipse creator object
	
	#patch creation! 
		#combine labels from txt with defect type.

	#write info to JSON






#csv reader widget
def csv_reader():
	with open(filename) as lbl:

	"""
	reads the csv files for a,b, theta, h ,k and label.

	"""


	#create the ellipse maker from a,b, theta, h ,k and label.




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






with open(file) as fc:
	reader = csv.reader(f)
	
	
	temp = 0
	for row in reader:
		if temp == 0:
			temp = 1 
		else:
			defect_number = int(row[0])
			h = float(row[5])
			k = float(row[6])
			angle = float(row[15])




if __name__ == '__main__':
	main()




		





