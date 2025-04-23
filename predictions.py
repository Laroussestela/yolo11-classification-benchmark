from ultralytics import YOLO
import numpy as np

# Load a model
model = YOLO("runs/classify/train/weights/best.pt")

# results = model("dataset/val/Bean/0023.jpg")
results = model("dataset/val/Potato/1026.jpg")

names = results[0].names
probs = results[0].probs.data.tolist()

print(names[np.argmax(probs)])
