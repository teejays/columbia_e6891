# Reporducting Computational Results
# EECS E6891, Columbia Univeristy
# Talha Jawad Ansari

# import packages
import numpy as np
import os

debug = False


# Load and make the soundfiles name and info dataset
def csvToList(filename, dropValues=[], ignoreFirstRow=False, debug=False):
	rawData_temp = open(filename, 'r')
	rawData = [];
	for row in rawData_temp:
		row_data = row.strip().split(',')
		# Check to see if the particular recording is to be dropped
		if (row_data[1] not in dropValues):
			rawData.append(row_data)
		else:
			print('Dropped!' + str(row_data[1]))
	# Drop the first row, as it only contains labels			
	if (ignoreFirstRow):
		rawLabels = rawData.pop(0)
	else:
		rawLabels = rawData[0]
	if (debug):
		print(rawData)
	return rawData, rawLabels

def dataCleanup(rawData, rawLabels, pathToSoundfiles=''):
	# iterate over each soundfile
	N = len(rawData)
	print(N)
	post_append = '_44k.wav'

	for i in range(N):
		catalog = str(rawData[i][1])
		filename = pathToSoundfiles + catalog + post_append

		# Do something with the files now
		# 1. Add size data to rawData:
		soundfile_size = os.stat(filename).st_size
		rawData[i].append(soundfile_size)

	
	rawLabels.append('size')
	return rawData, rawLabels



################### SCRIPT ###################

dropValues = ['184893'] # Catalog numbers of soundfiles to be ignored
spreadsheetName = 'ML_Order_30012802014_Mar_11_17_57_44.csv'
pathToSoundfiles='../bird_sounds_data/'

rawData, rawLabels = csvToList(spreadsheetName, dropValues=dropValues, ignoreFirstRow=True, debug=debug)
rawData, rawLabels = dataCleanup(rawData, rawLabels, pathToSoundfiles)


print(rawLabels)
print(rawData[0])
