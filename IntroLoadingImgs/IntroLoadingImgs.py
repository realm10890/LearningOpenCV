import cv2
import numpy as np
import matplotlib.pyplot as plt

#defining a variable to hold an image
img = cv2.imread('appleWatchSampleCV.jpg', cv2.IMREAD_GRAYSCALE )
#CAN ALSO DO IMREAD_COLOR = 1 AND IMREAD_UNCHANGED = -1

#method to show image
cv2.imshow('Window', img)

#wait key that waits for a click in order to do the next code
cv2.waitKey(0)

#Destroys the currently shown windows
cv2.destroyAllWindows()

#Saving an image after it is destroyed
cv2.imwrite('grayAppleWatch.png', img)

"""""
USING MATPLOTLIB
plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.plot([50, 100],[80, 100], 'c', linewidth = 5)
plt.show()
"""""
