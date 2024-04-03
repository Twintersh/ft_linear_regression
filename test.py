import pandas
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Sample data
dataset = pandas.read_csv("data.csv")
X = dataset.iloc[:,0].values
Y = dataset.iloc[:,1].values

# Reshape X to be a column vector
X = X.reshape(-1, 1)

# Fit linear regression model
model = LinearRegression()
model.fit(X, Y)

# Predictions
Y_pred = model.predict(X)

# Plot data points and regression line
plt.scatter(X, Y, color='blue')
plt.plot(X, Y_pred, color='red')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Linear Regression')
plt.show()


# Coefficients
print('Slope:', model.coef_[0])
print('Intercept:', model.intercept_)