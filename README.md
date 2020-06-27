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

We mainly used [2]'s code for training yolov3 model for our custom dataset. It was helpful to debug the possible problems we had. 
Our team use [1]'s code for web processing. So code included here is [1]'s source not [2]'s.

setting
- used 2 GPU. 
- CuDNN=1

You could reproduce our result by following command.

First, go to the model_web/ directory and make the darknet object.
git clone
cd model_web
make

For individual image processing.
./darknet detector test data/food.data cfg/yolov3-tiny_obj.cfg final.weights {image_path}

Reference
 [1] https://github.com/pjreddie/darknet
 [2] https://github.com/AlexeyAB/darknet

## Web Application
Create a web server for real-time calorie detector using python flask. 
We changed [1]'s code suitable for our project setting.

Reference 
 [1] https://github.com/neltia/flask-project
