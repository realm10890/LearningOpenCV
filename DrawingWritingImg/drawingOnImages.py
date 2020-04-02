import cv2
import numpy as np

#initalizing image
csgoCharacter = cv2.imread("csgoT.png", cv2.IMREAD_COLOR)

#DRAWING LINES
#(img, start, end, color)
cv2.line(csgoCharacter, (0, 0), (150, 150), (255, 0, 0))

cv2.imshow('CSGO Terrorist', csgoCharacter)

cv2.waitKey(0)

cv2.destroyAllWindows()

cv2.imwrite('csgoTWithLine.png', csgoCharacter)

#DRAWING RECTANGLES
#(img, start corner, end corner, color, thickness)
cv2.rectangle(csgoCharacter, (0, 0), (50, 50), (255, 0, 0), 15)

cv2.imshow('CSGO Terrorist With Rectangle', csgoCharacter)

cv2.waitKey(0)

cv2.destroyAllWindows()

cv2.imwrite('csgoTWithBox.png', csgoCharacter)

#DRAWING CIRCLES
#(img, center, radius, color, thickness)
cv2.circle(csgoCharacter, (50, 50), 10, (0, 255, 0), 10)

cv2.imshow('CSGO Terrorist With Circle', csgoCharacter)

cv2.waitKey(0)

cv2.destroyAllWindows()

cv2.imwrite('csgoTWithCircle.png', csgoCharacter)

#DRAWING POLYGONS
polygonPoints = np.array([[10, 5],[20, 30],[70, 20],[50, 10]], np.int32)

#(img, points, closed?, color, thickness)
cv2.polylines(csgoCharacter, [polygonPoints], True, (0, 255, 255), 5)

cv2.imshow('CSGO Terrorist With Polygon', csgoCharacter)

cv2.waitKey(0)

cv2.destroyAllWindows()

cv2.imwrite('csgoTWithpolygon.png', csgoCharacter)

#TEXT
font = cv2.FONT_HERSHEY_SIMPLEX

#(img, text, start, font, size, color, thickness)
cv2.putText(csgoCharacter, "Hello World From Terrorist", (0, 130), font, 5 ,(0, 255, 0), 2, cv2.LINE_AA)

cv2.imshow('CSGO Terrorist Talking', csgoCharacter)

cv2.waitKey(0)

cv2.destroyAllWindows()

cv2.imwrite('csgoTWithSayingHey.png', csgoCharacter)
