import numpy as np

a = [1, 3, 4, 5, 6]
b = [[1, 3, 4, 5, 6], [5, 6, 7, 7, 8]]
print (np.array (b))

# creating one and two-dimensional arrays
print (np.ones (1))

print ('*' * 120)
print (np.ones ((2, 2)))
print ('*' * 120)
# creating random numbers

print (np.random.random ((2, 2)))
print ('*' * 120)
# creating random integer

print (np.random.randint (0, 100, 16))
print ('*' * 120)
# Getting the shape
ran = np.random.randint (0, 100, 16)
print ('Shape of array')
print (ran.shape)
print ('dimension')
print (ran.ndim)
print ('reshape of array')
c = ran.reshape (4, 4)
print (c)
print ('Shape of new array')
print (c.shape)
print ('dimension of new array')
print (c.ndim)
print ('*' * 120)

# Indexing and slicing

# generate evenly spaced values

array = np.arange (1, 10)
print (array)
print ('*' * 120)
print (array[2:5])
print ('*' * 120)
# reshape the new array

arr1 = array.reshape (3, 3)
print (arr1)
print ('*' * 120)
# return the value 3 remember
print (arr1[0, 2])
print ('*' * 120)
# return a column
print (arr1[:, 0])
print ('*' * 120)
# pick the middle
print (arr1[:, 1])
print ('*' * 120)
# pick middle first two numbers
print (arr1[:2, 1])
print ('*' * 120)
# pick from middle and beyond
print (arr1[:2, 1:])
print ('*' * 120)
# get max across rows
print (arr1.max (axis=1))
print ('*' * 120)
# get max across columns
print (arr1.max (axis=0))
print ('*' * 120)
# Working using Prediction formula
prediction = np.array ([2, 5, 6])
lables = np.array ([1, 5, 8])
# MSN = (1/n)Sum(fi-yi)*2 where fi = prediction and yi= lables
difference = prediction - lables
print (difference)
sqdif = np.square (difference)
print(sqdif)
sumsqdif = np.sum(sqdif)
print(sumsqdif)
n = 3
MSE = (1/3)*sumsqdif
print(f'MSN  = {MSE}')

# or
print ('*' * 120)
MSE = (1/3)*sum(np.square(prediction-lables))
print(MSE)
