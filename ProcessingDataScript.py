import pandas as pd
from sklearn.linear_model import LinearRegression

data = pd.read_csv('Data_Format.csv')#Change Your File Data
data['TopoParasnis'] = data['Topo']*0.04193

data.to_csv('Parasnis.csv',index = False)
data2 = pd.read_csv('Parasnis.csv')
parasnis = pd.read_csv('Parasnis.csv', usecols=['TopoParasnis', 'Faa'])

#LINEAR REGRESSION
train_x = parasnis[['TopoParasnis']]
train_y = parasnis[['Faa']]
regr = LinearRegression()
regr.fit (train_x, train_y)
print('Coefficients: ', regr.coef_)
print('Intercept: ', regr.intercept_)
a= float(input("Copy Coeffisient Value = ",))

#BOUGER ANOMALY VALUE
data2['Bouger Anomaly'] = data2['Topo']*0.04193*a

# EXPORT DATA
data2.to_excel('Bouger Anomaly Result.xlsx',index = False)#Bouger Anomaly Result File
