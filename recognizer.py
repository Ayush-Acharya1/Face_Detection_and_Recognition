import cv2
from simple_facerec import SimpleFacerec
sfr=SimpleFacerec()
sfr.load_encoding_images("./images/")

cap=cv2.VideoCapture(0)

while True:
    ok,frame=cap.read()

    face_loc,face_names=sfr.detect_known_faces(frame)
  #if face_names:
   #     print("attendance marked")
    


    for loc,names in zip(face_loc,face_names):
        y1,x2,y2,x1=loc[0],loc[1],loc[2],loc[3]
        cv2.putText(frame,names,(x1,y1-10),cv2.FONT_HERSHEY_DUPLEX,1,(0,0,255),2)
        cv2.rectangle(frame,(x1,y1),(x2,y2),(0,0,255),4)



    cv2.imshow("Frame",frame)
    key=cv2.waitKey(1) & 0xFF
    if key==27:
        break
cap.release()
cv2.destroyAllWindows()