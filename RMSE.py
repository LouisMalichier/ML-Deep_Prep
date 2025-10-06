import numpy as np

def rmse(y_true, y_pred):
    return round(np.sqrt(np.mean((np.array(y_true) - np.array(y_pred))**2)), 3)
