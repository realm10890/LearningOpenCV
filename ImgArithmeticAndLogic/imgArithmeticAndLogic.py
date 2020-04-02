import cv2
import numpy as np
import matplotlib.pyplot as plt

img1 = cv2.imread('3D-Matplotlib.png')
img2 = cv2.imread('mainsvmimage.png')
img3 = cv2.imread('mainlogo.png')

#Simple Addition of Both Images(not really ideal)
simpleAddition = img1 + img2

cv2.imshow('Simple Addition', simpleAddition)

cv2.waitKey(0)

cv2.destroyAllWindows()

#Built in additon operation(adds pixel values, (155,211,79) + (50, 170, 200) = 205, 381, 279...translated to (205, 255,255).)
addOp = cv2.add(img1, img2)

cv2.imshow('addOperation', addOp)

cv2.waitKey(0)

cv2.destroyAllWindows()

#Adding images using weight
weighted = cv2.addWeighted(img1, 0.6, img2, 0.4, 0)

cv2.imshow('Weighted', weighted)

cv2.waitKey(0)

cv2.destroyAllWindows()

#Adding a picture ontop of another transparently
img2 = cv2.imread('mainlogo.png')

#Creating a ROI to place logo on top left corner
#Getting the dimmensions of the python logo
rows, cols, channels = img2.shape
#rows = 126, cols = 126, channels = 3
#Setting the roi to that specific part of the graph img
roi = img1[0 : rows, 0 : cols]

#make a mask out of the python logo
pythonToGray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)


cv2.imshow('First Step of Mask', pythonToGray)

cv2.waitKey(0)

#cv2.destroyAllWindows()

#adding threshold to the python image(if above 220 it will become white, if below 220 then black)
#right here the snakes are black and the background is white
#Then flip it because of last argument so everything that becomes white is black and everything that is black will become white
#right here the snakes are white and the background is black because of binary inverse
ret, mask = cv2.threshold(pythonToGray, 220, 255, cv2.THRESH_BINARY_INV)

cv2.imshow('Mask', mask)

cv2.waitKey(0)

#cv2.destroyAllWindows()

#making the invisible part of the python image
#bitwise is saying the parts that there is no mask the black area
mask_inv = cv2.bitwise_not(mask)

#the background of the graph image
img1_bg = cv2.bitwise_and(roi, roi, mask = mask_inv)

cv2.imshow('img1_bg', img1_bg)

cv2.waitKey(0)

#cv2.destroyAllWindows()

img2_fg = cv2.bitwise_and(img2, img2, mask = mask)

cv2.imshow('img2_fg', img2_fg)

cv2.waitKey(0)

#cv2.destroyAllWindows()

dst = cv2.add(img1_bg, img2_fg)

img1[0 : rows, 0 : cols] = dst

cv2.imshow('res', img1)

cv2.waitKey(0)

#cv2.destroyAllWindows()
