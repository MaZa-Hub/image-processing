# import numpy lib
import numpy as np

A = np.array([[1, 2], [3, 4]])

B = np.array([[5, 6], [7, 8]])

C = A + B

print(C)

D = B - A

print(D)

E = B * 3

print(E)

F = A * B

print(F)

G = A @ B

print(G)

H = A.T

print(H)

I = A.max()
J = A.min()
K = A.mean()

print(I)

print(J)

print(K)