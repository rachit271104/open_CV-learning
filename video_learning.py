# in this we learn video capturing and manipulation 
import cv2

# video capturing 
cap = cv2.VideoCapture(0)  # 0 means ki laptop k cam se , 1 means external jo connect h uss se 

while True:
    ret, frame =cap.read()
    if not ret:
        print("web cam not working")
        break
    cv2.imshow("web cam feed", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("quitting")
        break

cap.release()
cv2.destroyAllWindows()