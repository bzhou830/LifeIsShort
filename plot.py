#!/usr/bin/env python
# coding=utf-8
import numpy as np
import matplotlib.pyplot as plt

'''
xData = np.arange(0, 10, 1)
yData1 = xData.__pow__(2.0)
yData2 = np.arange(15, 61, 5)
plt.figure(num=1, figsize=(8, 6))
plt.title('Plot 1', size=14)
plt.xlabel('x-axis', size=14)
plt.ylabel('y-axis', size=14)
plt.plot(xData, yData1, color='b', linestyle='--', marker='o', label='y1 data')
plt.plot(xData, yData2, color='r', linestyle='-', label='y2 data')
plt.legend(loc='upper left')
plt.savefig('plot1.png', format='png')
'''

mu = 0.0
sigma = 2.0
samples = np.random.normal(loc=mu, scale=sigma, size=1000)
plt.figure(num=1, figsize=(8, 6))
plt.title('Plot 2', size=14)
plt.xlabel('value', size=14)
plt.ylabel('counts', size=14)
plt.hist(samples, bins=40, range=(-10, 10))
plt.text(-6, 100, r'$\mu$ = 0.0, $\sigma$ = 2.0', size=16)
plt.savefig('plot2.png', format='png')

data = [33, 25, 20, 12, 10]
plt.figure(num=1, figsize=(6, 6))
plt.axes(aspect=1)
plt.title('Plot 3', size=14)
plt.pie(data, labels=('Group 1', 'Group 2', 'Group 3', 'Group 4', 'Group 5'))
plt.savefig('plot3.png', format='png')

