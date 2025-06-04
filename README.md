# YOLOv9

## Installation and Files Setup
The current instructions are for an ubuntu based system. 
``` shell
# Go to a clean folder and start installations
git clone https://github.com/Bot736382/yolov9_special_course.git

cd yolov9_special_course

# In the same repository, install the Dockerfile (This is already in the main repo.)
mv Dockerfile ..

cd ..
```
Once this is done, start building the docker container as follows:
``` shell
# BUILD THE IMAGE
docker build -t yolov9-image .

# RUN THE CONTAINER
nvidia-docker run --gpus all -it \
  -p 8888:8888 -p 6006:6006 \
  -v ./yolov9_special_course:/yolov9 \
  --shm-size=64g \
  --name yolov9-container yolov9-image
```

Models (Unfreezed, directly taken from the [source directory](https://github.com/WongKinYiu/yolov9.git)): 
[`yolov9-t-converted.pt`](https://github.com/WongKinYiu/yolov9/releases/download/v0.1/yolov9-t-converted.pt) [`yolov9-s-converted.pt`](https://github.com/WongKinYiu/yolov9/releases/download/v0.1/yolov9-s-converted.pt) [`yolov9-m-converted.pt`](https://github.com/WongKinYiu/yolov9/releases/download/v0.1/yolov9-m-converted.pt) [`yolov9-c-converted.pt`](https://github.com/WongKinYiu/yolov9/releases/download/v0.1/yolov9-c-converted.pt) [`yolov9-e-converted.pt`](https://github.com/WongKinYiu/yolov9/releases/download/v0.1/yolov9-e-converted.pt) [`yolov9-s.pt`](https://github.com/WongKinYiu/yolov9/releases/download/v0.1/yolov9-s.pt) [`yolov9-m.pt`](https://github.com/WongKinYiu/yolov9/releases/download/v0.1/yolov9-m.pt) [`yolov9-c.pt`](https://github.com/WongKinYiu/yolov9/releases/download/v0.1/yolov9-c.pt) [`yolov9-e.pt`](https://github.com/WongKinYiu/yolov9/releases/download/v0.1/yolov9-e.pt) 
[`gelan-s.pt`](https://github.com/WongKinYiu/yolov9/releases/download/v0.1/gelan-s.pt) [`gelan-m.pt`](https://github.com/WongKinYiu/yolov9/releases/download/v0.1/gelan-m.pt) [`gelan-c.pt`](https://github.com/WongKinYiu/yolov9/releases/download/v0.1/gelan-c.pt) [`gelan-e.pt`](https://github.com/WongKinYiu/yolov9/releases/download/v0.1/gelan-e.pt)

Install these Models into the ``./weights/`` folder within the system and use Model_unfreezing.ipynb to unfreeze the weights. (Normally, models are frozen after training)

## Training

## Validation
