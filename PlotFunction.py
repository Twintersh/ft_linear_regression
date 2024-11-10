import matplotlib.pyplot as plt
import pandas
import shelve
from predict import estimatePrice

if __name__ == "__main__":
    try:
        dataset = pandas.read_csv("data.csv")
        x = dataset.iloc[:,0].values
        y = dataset.iloc[:,1].values

        file = shelve.open(".thetas")
        t0 = file.get("theta0", 0)
        t1 = file.get("theta1", 0)

        y_xmin = estimatePrice(min(x), t0, t1)
        y_xmax = estimatePrice(max(x), t0, t1)

        plt.plot(x, y, "o", color='blue')
        plt.plot([min(x), max(x)], [y_xmin, y_xmax], color='red')
        plt.xlabel('X-axis')
        plt.ylabel('Y-axis')
        plt.title("ft_linear_regression")
        plt.show()
    except SystemExit as e:
        print(e)