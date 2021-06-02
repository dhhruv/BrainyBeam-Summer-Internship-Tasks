import numpy as np
from sklearn.linear_model import LinearRegression

a = np.array([1, 2, 3, 4, 5, 6])
b = np.array([10, 20, 30, 40, 50, 60])
test = np.array([8, 9, 10])
model = LinearRegression()
model.fit(a.reshape(-1, 1), b)
model.predict(test.reshape(-1, 1))
