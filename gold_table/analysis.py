# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 01:03:30 2018

@author: PeterLi
"""


import pandas as pd
import numpy as np
from time import strptime
from datetime import datetime
import matplotlib.pyplot as plt

dataset = pd.read_csv("gold.csv")
dataset['number'] = dataset.index


index = dataset['price'].index
dataset = dataset.drop(['date','vol','opened','high','low',], axis = 1)


#change the format of the prices
price_price = [float(x.replace(',', '')) for x in dataset['price']]
dataset['price']= pd.DataFrame({'price': price_price})['price']

# change the format of the percent
price_per_format = [float(x.replace('%', '')) for x in dataset['change_per']]
dataset['change_per']= pd.DataFrame({'change_per': price_per_format})['change_per']

x = dataset.iloc[:,2:3].values

y = dataset.iloc[:,0].values

z = dataset.iloc[:,1].values


# fitting linear regression to the dataset of the price
from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(x, y)

# fitting polynomial regression to the dataset of the price
from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures(degree = 4)
x_poly = poly_reg.fit_transform(x)
poly_reg.fit(x_poly, y)
lin_reg_2 = LinearRegression()
lin_reg_2.fit(x_poly, y)

#visualising the polynomial results
plt.scatter(x, y, color = 'red')
plt.plot(x, lin_reg_2.predict(poly_reg.fit_transform(x)), color = 'blue')
plt.title('Gold Historical Data of Price(Polynomial Regression)')
plt.xlabel('Date index')
plt.ylabel('Price')
plt.show()


# fitting linear regression to the dataset of the price change percentage 
lin_reg_per = LinearRegression()
lin_reg_per.fit(x, z)

#fitting polynomial regression to the dataset of the price change percentage 
poly_reg_per = PolynomialFeatures(degree = 4)
x_poly_per = poly_reg_per.fit_transform(x)
poly_reg_per.fit(x_poly_per, z)
lin_reg_2_per = LinearRegression()
lin_reg_2_per.fit(x_poly_per, z)

#visualising the polynomial results
plt.scatter(x, z, color = 'red')
plt.plot(x, lin_reg_2_per.predict(poly_reg_per.fit_transform(x)), color = 'blue')
plt.title('Gold Historical Data of Price change percentage(Polynomial Regression)')
plt.xlabel('data index')
plt.ylabel('Price change percent')
plt.show()
