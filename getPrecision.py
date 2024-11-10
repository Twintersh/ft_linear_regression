# program that calculates the precision of the model
from predict import estimatePrice
from utils import getThetas, getDataset
from math import sqrt

def meanSquaredError(x, y, t0, t1):
    n = float(len(x))
    pred_y = estimatePrice(x, t0, t1)
    mse = 1/n * sum((y[i] - pred_y[i])**2 for i in range(len(x)))
    return mse

if __name__ == "__main__":
    x, y = getDataset()
    t0, t1 = getThetas()
    mse = meanSquaredError(x, y, t0, t1)
    print(f"Here is the precision of your model : {mse}\n(according to the meanSquaredError function)")
