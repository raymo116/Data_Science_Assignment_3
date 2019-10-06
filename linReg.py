import math
import pandas
from sklearn.model_selection import train_test_split

TRAIN_DATA_FILE = "reg_train.csv"
SPLIT_PERC = 0.2

#read the train file and return the data as two lists (ind and dep variables)
def readData(fname):
	names = ["feature", "prediction"]
	df = pandas.read_csv(fname, names = names)
	x = df[[names[0]]].to_numpy()
	x = x.reshape(x.shape[0],1)

	y = df[[names[1]]].to_numpy()
	y = y.reshape(x.shape[0],1)

	return train_test_split(x, y, test_size=SPLIT_PERC)

def predict(params, x):
	#TODO Fill in prediction functionality

def printParams(params):
	print("The value of B0 (intercept) is: ", params[0])
	print("The value of B1 (slope) is: ", params[1])

#The linear regression algorithm. Takes a list of lists as input
def lreg(x,y):
	params = []
	b0 = 0.0
	b1 = 0.0

    #TODO estimate the linear regression parameters (B0 and B1) here
	#DO NOT USE SciKit Learn functionality here




	params.append(b0)
	params.append(b1)
	return params


#this is the main routine of the program. You should not have to modify anything here
if __name__ == "__main__":
	xTrain, xTest, yTrain, yTest = readData(TRAIN_DATA_FILE)
	parameters = lreg(xTrain,yTrain)
	printParams(parameters)

	#TODO Validation metrics and visualization
	#SciKit Learn and matplotlib.pyplot functions OK here
