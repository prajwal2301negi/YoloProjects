# Loading our model
from ultralytics import YOLO

model = YOLO('')

results = model('/content/cars2.mp4', show = True, save = True)