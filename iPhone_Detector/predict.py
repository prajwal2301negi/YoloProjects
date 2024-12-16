from ultralytics import YOLO
import cv2
import numpy as np

model_path = r'C:\Users\prajwal\OneDrive\Desktop\iPhone_Detector\yolov8n-seg.pt'
image_path = r"C:\Users\prajwal\Downloads\iPhone_Detector\test\1.jpeg"

# Loading image
img = cv2.imread(image_path)
H, W, _ = img.shape

# Loading model
model = YOLO(model_path)

# Running model on the image
results = model(img)

# Looping over the results and processing each detected object
for result in results:
    for j, mask in enumerate(result.masks.data):
        # Converting mask to a numpy array and resizing to the original image size
        mask = (mask.numpy() * 255).astype(np.uint8)
        mask = cv2.resize(mask, (W, H))

        # Contours in the mask
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        # Bounding rectangles around each contour in the mask
        for contour in contours:
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)  

# Save the annotated image with bounding rectangles
cv2.imwrite('./output.png', img)
