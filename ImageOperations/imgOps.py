import cv2
import numpy as np

hand = cv2.imread('hand.jpg', cv2.IMREAD_COLOR)
#Grabbing and modifying pixels
pixel = hand[55, 55]

print(pixel)

hand[55, 55] = [255, 255, 255]

print(pixel)

#REGION OF INTEREST
ROI = hand[100 : 150, 100 : 150]

print(ROI)

cv2.imshow('window', hand)

cv2.waitKey(0)

cv2.destroyAllWindows()

hand[100 : 150, 100 : 150] = [200, 250, 255]

print(ROI)

cv2.imshow('window but with weird square', hand)

cv2.waitKey(0)

cv2.destroyAllWindows()

#CUTTING AND PASTING USING ROI
hand[100 : 150, 100 : 150] = hand[300 : 350, 300 : 350]

cv2.imshow('window but with weird cut and past', hand)

cv2.waitKey(0)

cv2.destroyAllWindows()
