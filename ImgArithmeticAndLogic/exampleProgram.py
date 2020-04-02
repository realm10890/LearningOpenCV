import cv2
import numpy as np
import matplotlib.pyplot as plt

img1 = cv2.imread('building.jpg')
img2 = cv2.imread('HappyFish.jpg')

simpleAddition = img1 + img2

cv2.imshow('Simple Addition', simpleAddition)

cv2.waitKey(0)

cv2.destroyAllWindows()
