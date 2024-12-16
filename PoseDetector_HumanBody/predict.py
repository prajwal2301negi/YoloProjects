from ultralytics import YOLO
import cv2

# Load the trained model
model = YOLO(r'C:\Users\prajwal\OneDrive\Desktop\New folder (2)\yolo11l-pose.pt')

# Predict on the image
results = model(r"C:\Users\prajwal\Downloads\humanFace\8.jpeg")

# print(results)
output_image = results[0].plot()  

cv2.imwrite('./output.png', output_image)  

