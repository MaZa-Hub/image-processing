# import numpy lib
import numpy as np

# define A
A = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])

# add 5 to all elements
print(A + 5)

# add [1 2 3] to every rows
print(A + np.array([1, 2, 3]))

# add transpose of [10 20 30] to every columns
print(A + np.array([[10], [20], [30]]))
