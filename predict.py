import sys
import matplotlib.pyplot as plt
import pandas
import shelve

def getMileage():
	prompt = input("Give the mileage of the car: ")
	if not prompt.isnumeric():
		sys.exit("Error: The given value is not a number")
	mileage = int(prompt)
	return mileage

if __name__ == "__main__":
	try:
		file = shelve.open(".thetas")
		theta1 = file.get("theta0", 0)
		theta0 = file.get("theta1", 0)

		# mileage = getMileage()
		


	except SystemExit as e:
		print(e)
