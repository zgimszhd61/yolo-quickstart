# https://colab.research.google.com/drive/1eGT7Z_Yqr3fObBAXGk0uP-L38K6jtqew#scrollTo=aphK6oCf8xY
# !pip install torch torchvision
# !pip install ultralytics
import torch
from ultralytics import YOLO
from PIL import Image

# Load a pretrained YOLOv8n model
model = YOLO('yolov8n.pt')

# Run inference on an image
results = model('image.jpg')  # list of 1 Results object
# Show the results
for r in results:
    im_array = r.plot()  # plot a BGR numpy array of predictions
    im = Image.fromarray(im_array[..., ::-1])  # RGB PIL image
    im.show()  # show image
    im.save('results.jpg')  # save image
# results.save('results.jpg')  # save image
