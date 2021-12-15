# https://numpy.org/
from array import array
from statistics import mean

import numpy as np

# array and mat ----------------------------------------------------------

lst = [1, 2, 3, ]
arr = np.array(lst)
mat = [[1, 2, 3], [1, 2, 3]]
np_mat = np.array(mat)

range_arr = np.arange(0, 10)
z = np.zeros((3, 4))  # rows, columns
lin = np.linspace(0, 10, 3)

i_mat = np.eye(5)

ar = np.zeros(25)
ar.reshape(5, 5)

# in python [:] its deep copy of the array, in numpy wll need to explicitly do it .copy()

# random---------------------------------------------------------------
np.random.seed(42)
rand = np.random.rand(5, 2)
normal_dis = np.random.randn(2, 3)
int_rand = np.random.randint(5)

# op---------------------------------------------------------------
print(arr)
arr + 5
print(arr)
arr.sum()
arr.mean()
arr.var()
arr.std()