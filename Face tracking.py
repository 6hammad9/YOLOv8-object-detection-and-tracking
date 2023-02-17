# -*- coding: utf-8 -*-
"""Untitled3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1UZO4HYigncOirr-_WqJ1NxzJmkjHIOe9
"""
#---------------------------------------------------------Hammad Naseer-------------------

!nvidia-smi

import os
Home=os.getcwd()
print(Home)
from PIL import Image

!pip install ultralytics

from IPython import display 
display.clear_output()
!yolo mode*checks

from ultralytics import YOLO

from IPython.display import display, Image

!pip install roboflow

from roboflow import Roboflow
rf = Roboflow(api_key="zevcoEtrBk9labeRvnWz")
project = rf.workspace("hammad-hj1ch").project("biden")
dataset = project.version(2).download("yolov8")

model = YOLO("yolov8n.yaml")  # build a new model from scratch
model = YOLO("yolov8n.pt")  # load a pretrained model (recommended for training)

# Train the model
model.train(data="/content/Biden-2/data.yaml", epochs=100, imgsz=640)



model = YOLO("yolov8n.pt")  # load an official model
model = YOLO("/content/runs/detect/train9/weights/best.pt")  # load a custom model

# Validate the model
metrics = model.val()  # no arguments needed, dataset and settings remembered
metrics.box.map    # map50-95
metrics.box.map50  # map50
metrics.box.map75  # map75
metrics.box.maps   # a list contains map50-95 of each category

# Run the model and generate the output frames
results = model.predict(source="bden.mp4", save=True)

# for result in results:
#     # detection
#     result.boxes.xyxy   # box with xyxy format, (N, 4)
#     result.boxes.xywh   # box with xywh format, (N, 4)
#     result.boxes.xyxyn  # box with xyxy format but normalized, (N, 4)
#     result.boxes.xywhn  # box with xywh format but normalized, (N, 4)
#     result.boxes.conf   # confidence score, (N, 1)
#     result.boxes.cls    # cls, (N, 1)


