import shelve
import pandas

def getThetas():
    try:
        file = shelve.open(".thetas")
        t1 = file.get("theta1", 0)
        t0 = file.get("theta0", 0)
        return t0, t1
    except Exception as e:
        exit(e)

def saveThetas(t0, t1):
    try:
        file = shelve.open(".thetas")
        file["theta0"] = t0
        file["theta1"] = t1
    except Exception as e:
        exit(e)

def getDataset():
    try:
        dataset = pandas.read_csv("data.csv")
        x = dataset.iloc[:,0].values
        y = dataset.iloc[:,1].values
        return x, y
    except FileNotFoundError:
        exit("File not found.")
    except pandas.errors.EmptyDataError:
        exit("No data")
    except pandas.errors.ParserError:
        exit("Parse error")
    except Exception:
        exit("Some other exception")
