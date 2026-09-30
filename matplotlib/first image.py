# import numpy lib & matplotlib.pyplot
import numpy as np
import matplotlib.pyplot as plt

# define image 
image = np.array(
    [
        [0, 0, 0, 0, 0],
        [0, 255, 255, 255, 0],
        [0, 255, 0, 255, 0],
        [0, 255, 255, 255, 0],
        [0, 0, 0, 0, 0],
    ],
    dtype=np.uint8,
)

# show image
plt.imshow(image, cmap="grey")
plt.show()


