# import numpy lib & matplotlib.pyplot
import numpy as np
import matplotlib.pyplot as plt

# define image2
image2 = np.zeros((500, 500), dtype=np.uint8)

# show image2
plt.imshow(image2, cmap="grey")
plt.show()