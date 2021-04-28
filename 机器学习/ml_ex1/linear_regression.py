# -*- coding: utf-8 -*-
# @Time : 2021/4/24 15:17
# @Author : yuggu
# @Site : 
# @File : linear_regression.py
# @Software: PyCharm

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def oputidentitymt():
    A = np.eye(4)
    print(A)


def plotData1():
    data = pd.read_csv("ex1data1.txt", header=None, names=['Population', 'Profit'])
    print(data)
    data.plot(kind='scatter', x='Population', y='Profit', figsize=(12, 8))
    plt.show()
    return data


def j_theta(X, y, theta):
    inner = np.power(((X * theta.T) - y), 2)
    return np.sum(inner) / (2 * len(X))


def gradientDescent(X, y, theta, alpha, iters):
    temp = np.matrix(np.zeros(theta.shape))
    var_n = theta.shape[1]
    sum_x = []
    cost = np.zeros(iters)

    for i in range(iters):
        # X * theta.T - y is a column vertor, so is X[:, j]
        error = (X * theta.T - y).T
        for j in range(var_n):
            temp[0, j] = theta[0, j] - alpha * error * X[:, j] / X.shape[0]

        theta = temp
        cost[i] = j_theta(X, y, theta)
    return cost, theta

def regreData1():
    data = plotData1()
    data.insert(0, 'ones', 1)
    theta = np.matrix(np.array([0, 0]))
    X = np.matrix(data.iloc[:, 0:2])
    y = np.matrix(data.iloc[:, 2:3])
    alpha = 0.023
    iters = 10000
    cost, g = gradientDescent(X, y, theta, alpha, iters)
    print(g)

    # we have a linear funciton g(theta_0, theta_1 ...)
    # precit the profit when poplulation is about 3.5 and 7
    predict1 = [1, 3.5] * g.T
    print("when pop is about 3.5, predict1:", predict1)
    predict2 = [1, 7] * g.T
    print("when pop is about 7, predict2:", predict2)

    x = np.linspace(data.Population.min(), data.Population.max(), 100)
    # linear function
    f = g[0, 0] + (g[0, 1] * x)

    fig, ax = plt.subplots(figsize=(12, 8))
    ax.plot(x, f, 'r', label='Prediction')
    ax.scatter(data.Population, data.Profit, label='Traning Data')
    ax.legend(loc=2)
    ax.set_xlabel('Population')
    ax.set_ylabel('Profit')
    ax.set_title('Predicted Profit vs. Population Size')
    plt.show()
    # 原始数据以及拟合的直线

def regreData2():
    data = pd.read_csv("ex1data2.txt", header = None, names = ['Size', 'Bedrooms', 'Price'])
    data = (data - data.mean()) / data.std()
    data.insert(0, 'one', 1)
    cols = data.shape[1]
    X = np.matrix(data.iloc[:, 0:cols - 1])
    y = np.matrix(data.iloc[:, cols - 1:cols])
    alpha = 0.01
    iters = 1500
    normalEqn(X, y)
    theta = np.matrix(np.zeros((1,3)))
    cost, g = gradientDescent(X, y, theta, alpha, iters)
    print(g)

# 正规方程
def normalEqn(X, y):
    theta = np.linalg.inv(X.T@X)@X.T@y #X.T@X等价于X.T.dot(X)
    print(theta)
    return theta

if __name__ == "__main__":
   regreData2()
