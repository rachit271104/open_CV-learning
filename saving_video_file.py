import cv2

# we learn how to sace a video file here
camera=cv2.VideoCapture(0)

frame_width=int(camera.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height=int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT))

codec= cv2.VideoWriter_fourcc(*'XVID')
recorder = cv2.VideoWriter("my_video.mp4",codec,30,(frame_width,frame_height))

while True:
    success,image=camera.read()

    if not success:
        print("not saving")
        break
    recorder.write(image)
    cv2.imshow("recorder_video",image)

    if cv2.waitKey(1) & 0xFF == ord('q'):
       break

camera.release()
recorder.relese()
cv2.destroyAllWindows()