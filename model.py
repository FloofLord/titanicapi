import pandas as pd
import pickle
from sklearn.externals import joblib

import numpy as np

data = np.array([1,0,38,1,0,71.28])
data  = data.reshape(1,-1)
print(data)




loaded_model = joblib.load('model.pkl')
result = loaded_model.predict(data)
print(result)
