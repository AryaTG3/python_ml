#import open cv librry
import cv2
#difine a videocapture objet
vid=cv2.VideoCapture(0) #0 port number
while True:
    ret,frame = vid.read()#read fuction gives 2 out puts key and image
    image=cv2.putText(frame, "welcome to AI class",(50,50), cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),2,cv2.LINE_AA)
    cv2.imshow("frame", image)
    if cv2.waitKey(1) & 0xFF == ord('q'):# it stops when we presss the key q
        break

vid.release()
cv2.destroyAllWindows()
