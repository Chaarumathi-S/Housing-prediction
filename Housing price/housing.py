# -*- coding: utf-8 -*-
"""Housing.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Xe7kFJZRzDAawzbLx4y7-SZ47k1Y6c71
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("housing.csv")

data

data.info()

data.dropna(inplace=True)

data.info()

#train test split
from sklearn.model_selection import train_test_split

z = data.drop("median_house_value", axis=1)
y = data["median_house_value"]

z_train, z_test, y_train, y_test = train_test_split(z, y, test_size=0.2)

#Analysing the basic correlation

train_data = z_train.join(y_train)

train_data

train_data.hist()

train_data.hist(figsize = (15,8))

plt.figure(figsize=(15,8))
sns.heatmap(train_data.corr(numeric_only=True), annot=True)

train_data['total_rooms'] = np.log(train_data['total_rooms'] + 1)
train_data['total_bedrooms'] = np.log(train_data['total_bedrooms'] + 1)
train_data['population'] = np.log(train_data['population'] + 1)
train_data['households'] = np.log(train_data['households'] + 1)

train_data.hist(figsize = (15,8))

train_data.ocean_proximity.value_counts()

train_data.join(pd.get_dummies(train_data.ocean_proximity, dtype=int))

train_data = train_data.join(pd.get_dummies(train_data.ocean_proximity, dtype=int)).drop(['ocean_proximity'],axis = 1)

plt.figure(figsize=(15,8))
sns.heatmap(train_data.corr(numeric_only=True), annot=True)

plt.figure(figsize=(15,8))
sns.scatterplot(x='longitude', y='latitude', data=train_data, hue='median_house_value', palette="coolwarm")

train_data['bedrrom_ratio'] = train_data['total_bedrooms']/train_data['total_rooms']
train_data['household_rooms'] = train_data['total_rooms']/train_data['households']

plt.figure(figsize=(15,8))
sns.heatmap(train_data.corr(numeric_only=True), annot=True)

from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler


z_train,y_train = train_data.drop(['median_house_value'],axis = 1),train_data['median_house_value']


reg = LinearRegression()

reg.fit(z_train,y_train)

LinearRegression()

test_data = z_test.join(y_test)

test_data['total_rooms'] = np.log(test_data['total_rooms'] + 1)
test_data['total_bedrooms'] = np.log(test_data['total_bedrooms'] + 1)
test_data['population'] = np.log(test_data['population'] + 1)
test_data['households'] = np.log(test_data['households'] + 1)

test_data = test_data.join(pd.get_dummies(test_data.'ocean_proximity', dtype=int)).drop(['ocean_proximity'],axis = 1)




test_data['bedrrom_ratio'] = test_data['total_bedrooms']/test_data['total_rooms']
test_data['household_rooms'] = test_data['total_rooms']/test_data['households']

z_test,y_test = test_data.drop(['median_house_value'],axis = 1),test_data['median_house_value']

reg = LinearRegression()

reg.fit(z_test,y_test)

test_data

reg.score(z_test,y_test)

from sklearn.ensemble import RandomForestRegressor

forest = RandomForestRegressor()

forest.fit(z_train,y_train)

RandomForestRegressor()

GridSearchCV(cv=5, estimator=RandomForestRegressor(),
             param_grid={'max_features': [2, 4, 6, 8], 'n_estimators': [3, 10, 30]}, return_train_score=True,scoring='neg_mean_squared_error')

best_forest = grid_search.best_estimator_