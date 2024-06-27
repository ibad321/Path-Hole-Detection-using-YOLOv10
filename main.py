import cv2
from ultralytics import YOLOv10
import pandas as pd
import cvzone

model = YOLOv10("best.pt")

# Function to handle mouse events
def RGB(event, x, y, flags, param):
    if event == cv2.EVENT_MOUSEMOVE:
        point = [x, y]
        print(point)

# Open a window for displaying video frames
cv2.namedWindow('RGB')
cv2.setMouseCallback('RGB', RGB)

# Open the video file
cap = cv2.VideoCapture('demo.mp4')

# Read class names from a file (assuming coco1.txt contains class names)
my_file = open("coco1.txt", "r")
data = my_file.read()
class_list = data.split("\n")

count = 0
while True:
    ret, frame = cap.read()
    count += 1
    if count % 3 != 0:
        continue
    if not ret:
        break
    frame = cv2.resize(frame, (1020, 600))

    # Use the YOLOv10 model to predict on the frame
    results = model(frame)
    
    # Extract bounding boxes and their respective data
    a = results[0].boxes.data
    px = pd.DataFrame(a).astype("float")

    for index, row in px.iterrows():
        x1 = int(row[0])
        y1 = int(row[1])
        x2 = int(row[2])
        y2 = int(row[3])
        confidence = row[4]  # Confidence score
        d = int(row[5])
        c = class_list[d]
        
        # Draw rectangle around the detected object
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        
        # Display class name and confidence score
        text = f'{c}: {confidence:.2f}'
        cvzone.putTextRect(frame, text, (x1, y1), 1, 1)

    # Show the frame in the 'RGB' window
    cv2.imshow("RGB", frame)
    
    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release video capture and close all windows
cap.release()
cv2.destroyAllWindows()
