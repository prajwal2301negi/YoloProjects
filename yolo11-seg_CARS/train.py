from ultralytics import YOLO

model = YOLO("yolo11x-seg.pt") 

results = model.train(data="coco8-seg.yaml", epochs=100, imgsz=640)