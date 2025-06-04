#!/bin/bash


unzip *.zip -d . 

# move the python files to the respective folders.
mv ./move_image.py ./JPEGImages/
mv ./move_xml.py ./Annotations/
mv ./xmltotxt.py ./Annotations/

python ./JPEGImages/move_image.py
python ./Annotations/move_xml.py
python ./Annotations/xmltotxt.py
