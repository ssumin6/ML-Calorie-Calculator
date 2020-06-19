import os

'''
For future custom, 
change line 12, 14, 17, 20, 21 for your dataset setting. 
'''

# folders are subdirectories inside main_folder.
# folders = ['000','002','003','005','007','012','021','026','028','036','044', \
        # '057','074','084','086','097','105','112','113','114', '888', '099']

folders = [i for i in range(20)]+['888','099']

labels = [0, 2, 3, 5, 7, 12, 21, 26, 28, 36, 44, 57, 74, 84, 86, 97, 105, 112, 113, 114, 120]

# main folder is whether 'train' or 'validation'
main_folder = 'train'
# main_folder = 'validation'

image_width = 256
image_height = 256

'''
Annotation of BBox-Label looks like this 
[# of bounding box]
[top left x] [top left y] [bottom right x] [bottom right y] [label]
All of this number is represented in integer.(0<x<image_width and 0<y<image_height)

Annotation of Yolov3 should be
[label] [center_x] [center_y] [bounding box width] [bounding box height]
Excluding label, all values should be float between 0<value<1.

'''

for folder in folders:
    path = os.path.join(os.path.join("../Downloads/dataset", main_folder), folder)
    print("path %s start" %path)
    for file in os.listdir(path):
        
        if file.endswith(".txt"):
            file_path = os.path.join(path, file)
            f = open(file_path, 'r')
            num = int(f.readline().strip())
            lines = []

            for i in range(num):
                tmp = f.readline().strip().split(" ")
                # tmp [label, topleftX, topleftY, bottom X, bottom Y]
                tmp = list(map(int, tmp))

                center_x = ((tmp[1]+tmp[3])/2)/image_width
                center_y = ((tmp[2]+tmp[4])/2)/image_height

                width = (tmp[3] - tmp[1])/image_width
                height = (tmp[2] - tmp[4])/image_height
                tmp2 = "%d %0.6f %0.6f %0.6f %0.6f" %(labels.index(tmp[0]), center_x, center_y, width, height)
                lines.append(tmp2)
            f.close()

            f = open(file_path, 'w')
            f.write("\n".join(lines))
            f.close()



