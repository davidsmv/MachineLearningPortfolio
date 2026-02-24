# Project: https://www.hackerrank.com/challenges/predicting-office-space-price/problem?isFullScreen=true


# Import libraries
from sklearn import linear_model
from sklearn.preprocessing import PolynomialFeatures
import numpy as np



# Set data
features, rows = map(int, input().split())
X, Y = [], []

# Get the parameters X and Y for discovery the variables a and b
for i in range(rows):
    x = []
    elements = list(map(float, input().split()))
    for j in range(len(elements)):
        if j < features:
            x.append(elements[j])
        else:
            Y.append(elements[j])
    X.append(x)

# Set Polynomial Features
poly = PolynomialFeatures(degree=3)

# Set the model LinearRegression
model = linear_model.LinearRegression()
model.fit(poly.fit_transform(np.array(X)), Y)

# Get the parameters X for discovery the Y
new_rows = int(input())
X_test = []
for i in range(new_rows):
    x = []
    elements = list(map(float, input().split()))
    for j in range(len(elements)):
        x.append(elements[j])
    X_test.append(x)

# Gets the result and show on the screen
result = model.predict(poly.fit_transform(np.array(X_test)))
for i in range(len(result)):
    print(round(result[i],2))