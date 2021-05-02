import cv2 
import mediapipe as mp
import time

path = 'sample-mp4-file.mp4'
cap = cv2.VideoCapture(path)
pTime = 0


mpDraw = mp.solutions.drawing_utils
mpPose = mp.solutions.pose
pose = mpPose.Pose(static_image_mode = False,
                    upper_body_only = False,
                    )



while True:
    success, img = cap.read()

    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = pose.process(imgRGB)
    print(results.pose_landmarks)
    if results.pose_landmarks:
        mpDraw.draw_landmarks(img, results.pose_landmarks, mpPose.POSE_CONNECTIONS)
        for id, lm in enumerate(results.pose_landmarks.landmark):
            h, w, c = img.shape
            print(id, lm)
            cx, cy = int(lm.x * w), int(lm.y * h) #conerting lm.x that is a ratio to coordinates
            cv2.circle(img, (cx,cy), 10, (255,0,0), cv2.FILLED)


    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    cv2.imshow("Image", img)

    cv2.waitKey(5)