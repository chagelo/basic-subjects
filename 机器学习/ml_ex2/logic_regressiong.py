# -*- coding: utf-8 -*-
# @Time : 2021/4/27 13:15
# @Author : yuggu
# @Site : 
# @File : logic_regressiong.py
# @Software: PyCharm

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as opt

def show1(data):
    positive = data[data['Admitted'].isin([1])]
    negative = data[data['Admitted'].isin([0])]

    fig, ax = plt.subplots(figsize=(12, 8))
    ax.scatter(positive['Exam 1'], positive['Exam 2'], s=50, c='b', marker='o', label='Admitted')
    ax.scatter(negative['Exam 1'], negative['Exam 2'], s=50, c='r', marker='x', label='Not Admitted')
    ax.legend()
    ax.set_xlabel('Exam 1 Score')
    ax.set_ylabel('Exam 2 Score')
    plt.show()

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

def cost(theta, X, y):
    theta = np.matrix(theta)
    X = np.matrix(X)
    y = np.matrix(y)
    first = np.multiply(-y, np.log(sigmoid(X * theta.T)))
    second = np.multiply((1 - y), np.log(1 - sigmoid(X * theta.T)))
    return np.sum(first - second) / (len(X))

def proce_1(data):
    data.insert(0, 'one', 1)
    col = data.shape[1]
    X = np.matrix(data.iloc[:, :col - 1])
    y = np.matrix(data.iloc[:, col - 1:col])
    theta = np.zeros(3)
    print(cost(theta, X, y))
    # 在scipy的官方文档看到fmin系列的函数都是不推荐使用的
    result = opt.fmin_tnc(func=cost,x0=theta,fprime=gradient, args =(X, y))
    print(result)

    plotting_x1 = np.linspace(30, 100, 100)
    plotting_h1 = (- result[0][0] - result[0][1] * plotting_x1) / result[0][2]

    positive = data[data['Admitted'].isin([1])]
    negative = data[data['Admitted'].isin([0])]

    fig, ax = plt.subplots(figsize=(12, 8))
    ax.plot(plotting_x1, plotting_h1, 'y', label='Prediction')
    ax.scatter(positive['Exam 1'], positive['Exam 2'], s=50, c='b', marker='o', label='Admitted')
    ax.scatter(negative['Exam 1'], negative['Exam 2'], s=50, c='r', marker='x', label='Not Admitted')
    ax.legend()
    ax.set_xlabel('Exam 1 Score')
    ax.set_ylabel('Exam 2 Score')
    plt.show()

    # 统计预测正确率
    theta_min = np.matrix(result[0])
    predictions = predict(theta_min, X)
    y = np.matrix(y)
    correct = [1 if ((a == 1 and b == 1) or (a == 0 and b == 0)) else 0 for (a, b) in zip(predictions, y)]
    accuracy = (sum(map(int, correct)) / len(correct))
    print('accuracy = {0}%'.format(accuracy))

def gradient(theta, X, y):
    theta = np.matrix(theta)
    X = np.matrix(X)
    y = np.matrix(y)

    parameters = int(theta.ravel().shape[1])
    grad = np.zeros(parameters)

    error = sigmoid(X * theta.T) - y

    for i in range(parameters):
        # @TODO
        grad[i] = np.sum(error.T * X[:,i])
    return grad

# 实现hθ
def hfunc1(theta, X):
    return sigmoid(np.dot(theta.T, X))


# 定义预测函数
def predict(theta, X):
    X = np.matrix(X)
    probability = sigmoid(X * theta.T)
    return [1 if x >= 0.5 else 0 for x in probability]

if __name__ == '__main__':
    data = pd.read_csv("ex2data1.txt", header = None, names = ['Exam 1', 'Exam 2', 'Admitted'])
    show1(data)
    proce_1(data)
