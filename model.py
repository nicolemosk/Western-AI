from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
from sklearn.preprocessing import PolynomialFeatures
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import yfinance as yf
import pickle
import requests
import json

#dataset = pd.read_csv('TSLA.csv')

# or use yfinance library

dataset = yf.download('TSLA','2010-01-01','2022-01-01')
# choose predictors
x = dataset[["High", "Low", "Open", "Volume"]].values
y = dataset['Close'].values

#split data

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size= 0.2, random_state= 0)

regressor = LinearRegression()

# fit model

regressor.fit(x_train, y_train)
print(regressor.coef_)
print(regressor.intercept_)
predicted = regressor.predict(x_test)
print(predicted)
dframe = pd.DataFrame({'Actual':y_test.flatten(),"Predicted":predicted.flatten()})
dframe.head(25)
# check metrics

print("Mean Absolute Error: ", metrics.mean_absolute_error(y_test,predicted))
print("Mean Squared Error: ", metrics.mean_squared_error(y_test, predicted))
print("Root Mean Squared Error: ", np.sqrt(metrics.mean_squared_error(y_test,predicted)))

with open('model.pkl', 'wb') as model_file:
    pickle.dump(regressor, model_file)
