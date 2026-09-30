# import numpy lib
import numpy as np

A = np.array([[1, 2, 3], [4, 5, 6]])

print(A.sum())

print(A.mean())

print(A.sum(axis=0))

print(A.sum(axis=1))

print(A.mean(axis=0))

print(A.mean(axis=1))
