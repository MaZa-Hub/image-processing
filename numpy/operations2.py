# import numpy lib
import numpy as np

# define A
A = np.array([[1, 2, 3], [4, 5, 6]])

# sum of elements
print(A.sum())

# mean of elements
print(A.mean())

# sum of elements through rows
print(A.sum(axis=0))

# sum of elements through columns
print(A.sum(axis=1))

# mean of elements through rows
print(A.mean(axis=0))

# sum of elements through columns
print(A.mean(axis=1))
