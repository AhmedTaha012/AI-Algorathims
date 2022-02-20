# -*- coding: utf-8 -*-
"""LinearRegressionUsingNormalEquation.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hRsQeHh5kMMDg4DY8u7eLkZdK8jh7QJg

Import the modules
"""

import numpy as np

"""My Data"""

data=[[ 23,  3,  8,6562],

         [  15,  2,  7,4569],

         [ 24,  4,  9,6897],

         [  29,  5,  4,7562],

         [ 31,  7,  6,8234]

         ]

"""Get the X and Y**values**"""

x=[]
y=[]
for i in range(len(data)):
  x.append(data[i][0:-1])
  y.append(data[i][-1])
print(x)
print(y)

"""Convert X and Y to numpy arrays"""

x=np.array(x)
ones=np.ones((x.shape[0],1))
x=np.concatenate((ones,x),axis=1)
print(x)
print(x.shape)
y=np.array(y)
y=np.expand_dims(y,axis=-1)
print(y)
print(y.shape)

"""Transpose The X Matrix """

x_transpose=x.T
print(x_transpose)
print(x_transpose.shape)

"""## Multiply The Xtranspose by X take care xt*x not x*xt **bold text**"""

x_mult_x_transpose=np.matmul(x.T,x)
print(x_mult_x_transpose)
print(x_mult_x_transpose.shape)

"""Get The Matrix inverse"""

x_mult_x_transpose_all_inverse=np.linalg.inv(x_mult_x_transpose)
print(x_mult_x_transpose_all_inverse)
print(x_mult_x_transpose_all_inverse.shape)

"""Multiply The Inversed Matrix multiply by the X transpose matrix"""

x_mult_x_transpose_all_inverse_multiplyby_xtranspose=np.dot(x_mult_x_transpose_all_inverse,x_transpose)
print(x_mult_x_transpose_all_inverse_multiplyby_xtranspose)
print(x_mult_x_transpose_all_inverse_multiplyby_xtranspose.shape)

"""Get The Thetass"""

thetas=np.dot(x_mult_x_transpose_all_inverse_multiplyby_xtranspose,y)
print(thetas)
print(thetas.shape)

"""test the model"""

x_test=np.array([ 1,25,  3,  10])
y_test=7485
result=np.dot(thetas.T,x_test)
print("Accuracy Result:",100-((y_test-result)/y_test)*100)