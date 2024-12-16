# from ultralytics import YOLO

# model = YOLO('yolov8l-pose.pt')  # load a pretrained model (recommended for training)

# model.train(data='config.yaml', epochs=10, imgsz=640)


from ultralytics import YOLO

# Load a model
model = YOLO("yolo11l-pose.pt")  # load a pretrained model (recommended for training)


# Train the model
results = model.train(data="coco8-pose.yaml", epochs=1, imgsz=640)

