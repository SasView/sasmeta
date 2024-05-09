import numpy as np
import matplotlib.pyplot as plt

import cv2

size = 2048

w = size
h = size

x_values = np.arange(w)
y_values = np.arange(h)


x, y = np.meshgrid(x_values-w//2, y_values-h//2)

r = np.sqrt(x**2 + y**2)

scatter = np.sinc(25*r/size)

scatter -= np.min(scatter)
scatter *= (255/np.max(scatter))

scatter = np.array(scatter, dtype=np.uint8)

plt.pcolor(scatter)

cv2.imwrite('bg.jpg', scatter)

cv2.imshow("Image", scatter)

cv2.waitKey()

cv2.destroyAllWindows()
