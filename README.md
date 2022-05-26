# Calorie Calculator with Object Detection Model
Simple web demo of **real-time Calorie Calculator** using Yolov3 Object Detection model. \
[[Youtube Demo]](https://www.youtube.com/watch?v=aUYLaG7vMmk) 

### Environment
- Tensorflow 1
- CuDNN=1

## DATA Preprocessing 
Our team created an Object Detection dataset based on Classification dataset, "FoodDataSet"[1]. It is also available on [Kaggle](https://www.kaggle.com/datasets/jiminkoo/koreanfood-objectdetection-dataset).

**bound_process.py** is used for specific annotation setting for yolov3. 

All codes utilized in preprocessing is located in */preprocess.*

## Model Training
We trained YOLOv3-tiny model for our custom dataset.

Our result demonstrated following result on our custom dataset.
|  | Trained Model |
|--|--|
| mAP | 0.8079 |
| average IOU | 52.09% |

You could reproduce our result by following command.

    git clone https://github.com/ssumin6/ML-Calorie-Calculator.git
    cd model_web
    make

For individual image processing.

    ./darknet detector test data/food.data cfg/yolov3-tiny_obj.cfg final.weights {image_path}


### References
 [1] https://github.com/corona10/FoodDataSet \
 [2] https://github.com/pjreddie/darknet \
 [3] https://github.com/AlexeyAB/darknet \
 [4] https://github.com/neltia/flask-project
