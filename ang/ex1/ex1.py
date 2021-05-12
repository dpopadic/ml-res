# ------------- Machine Learning - Topic 1: Linear Regression

#  Instructions
#  ------------
#
#  This file contains code that helps you get started on the
#  linear exercise. You will need to complete the following functions
#  in this exercise:
#
#     warmUpExercise
#     plotData
#     gradientDescent
#     computeCost
#
# x refers to the population size in 10,000s
# y refers to the profit in $10,000s
import os, sys
sys.path.append(os.getcwd() + os.path.dirname('/ang/ex1/'))
from helpers import warmUpExercise, computeCost, gradientDescent, plotData
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

## ==================== Part 1: Basic Function ====================
print('Running warmUpExercise...')
print('5x5 Identity Matrix: ')

print(warmUpExercise())

input('Program paused. Press enter to continue.\n')

## ======================= Part 2: Plotting =======================
print('Plotting Data...')

data = np.loadtxt('ang/ex1/ex1data1.txt', delimiter=",")
X = data[:, 0]
y = data[:, 1]
m = len(y) # number of training examples

# Plot Data
plotData(X, y)

input('Program paused. Press enter to continue.\n')

## =================== Part 3: Gradient descent ===================
print('Running Gradient Descent...')

X_padded = np.column_stack((np.ones((m,1)), X)) # Add a column of ones to x
theta = np.zeros((2, 1)) # initialize fitting parameters

# Some gradient descent settings
iterations = 1500
alpha = 0.01

# compute and display initial cost
print(computeCost(X_padded, y, theta))

# run gradient descent
theta = gradientDescent(X_padded, y, theta, alpha, iterations)

# print theta to screen
print('Theta found by gradient descent: ')
print("{:f}, {:f}".format(theta[0,0], theta[1,0]))

# Plot the linear fit
plt.plot(X, X_padded.dot(theta),'-', label='Linear regression')
plt.legend(loc='lower right')
plt.draw()
plt.hold(False) # prevents further plotting on the same figure

# Predict values for population sizes of 35,000 and 70,000
predict1 = np.array([1, 3.5]).dot(theta)
print("For population = 35,000, we predict a profit of {:f}".format( float(predict1*10000) ))
predict2 = np.array([1, 7]).dot(theta)
print('For population = 70,000, we predict a profit of {:f}'.format( float(predict2*10000) ))

input('Program paused. Press enter to continue.\n')

## ============= Part 4: Visualizing J(theta_0, theta_1) =============
print('Visualizing J(theta_0, theta_1)...')

# Grid over which we will calculate J
theta0_vals = np.linspace(-10, 10, 100)
theta1_vals = np.linspace(-1, 4, 100)

# initialize J_vals to a matrix of 0's
J_vals = np.zeros((len(theta0_vals), len(theta1_vals)))

# Fill out J_vals
for i in range(len(theta0_vals)):
    for j in range(len(theta1_vals)):
        t = [[theta0_vals[i]], [theta1_vals[j]]]
        J_vals[i, j] = computeCost(X_padded, y, t)

# Because of the way meshgrids work in the surf command, we need to
# transpose J_vals before calling surf, or else the axes will be flipped
J_vals = np.transpose(J_vals)

# Surface plot
fig = plt.figure()
ax = fig.gca(projection='3d')
theta0_vals, theta1_vals = np.meshgrid(theta0_vals, theta1_vals) # necessary for 3D graph
surf = ax.plot_surface(theta0_vals, theta1_vals, J_vals, cmap=cm.coolwarm, rstride=2, cstride=2)
fig.colorbar(surf)
plt.xlabel('theta_0')
plt.ylabel('theta_1')
plt.show(block=False)
plt.hold(False)


# Contour plot
fig = plt.figure()
ax = fig.add_subplot(111)
# # Plot J_vals as 20 contours spaced logarithmically between 0.01 and 100
cset = plt.contour(theta0_vals, theta1_vals, J_vals, np.logspace(-2, 3, 20), cmap=cm.coolwarm)
fig.colorbar(cset)
plt.xlabel('theta_0')
plt.ylabel('theta_1')
plt.hold(True)
plt.plot(theta[0,0], theta[1,0], 'rx', markersize=10, linewidth=2)
plt.show(block=False)
plt.hold(False)

input('Program paused. Press enter to finish.\n')










