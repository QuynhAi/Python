# Ai Quynh Nguyen
# TCSS 142
# 11/28/18
#
# This program implement a simple machine-learning algorithm to predict 
# whether or not a particular patient has a coronary heart disease. 
# This program will train the data-set and recognize a disease.
# After training, it is capable to predict the existence or absence of disease.
import math
def main():
	healthyList = []
	illList = []
	# counterList[0]: healthy patients counter, 
	# counterList[1]: ill patients counter
	counterList = [0, 0] 

	readFile = open("train.csv", "r")
	getHealthyIllTotals(healthyList, illList, counterList, readFile) 
	readFile.close()

	totalPatients = counterList[0] + counterList[1]
	displayCount(totalPatients, counterList[0], counterList[1])

	healthyAverages = getAverage(healthyList)
	illAverages = getAverage(illList)

	sepValues = getSeparationValues(healthyAverages, illAverages)

	displayList(healthyAverages, "Healthy patients' averages:")
	displayList(illAverages, "Ill patients' averages:")
	displayList(sepValues, "Separation Values:")

	readFile = open("train.csv", "r")
	diagCnt = checkAccuracy(readFile, sepValues)
	accurancy = round(diagCnt / totalPatients, 2)
	print("Accuracy of the model: {}%".format(int(accurancy * 100)))
	readFile.close()


	in1 = open("cleveland.csv", "r")
	output = open("clevelanddiag.csv", "w")
	writeDiagnosis(in1, output, sepValues)
	in1.close()
	output.close()

# params: the healthy patients list, the ill patients list, 
# the healthy ill counters, and data set file
# this function take the data set file and separate into 2 different lists
# one list is for healthy patients, and one list is for ill patients
# the last attribute for each patient is the indication of healthy or ill
# if last attribute is 0 then healthy, if larger than 0 then ill
def getHealthyIllTotals(healthyList, illList, counterList, readFile):
	for line in readFile:
		eachLine = line.split(",")
		if(int(eachLine[-1]) == 0): # healthy patients
			counterList[0] += 1
			healthyList.append(eachLine)
		else:
			counterList[1] += 1 # ill patients
			illList.append(eachLine)

# params: the total patients, the number of healthy patients and number of ill patients
# this function display the number of total patients, number of healthy patients
# and the number of ill patients
def displayCount(total, healthy, ill):
	print("Total Lines Processed: {}".format(total))
	print("Total Healthy Count: {}".format(healthy))
	print("Total Ill Count: {}".format(ill))

# params: the patient list (either healthy or ill)
# if the value of the attribute is a question mark, value is 0
# this function calculate the average value of each attribute/column
# put the average for each column into the new list
# the average for each attribute going to be round to two decimal places
# return the average list 
def getAverage(patientList):
	averageList = [0] * 13
	size = len(averageList)
	# do it for each column
	for i in range(size):
		total = 0
		# get the average for each column
		for elements in patientList:
			# if the value of the attribute is a question mark, value is 0
			if elements[i] == "?":
				elements[i] = 0
			total += float(elements[i])
		averageList[i] = round((total/ len(patientList)), 2)
	return averageList

# params: the average attributes list for healthy patients, and
# averages attributes list for ill patients
# For each attribute, find average between the healthy patients and ill patients
# the average for each attribute going to be round to two decimal places
# Return the average for each attribute as a corresponding separator values
def getSeparationValues(healthyAverages, illAverages):
	separateList = [0] * 13
	for i in range(13):
		total = healthyAverages[i] + illAverages[i]
		separateList[i] = round((total / 2), 2)
	return separateList

# params: the string message, and list
# this function convert the list into a string and 
# display the given message with the values in the list as string
def displayList(listValue, message):
	values = str(listValue[0])
	for i in listValue:
		values = values + "," + str(i) 
	print(message, values)

# params: the data set file, and the corresponding separator value
# if an attribute has higher value than corresponding separator value,
# Then the current patient is at risk of being ill. 
# if a patient has half attributes higher than corresponding 
# separator value, then the patient is ill
# this function call the function that calculate the total 
# correct diagnosis 
# return the number of correct diagnosis
def checkAccuracy(readFile, sepValues):
	original = []
	result = []
	for line in readFile:
		eachLine = line.split(",")
		original.append(eachLine[-1])
		result.append(comparison(eachLine, sepValues))
	correct = correctCounter(original, result)
	return correct

# params: each line from input file, the corresponding separator values
# this function compare each value from the line and each value 
# from the corresponding separator
# if there are more than half values from line with higher value compare
# to corresponding separator, then that person is ill
# return 1 if healthy or 0 if ill
def comparison(eachLine, sepValues):
	counter = 0 
	for i in range(13):
		if eachLine[i] == "?" or eachLine[i] == "?\n":
			eachLine[i] = 0
		if (float(eachLine[i]) > sepValues[i]):
			counter += 1
	# 6 attributes higher than corresponding separator value
	if counter >= 7:
		return 1 # 1 for ill
	# 0 for healthy
	return 0

# params: the actual diagnosis list for all patients, and 
# the predicted diagnosis list for all patients
# this function compare whether if the prediction is correct or not
# return the number of correct diagnosis
def correctCounter(original, result):
	size = len(original)
	correct = 0
	for i in range(size):
		# if actual diagnosis and prediction diagnosis value is 0, 
		# then it is correct
		if (int(original[i]) == 0 and result[i] == 0):
			correct += 1
		# if actual diagosis and prediction diagnosis value is 
		# higher than 0, then it is correct
		elif (int(original[i]) > 0 and result[i] > 0):
			correct += 1
	return correct

# params: the data set file, output csv file, and the corresponding separator
# this function write in the output file the diagnosis result for each patient
# the output file going to consist of patient ID and 1 for healthy or 0 for ill
def writeDiagnosis(readFile, out1, sepValues):
	for line in readFile:
		counter = 0
		patientID = int(line.split(",")[0])
		eachLine = line.split(",")[1:]
		result = comparison(eachLine, sepValues)
		out1.write("{},{} \n".format(patientID, result))

main()
