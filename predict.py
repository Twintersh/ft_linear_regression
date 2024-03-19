import sys

def getMileage():
	prompt = input("Give the mileage of the car: ")
	if not prompt.isnumeric():
		sys.exit("Error: The given value is not a number")
	mileage = int(prompt)
	return mileage

if __name__ == "__main__":
	try:
		mileage = getMileage()
	except SystemExit as e:
		print(e)
