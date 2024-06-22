import pandas as pd
data = pd.read_csv('C:\\Users\\Downloads\\Data.csv')
type(data)
pandas.core.frame.DataFrame
data.info
data.describe()
data = data.drop_duplicates()
data.isnull()
data.isnull().sum()
data.notnull()
data.isnull().sum().sum()
data2 = data.fillna(value=0)
data3 = data.fillna(method = 'pad')
data4 = data.fillna(method = 'bfill')

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

data2.columns
data2.drop(['Observation'], axis=1, inplace = True)
data2.columns
q1 = data2.quantile(0.25)
q2 = data2.quantile(0.75)
qr = q2-q1
print(qr)
data2 = data2[~((data2<(q1-1.5*qr))|(data2>(q2+1.5*qr))).any(axis=1)]
