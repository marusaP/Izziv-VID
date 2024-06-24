import os
from ultralytics import YOLO
import cv2

folder = 'C:\\Users\\Marusa\\Documents\\Faks MAG 1\\VID (Robotski vid)\\Izziv_VID\\test3'

# Load a model
model = YOLO("C:\\Users\\Marusa\\Documents\\Faks MAG 1\\VID (Robotski vid)\\runs\\detect\\train4\\weights\\last.pt")  # load a custom model

threshold = 0.5

for filename in os.listdir(folder):
    img = cv2.imread(os.path.join(folder,filename))

    results = model(img)

    for result in results[0].boxes.data.tolist():
        x1, y1, x2, y2, score, class_id = result

        if score > threshold:
            cv2.rectangle(img, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 4)
            cv2.putText(img, results[0].names[int(class_id)].upper(), (int(x1), int(y1 - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)

    cv2.imshow('image', img)
    cv2.waitKey(0)
