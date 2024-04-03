import sys
import matplotlib.pyplot as plt
import pandas
import shelve

# theta0 = 9400
# theta1 = -0.028

def estimatePrice(mileage, theta0, theta1):
	return(theta0 + (theta1 * mileage))

def train():
	file = shelve.open(".thetas")
	theta1 = file.get("theta0", 0)
	theta0 = file.get("theta1", 0)
	
	dataset = pandas.read_csv("data.csv")
	x = dataset.iloc[:,0].values
	y = dataset.iloc[:,1].values
	m = len(x)
	learningRate = 0.0001
	total0 = 0
	total1 = 0 
	
	for i in range(m):
		total1 += (estimatePrice(x[i], theta0, theta1) - y[i]) * x[i]
		total0 += (estimatePrice(x[i], theta0, theta1) - y[i])

	print(total0, total1)
	theta1 = learningRate * (total1 / m)
	theta0 = learningRate * (total0 / m)

	file["theta0"] = theta0
	file["theta1"] = theta1
	print(theta0, theta1)

if __name__ == "__main__":
	try:
		train()

		dataset = pandas.read_csv("data.csv")
		x = dataset.iloc[:,0].values
		y = dataset.iloc[:,1].values

		plt.plot(x, y, "o", color='m')
		plt.xlabel('X-axis')
		plt.ylabel('Y-axis')
		plt.title("A simple line graph")
		plt.show()
		
	except SystemExit as e:
		print(e)


# questions :
# 	- What is m ? -> it is the number of values in the dataset
# 	- How to get and what is LearningRate ? I choose it
# 	- Do I need to use the formulas on the data from the data.csv file ? -> i think so