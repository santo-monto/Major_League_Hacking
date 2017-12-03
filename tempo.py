import sys
import pandas as pd
import numpy as np

data = pd.read_csv('merge.dat', sep = ' ', header = None)

#Removinf Zero rows.

zero_rows = (data.iloc[:,1]==0)
#Removing NaN rows
nan_rows = (data.iloc[:,:].isnull().any(1))
#Need not remove Zero Rows as it may be useful !!
data.drop(data.index[nan_rows],inplace = True)
hello = data.shape#()
print(hello)
print(data.isnull().sum())

#Target Values are Heart Rate for me.
array_Y = data.iloc[:,2]

#array_X = df.drop()
