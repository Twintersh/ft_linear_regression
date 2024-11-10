import sys
import shelve

def estimatePrice(mileage, theta0, theta1):
    return(theta0 + (theta1 * mileage))

def getMileage():
	prompt = input("Give the mileage of the car: ")
	if not prompt.isnumeric():
		sys.exit("The given value is not a valid number")
	mileage = int(prompt)
	return mileage

if __name__ == "__main__":
	try:
		file = shelve.open(".thetas")
		t0 = file.get("theta0", 0)
		t1 = file.get("theta1", 0)
		
		mileage = getMileage()
		price = estimatePrice(mileage, t0, t1)
		if price < 0:
			print("The estimate price of your car is bellow 0...")
		else:
			print(f"The estimate price of your car is {price}")

	except SystemExit as e:
		print(f"Error: {e}")
