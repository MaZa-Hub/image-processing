# import the numpy lib to the code
import numpy as np

# create a matrix 
image = np.array(
    [[10, 20, 30, 40], [50, 60, 70, 80], [90, 100, 110, 120], [130, 140, 150, 160]]
)

# show the whole matrix
print(image)

# show the second row of matrix
print(image[1])

# show  the third column
print(image[:, 2])

# show the elements from second row to third row and second column to third column
# also crop the image
print(image[1:3, 1:3])
