# import numpy lib & matplotlib.pyplot
import numpy as np
import matplotlib.pyplot as plt

image2 = np.zeros((500, 500), dtype=np.uint8)

plt.imshow(image2, cmap="grey")
plt.axis("off")
plt.show()