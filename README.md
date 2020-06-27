# ITM_project
ITM Object Detection project : Calculate Food Calorie

## DATA Preprocessing 
Our team created an Object Detection dataset based on Classification dataset, "FoodDataSet"[1]
We modified convert.py and config.py from [1] to save .jpg from huge .bin files for selected 21 labels.
Our team member Jimin Koo hand crafted bounding box by using [2].

bound_process.py is used for specific annotation setting for yolov3. 
BBox-Label Tool[2] and yolov3 have different annotation for bounding box, so we have to change every annotation file.

All codes used in preprocessing is in /preprocess.

setting
- Tensorflow 1

Reference
[1] https://github.com/corona10/FoodDataSet
[2] https://github.com/jxgu1016/BBox-Label-Tool-Multi-Class

## Model Training
YOLOv3-tiny.

setting
- used 2 GPU. 
- CuDNN=1

Reference
[1] 

## Web Application
