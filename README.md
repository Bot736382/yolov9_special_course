# YOLOv9

## Installation and Files Setup
The current instructions are for an ubuntu based system. 
``` shell
# Go to a clean folder and start installations
git clone https://github.com/Bot736382/yolov9_special_course.git

mv ./yolov9_special_course/Dockerfile ./
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

Install the Models: yolov9-c-converted, yolov9-t-converted and the [SeaShips Dataset](http://www.lmars.whu.edu.cn/prof_web/shaozhenfeng/datasets/SeaShips%287000%29.zip)
```
wget https://github.com/WongKinYiu/yolov9/releases/download/v0.1/yolov9-c-converted.pt -O ./yolov9_special_course/weights/yolov9-c-converted.pt

wget https://github.com/WongKinYiu/yolov9/releases/download/v0.1/yolov9-t-converted.pt -O ./yolov9_special_course/weights/yolov9-t.pt

wget http://www.lmars.whu.edu.cn/prof_web/shaozhenfeng/datasets/SeaShips%287000%29.zip -O ./yolov9_special_course/new_data/Seaships.zip 
```



# TO DO
Format the dataset to install it on the cluster
Add the weights to the dockerfile installation
Unfreeze the weights 
#

## Training a Model on New Datasets
### Dataset Setup
Before initiating training yolov9 on new datasets, one must download the models from the [yolov9 original repository](https://github.com/WongKinYiu/yolov9). For the given tutorial, the author will be using the yolov9-c.pt model for retraining the parameters. 

Required image file structure:
### change the image to a better readme compatible filetype



### Retraining
We start of by running this. The new_data folder is basically a combination of the SeaShips dataset as can be found on: [SeaShips](http://www.lmars.whu.edu.cn/prof_web/shaozhenfeng/datasets/SeaShips%287000%29.zip)
``` shell
python train_dual.py --workers 4 --device 0 --batch 8 --data new_data/seaships.yaml --cfg models/detect/yolov9-c.yaml --weights './weights/yolov9-c.pt' --name train2_new --min-items 0 --epochs 50 --close-mosaic 15
```
Once the model has been retrained, it is stored as ./runs/train/train2_new/best.pt. 

### Evaluation
This new model can be evaluated by:
``` shell
python val.py --data new_data/seaships.yaml --batch 2 --conf 0.001 --iou 0.7 --device 0 --weights './runs/train/OBS_10/weights/best.pt' --save-json --name OBS_10_eval
```
## Citations
