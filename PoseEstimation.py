import cv2 
import mediapipe as mp
import time

path = 'sample-mp4-file.mp4'
cap = cv2.VideoCapture(path)
pTime = 0

mpPose = mp.solutions.pose
pose = mpPose.Pose(static_image_mode = False,
                    upper_body_only = False,
                    )

while True:
    success, img = cap.read()

    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = pose.process(imgRGB)
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    cv2.imshow("Image", img)

    cv2.waitKey(5)