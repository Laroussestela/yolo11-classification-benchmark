from ultralytics import YOLO

# Load a model
model = YOLO("yolo11n-cls.pt")

# Train the model
results = model.train(data="E:/00. Kaggle/18. Clasification Inception/Yolo/dataset", 
                      epochs=500, 
                      patience=5,
                      imgsz=64)
