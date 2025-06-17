#!/bin/bash

DATA="new_data/seaships.yaml"
BATCH=8
CONF=0.001
DEVICE=0
WEIGHTS="./runs/train/OBS_50/weights/best.pt"
TASK="test"

mkdir -p logs

echo "Starting batch evaluation..." > logs/output_c.log
echo "============================" >> logs/output_c.log

for IOU in 0.95 0.9 0.8 0.7 0.6 0.5
do
    OUT_NAME="Yolov9C-IOU_${IOU//./_}"
    echo "Running IoU=$IOU..." | tee -a logs/output_c.log
    time python val.py \
        --data "$DATA" \
        --batch "$BATCH" \
        --conf "$CONF" \
        --iou "$IOU" \
        --device "$DEVICE" \
        --weights "$WEIGHTS" \
        --name "$OUT_NAME" \
        --task "$TASK" \
        >> logs/output_c.log 2>> logs/error_c.log
    echo "Finished IoU=$IOU" | tee -a logs/output_c.log
done

echo "All evaluations complete." | tee -a logs/output_c.log
