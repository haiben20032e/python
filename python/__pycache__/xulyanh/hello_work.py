import cv2
vid_capture = cv2.VideoCapture(0)
vid_cod = cv2.VideoWriter_fourcc(*'XVID')
output= cv2.VideoWriter("E:\cam_video.mp4",vid_cod,20.0,(640,480))
while(True):
    ret,frame = vid_capture.read()
    cv2.imshow( "my cam video",frame)
    output.write(frame)
    if cv2.waitKey(1) &0XFF == ord('x'):
        break
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

vid_capture.release()
output.release()
cv2.destroyAllwindows()
    