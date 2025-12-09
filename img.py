import cv2
import time
cpt = 0
maxFrames = 30 # cantidad de frames

cap=cv2.VideoCapture(1)

while cpt < maxFrames:
    ret, frame = cap.read()
    frame=cv2.resize(frame,(640,480))
    cv2.imshow("test window", frame) # mostrar imagen
    cv2.imwrite("C:/Users/alexi/Downloads/bebidas/yolov5win11customobj-main/yolov5win11customobj-main/images/Bilz_%d.jpg" %cpt, frame)
    time.sleep(2)
    cpt += 1
    if cv2.waitKey(1)&0xFF==27:
        break
cap.release()
cv2.destroyAllWindows()