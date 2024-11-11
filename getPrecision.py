# program that calculates the precision of the model
from predict import estimatePrice
from utils import getThetas, getDataset
from math import sqrt

def determinationCoef(x, y, t0, t1):
    n = float(len(x))
    pred_y = estimatePrice(x, t0, t1)
    mean_y = sum(pred_y) / n
    coef =  1 - sum((y - pred_y)**2) / sum((y - mean_y)**2)
    return coef

if __name__ == "__main__":
    try:
        x, y = getDataset()
        t0, t1 = getThetas()
        coef = determinationCoef(x, y, t0, t1)
        print(f"Here is the precision of your model : {coef}\n(according to the coefficient of determination)")

    except SystemExit as e:
        print(e)