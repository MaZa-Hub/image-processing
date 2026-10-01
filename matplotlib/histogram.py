import numpy as np
import matplotlib.pyplot as plt

image = np.array([
    [10, 10, 20],
    [20, 20, 20],
    [30, 40, 40]
])

plt.hist(image.ravel(), bins=256, range=(0, 256))
plt.show()