# import numpy lib & matplotlib.pyplot
import numpy as np
import matplotlib.pyplot as plt

# define image2
image2 = np.zeros((500, 500), dtype=np.uint8)

# show image2
plt.imshow(image2, cmap="gray")
plt.show()

# slicing
image2[100:400, 100:400] = 255
plt.imshow(image2, cmap="gray")
plt.show()

# horizontal white tape
image2[225:275, :] = 255
plt.imshow(image2, cmap="gray")
plt.show()

# vertical white tape
image2[:, 225:275 ] = 255
plt.imshow(image2, cmap="gray")
plt.show()