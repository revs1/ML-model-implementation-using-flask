import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle

dataset = pd.read_csv('housing.csv')

dataset['population'].fillna(dataset['population'].mean(), inplace=True)
dataset['households'].fillna(dataset['median_income'].mean(), inplace=True)
dataset['median_house_value'].fillna(dataset['median_house_value'].mean(), inplace=True)
dataset['longitude'].fillna(dataset['longitude'].mean(), inplace=True)
dataset['latitude'].fillna(dataset['latitude'].mean(), inplace=True)
dataset['housing_median_age'].fillna(dataset['housing_median_age'].mean(), inplace=True)
dataset['total_rooms'].fillna(dataset['total_rooms'].mean(), inplace=True)
dataset['total_bedrooms'].fillna(dataset['total_bedrooms'].mean(), inplace=True)



X = dataset.iloc[:, 3:6]
y = dataset.iloc[:, -2]


from sklearn.linear_model import LinearRegression
regressor = LinearRegression()

regressor.fit(X, y)

pickle.dump(regressor, open('model.pkl','wb'))

model = pickle.load(open('model.pkl','rb'))
print(model.predict([[880, 129, 332]]))
