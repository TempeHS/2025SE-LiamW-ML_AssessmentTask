import export_import
import pickle
import numpy as np


def predict(data):
    loaded_model = pickle.load(open('my_saved_model1.sav', 'rb'))
    predict = np.array(data).reshape(1, -1)
    result = loaded_model.predict(predict)
    output = f"{result[0] * 1.2} Global_Sales"
    return output