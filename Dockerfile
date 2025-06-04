# GET THE CONTAINER FROM NVCR.IO. YOLOv9 USES pytorch:21.11 by NVIDIA
FROM nvcr.io/nvidia/pytorch:21.11-py3

# Since installations will cause interactions, set installations to non interactive and default by nature
ENV DEBIAN_FRONTEND=noninteractive

# Apt update the repository and install the following tools including curl, gedit, nano
RUN apt update && apt install -y \
    zip htop screen libgl1-mesa-glx git nano gedit curl \
    && apt clean && rm -rf /var/lib/apt/lists/*

RUN pip install \
    seaborn thop Pillow==9.5.0
    
# Change the working directory to YOLOv9
WORKDIR /yolov9 

RUN wget https://github.com/WongKinYiu/yolov9/releases/download/v0.1/yolov9-c-converted.pt \
    -O ./weights/yolov9-c-converted.pt

RUN wget https://github.com/WongKinYiu/yolov9/releases/download/v0.1/yolov9-t-converted.pt \
    -O ./weights/yolov9-t.pt

RUN wget http://www.lmars.whu.edu.cn/prof_web/shaozhenfeng/datasets/SeaShips%287000%29.zip \
    -O ./new_data/Seaships.zip 

COPY yolov9_special_course /yolov9

RUN mkdir -p /yolov9/coco

# RUN pip install --requirement requirements.txt

EXPOSE 8888 6006

CMD ["/bin/bash"]
