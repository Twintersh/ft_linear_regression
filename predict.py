import sys
import matplotlib.pyplot as plt
import pandas

def getMileage():
	prompt = input("Give the mileage of the car: ")
	if not prompt.isnumeric():
		sys.exit("Error: The given value is not a number")
	mileage = int(prompt)
	return mileage

if __name__ == "__main__":
	try:
		# mileage = getMileage()
		dataset = pandas.read_csv("data.csv")
		x = dataset.iloc[:,0].values
		y = dataset.iloc[:,1].values


	except SystemExit as e:
		print(e)
