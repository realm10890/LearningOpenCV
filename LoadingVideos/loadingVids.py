import cv2
import numpy as np

cap = cv2.VideoCapture(0)
#writing video to save
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output4.mp4', fourcc, 20.0, (640, 480))

while True:
    #ret return true or false if true then will be displayed
    #setting frame equal to the cap variable that captures the video
    ret, frame = cap.read()

    #modifying Video
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #Write it
    out.write(frame)

    #Showing modified Video
    cv2.imshow('gray', gray)

    #showing actual video
    cv2.imshow('video of me', frame)

    #finding way out of capturing video
    if cv2.waitKey(1) & 0xFF == ord('q'):

        #breaks while loop
        break


cap.release()

#releasing saving Video
out.release()

#destroys the windows that video is being displayed in
cv2.destroyAllWindows()
