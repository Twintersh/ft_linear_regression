import pandas
import shelve
from sklearn.preprocessing import StandardScaler
from predict import estimatePrice

def train(x, y):
    # extract thetas
    file = shelve.open(".thetas")
    t1 = file.get("theta1", 0)
    t0 = file.get("theta0", 0)

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

	# save thetas
    file["theta1"] = t1
    file["theta0"] = t0

if __name__ == "__main__":
    try:
        dataset = pandas.read_csv("data.csv")
        x = dataset.iloc[:,0].values
        y = dataset.iloc[:,1].values

        train(x, y)
        print("Model succesfully trained")

    except SystemExit as e:
        print(e)
