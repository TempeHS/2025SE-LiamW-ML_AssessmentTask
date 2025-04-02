import export_import
import pickle
import numpy as np



loaded_model = pickle.load(open('my_saved_model1.sav', 'rb'))
predict = np.array([0.1,0.1,False,False,False,False,False,False,False,False,False,False,False,True]).reshape(1, -1)
result = loaded_model.predict(predict)
print(f"{result[0] * 1.2} Global_Sales")