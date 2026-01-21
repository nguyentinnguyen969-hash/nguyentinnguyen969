import numpy as np
import matplotlib.pyplot as plt

image = np.zeros((100, 100), dtype=np.uint8)        
image[30, 30] = 255 
plt.imshow(image, cmap='gray')
print(image)
plt.show()