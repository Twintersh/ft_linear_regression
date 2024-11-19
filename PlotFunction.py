import matplotlib.pyplot as plt
from predict import estimatePrice
from utils import getDataset, getThetas

if __name__ == "__main__":
    try:
        x, y = getDataset()
        t0, t1 = getThetas()

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
        exit(42)
