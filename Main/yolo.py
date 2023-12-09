
import cv2
from ultralytics import YOLO
import json
from datetime import datetime
import pymongo
import time
import CameraSettings
myclient=pymongo.MongoClient("mongodb://localhost:27017/")
db=myclient["capstone"]
col=db["camera_log"]
url='http://192.168.137.78'
video_path = url+":81/stream"
CameraSettings.setCamera(url)
# Load the YOLOv8 model
model = YOLO('yolov8s.pt')
# Open the video file
cap = cv2.VideoCapture(video_path)
# fps = int(cap.get(cv2.CAP_PROP_FPS))
pTime=0
cTime=0
# Loop through the video frames
while cap.isOpened():
    # Read a frame from the video
    success, frame = cap.read()

    if success:
        # Run YOLOv8 inference on the frame
        frame=cv2.rotate(frame, cv2.ROTATE_90_COUNTERCLOCKWISE)
        results = model(frame, classes=list(range(1, 81)),imgsz=320, conf=0.6) #,conf=0.6qq


        # Visualize the results on the frame
        annotated_frame = results[0].plot()

        #Calculate the fps of results
        cTime=time.time()
        fps=1/(cTime-pTime)
        pTime=cTime

        # Display the annotated frame
        cv2.putText(annotated_frame,str(int(fps)),(10,70),cv2.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
        cv2.imshow("YOLOv8 Inference", annotated_frame)
        #Convert result to JSON Format
        r=results[0].tojson()
        lst = json.loads(r)
        if lst :
            x=col.insert_many(lst)
       ## To save in text file
        # for r in results:
            
            # lst=r.tojson() #convert r object in list of results into JSON
            # y=json.loads(lst) # load the Json object to work with it which is also a list

            # for l in y: #List of dictionaries
            #     # print(l)
            #     # print(l["name"],l["confidence"])
            #     # print(l["name"])
            #     with open('log.csv', 'a') as f:
            #         line=l["name"]+","+str(l["class"])+","+str(l["confidence"])+","+datetime.now().strftime("%H:%M:%S")
            #         f.write(line+"\n")
            # r.save_crop('Saved_Crops')
            # r.save_txt('log.csv',save_conf=True)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        # Break the loop if the end of the video is reached
        break

# Release the video capture object and close the display window
cap.release()
cv2.destroyAllWindows()
