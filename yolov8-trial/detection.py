import cv2
from ultralytics import YOLO
import numpy as np

cap = cv2.VideoCapture("pedestrian.mp4")

model = YOLO('yolov8m.pt')

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame, device='mps')
    result = results[0]
 
    boxes = result.boxes.xyxy.cpu().numpy().astype(np.int64)
    classes = result.boxes.cls.cpu().numpy().astype(np.int64)
    confs = result.boxes.conf.cpu().numpy()

    for box, cls, conf in zip(boxes, classes, confs):
        x1, y1, x2, y2 = box
        label = f"{model.names[cls]} {conf:.2f}"
        
    
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        
        cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)


    cv2.imshow("Img", frame)
    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
