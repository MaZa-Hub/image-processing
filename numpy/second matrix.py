# import numpy lib
import numpy as np

# create a matrix
image = np.array([
    [10, 20, 30],
    [40, 255, 60],
    [70, 80, 90]
])

# show the matrix
print(image[1, 2])

# show the matrix dimention
print(image.shape)