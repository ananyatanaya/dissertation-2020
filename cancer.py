import numpy as np
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import seaborn as sns # data visualization library  
import matplotlib.pyplot as plt
import time
from subprocess import check_output

# print(check_output(["ls", "../input"]).decode("utf8"))

data = pd.read_csv('./data.csv')
#print(data)
#print(data.head())  # head method show only first 5 rows
col = data.columns       # .columns gives columns names in data 
#print(col)
y = data.diagnosis                          # M or B 
list = ['Unnamed: 32','id','diagnosis']
x = data.drop(list,axis = 1 )
x.head()
ax = sns.countplot(y,label="Count")       # M = 212, B = 357
B, M = y.value_counts()
#print('Number of Benign: ',B)
#print('Number of Malignant : ',M)
x.describe()
                                