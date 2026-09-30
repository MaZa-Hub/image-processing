# import numpy lib
import numpy as np

# define image
image = np.array([[100, 200], [240, 250]], dtype=np.uint8)

print(image.dtype)

image = image + 30

# show false results
print(image)

# define image2
image2 = np.array([[100, 200], [240, 250]], dtype=np.uint8)

# transform image2 to 32 bit float number
image2 = image2.astype(np.float32)

image2 = image2 + 30

print(image2)

# clip image2 to an 8 bit uint number
image2 = np.clip(image2, 0, 255)

print(image2)
