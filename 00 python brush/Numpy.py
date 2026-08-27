#NUMPY AND PANDAS
import numpy as np
import pandas as pd

# Create a 1D array
array_1d = np.array([1,2,3,4,5])

print("1D Array:", array_1d)
print("1D Array:", *array_1d)

# Create a 2D array
array_2d = np.array([[1,2,3],[4,5,6]])
print("2D Array:\n", array_2d)

# Create a 3D array
array_3d = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print("3D Array:\n", array_3d)

#applying shape and ndim attributes to arrays

a = np.array([1, 2, 3, 4, 5])
b = np.array([[1, 2, 3], [4, 5, 6]])   # 2D array (matrix)
 
print(a.shape)     # (5,)      -> 1D array with 5 elements
print(b.shape)     # (2, 3)    -> 2 rows, 3 columns
print(b.ndim)       # 2         -> number of dimensions
 
zeros = np.zeros((2, 3))       # array of zeros, shape (2,3)
ones = np.ones((3,))            # array of ones
seq = np.arange(0, 10, 2)       # [0 2 4 6 8]  (like range, but an array)
lin = np.linspace(0, 1, 5)      # 5 evenly spaced numbers from 0 to 1

#Array Math — the Real Power of NumPy

prices = np.array([10, 20, 30, 40])
 
print(prices * 1.1)          # [11. 22. 33. 44.]  -> applies to every element at once
print(prices + 5)            # [15 25 35 45]
print(prices.mean())         # 25.0
print(prices.sum())          # 100
print(prices.max(), prices.min())   # 40 10
print(prices.std())          # standard deviation
 
# Compare this to a plain Python list, where you'd need a loop:
# scaled = [p * 1.1 for p in prices_list]
# NumPy does it in one vectorized operation - faster and more readable.

# Reshaping
flat = np.arange(12)               # [0 1 2 ... 11]
matrix = flat.reshape(3, 4)         # reshape into 3 rows, 4 columns
print(matrix)



#PANDAS

