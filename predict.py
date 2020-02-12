import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

# y = output
# b = weight
# a = bias
# x = input
def activation_func(input, bias, weight):
    output = bias + weight * input
    print('y =', bias, '+', weight, '*', input)
    return output

N = 10
x = np.array([17, 13, 15, 11, 19, 10, 12, 11, 13, 14])
y = np.array([11, 15, 14, 18, 10, 19, 16, 15, 15, 14])

x_sum = np.sum(x)
y_sum = np.sum(y)

x_sqr_sum = np.sum(np.square(x))
x_y_sum = np.sum(np.multiply(x, y))

print('----------------------------------------------------------------------------------------------')
print('N = ', N, '\nS(X) =', x_sum, '\nS(Y) =', y_sum, '\nS(X^2) =', x_sqr_sum, '\nS(X*Y) =', x_y_sum)
print('\nEquations sistem:')
print('[1]', N, '* a', '+', x_sum, '* b', '=', y_sum)
print('[2]', x_sum, '* a', '+', x_sqr_sum, '* b', '=', x_y_sum)

a = np.array([[10, 135], [135, 1895]])
b = np.array([147, 1918])

# [bias, weight]
[a, b] = np.linalg.solve(a, b)
print('a =', a, '; b =', b)
print('------------------------------------------[activation_func]-----------------------------------')
x0 = 11
x1 = 14
output0 = activation_func(x0, a, b)
output1 = activation_func(x1, a, b)
print('x0 =', x0, '=>', 'y0', '=', output0)
print('x1 =', x1, '=>', 'y1', '=', output1)
