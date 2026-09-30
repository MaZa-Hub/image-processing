# import the numpy lib
import numpy as np

# create a matrix 
image = np.array(
    [[10, 20, 30, 40], [50, 60, 70, 80], [90, 100, 110, 120], [130, 140, 150, 160]]
)

# show the matrix
print(image)

# show the 2nd row 
print(image[1])

# show the 3rd column
print(image[:, 2])

# show the elements from 2nd row to 3rd row & 2nd column to 3rd column
# also crop the image 
print(image[1:3, 1:3])
