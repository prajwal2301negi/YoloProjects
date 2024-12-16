from ultralytics import YOLO
import cv2

model = YOLO(r'C:\Users\prajwal\OneDrive\Desktop\New folder (2)\yolo11l-pose.pt')

cap = cv2.VideoCapture(0)  

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame)

    output_frame = results[0].plot()  

    cv2.imshow('Pose Detection', output_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
