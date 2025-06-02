import torch
import sys
import os

# Add YOLOv9 root directory to the Python path
sys.path.append('/CV/yolov9')

from models.yolo import Model  # This must match your model file
from utils.torch_utils import select_device

# Load model architecture
cfg_path = '/CV/yolov9/models/detect/yolov9-c.yaml'
model = Model(cfg_path, ch=3, nc=80)  # Adjust `nc` to your number of classes

# Load pretrained weights
ckpt_path = '/CV/yolov9/weights/yolov9-c.pt'
ckpt = torch.load(ckpt_path, map_location='cpu')
model.load_state_dict(ckpt['model'].float().state_dict(), strict=False)

# unfreeze all layers first
for param in model.parameters():
    param.requires_grad = True
