import shelve
import pandas

def getThetas():
    file = shelve.open(".thetas")
    t1 = file.get("theta1", 0)
    t0 = file.get("theta0", 0)
    return t0, t1

def saveThetas(t0, t1):
    file = shelve.open(".thetas")
    file["theta0"] = t0
    file["theta1"] = t1

def getDataset():
    try:
        dataset = pandas.read_csv("data.csv")
        x = dataset.iloc[:,0].values
        y = dataset.iloc[:,1].values
        return x, y
    except FileNotFoundError:
        exit("File not found.")
    except pd.errors.EmptyDataError:
        exit("No data")
    except pd.errors.ParserError:
        exit("Parse error")
    except Exception:
        exit("Some other exception")
