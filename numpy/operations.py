# import numpy lib
import numpy as np

# define matrix A
A = np.array([[1, 2], [3, 4]])

# define matrix B
B = np.array([[5, 6], [7, 8]])

# Sum of A & B
C = A + B

print(C)

# subtraction A from B
D = B - A

print(D)

# B times 3
E = B * 3

print(E)

# inner product
F = A * B

print(F)

# outer product
G = A @ B

print(G)

# transpose of A
H = A.T

print(H)

# max, min & mean of elements of A
I = A.max()
J = A.min()
K = A.mean()

print(I)

print(J)

print(K)