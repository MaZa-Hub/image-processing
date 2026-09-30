import numpy as np
import matplotlib.pyplot as plt

image = np.zeros((500, 500), dtype=np.uint8)

image += 255
print(image)

image[200:300,200:300]=200
plt.imshow(image, cmap="gray")
plt.show()

image[100:200,100:200]=0
plt.imshow(image, cmap="gray")
plt.show()