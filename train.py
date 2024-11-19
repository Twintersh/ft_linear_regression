from sklearn.preprocessing import StandardScaler
from utils import getDataset, getThetas, saveThetas

def train(x, y):
    # extract thetas
    t0, t1 = getThetas()

    # data normalization to avoid overflows
    scaler_x = StandardScaler()
    scaler_y = StandardScaler()
    x = scaler_x.fit_transform(x.reshape(-1, 1)).flatten()
    y = scaler_y.fit_transform(y.reshape(-1, 1)).flatten()

    # setting the necessary variables to process gradient descent algorithm
    L = 0.01
    epochs = 1000
    m = float(len(x))

    # Process Gradient Descent 
    for i in range(epochs): 
        y_pred = t1 * x + t0 
        tmp_t1 = L * (1 / m) * sum(x * (y_pred - y))
        tmp_t0 = L * (1 / m) * sum(y_pred - y)
        t1 = t1 - tmp_t1 
        t0 = t0 - tmp_t0 
 
    # unnormalize the data 
    t1 = t1 * (scaler_y.scale_[0] / scaler_x.scale_[0])
    t0 = scaler_y.mean_[0] - t1 * scaler_x.mean_[0]

    saveThetas(t0, t1)

if __name__ == "__main__":
    try:
        x, y = getDataset()
        
        train(x, y)
        print("Model succesfully trained")

    except SystemExit as e:
        print(e)
        exit(42)
