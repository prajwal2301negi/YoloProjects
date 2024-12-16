from ultralytics import YOLO

model = YOLO('')

model.export(format = 'onnx')