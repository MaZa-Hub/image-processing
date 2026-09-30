# import numpy lib
import numpy as np

# define image
image = np.array([[10, 20], [30, 40]])

print(image.dtype)

# define image2
image2 = np.array([[0, 128], [200, 255]], dtype=np.uint8)

print(image2.dtype)

# transform image2 to a 32 bit float number
image2= image2.astype(np.float32)

print(image2)