import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

dataset = pd.read_csv("50_Startups.csv")
X = dataset.iloc[:, :-1]
Y = dataset.iloc[:, 4]

states = pd.get_dummies(X["State"], drop_first=True)

X = X.drop("State", axis=1)

X = pd.concat([X, states], axis=1)

from sklearn.linear_model import LinearRegression

# importing methods/packages for random state
from sklearn.model_selection import train_test_split

# implementing train_test_split() for random state
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=0)

regressor = LinearRegression()
regressor.fit(X_train, Y_train)

yp = regressor.predict(X_test)
