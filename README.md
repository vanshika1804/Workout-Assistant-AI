# Artificial Intelligence supported Personal Workout Assistant

## Introduction
The movement of various muscles and joints in continuous synchronization across the body is extremely essential when it comes to successful sprint over long distances. Understanding of biomechanical factors in successful workout is useful because of their critical value to performance. At the beginning of a successful rep, it is important to produce great force/ power and generate high velocity in the block and acceleration phases. During the constant-speed phase, the events immediately before and during the braking phase are important in increasing explosive force/power and efficiency of movement in the propulsion phase. All of the aforementioned factors can be easily analysed using the various joints and muscle movements across the body of the athelete.

## Background
With the current realities due to the pandemic it is not possible to go to communtiy spaces for workout such as gyms, workout training classses, etc. And hence most people end up with injuries due to improper wotkout workout sessions. We’ve seen plenty of accidents happen at the gym—barbells to the windpipe, kettlebells to the nether regions, and whatever the hell this guy was doing on the cable machine. And every runner knows just how dangerous a stray dog or a surprise swarm of hornets can be.
Hence to avoid such instances AI based personal workout support application is necessary. This software can be embedded in mirrors for taking input and simultaneously counting reps, suggesting exercises, and telling pose corrections.

The following news articles confirms such happenings accross the country at a regular basis:
 * https://www.indiatvnews.com/amp/lifestyle/news-22-year-old-dell-techie-andhra-pradesh-dies-while-working-out-in-gym-how-to-prevent-accidents-at-gym-391149
 * https://www.timesnownews.com/amp/health/article/24-year-old-dies-while-running-on-treadmill-in-noida-precautions-you-must-take-before-hitting-the-gym/496108
 * https://wap.business-standard.com/article-amp/pti-stories/man-dies-of-heart-attack-while-working-out-in-gym-120031301442_1.html


## Data Format
The target of the project is to design and create a solution that can evaluate the workout quality of an individual in a short period of time and can be done without attaching any extra equipments (like ECG monitors) to the body. 

For achieving the same, live video feed while workoing out would be most effective. While the software would suggest personalised effective workout plans, count the number of reps and suggest corrections in the position.

## Methodology
The methodology for the project is explained as follows:
* Live video ffed is input while the person is working out.
* The video is divided into various still frames for analysis
* Each still frame is taken into consideration, one-by-one and a pose detection algorithm is run on it
* The pose detection algorithm finds the various joints of the body as landmarks and returns their locations as X and Y Coordinates

<img src="https://github.com/adityakumar2809/SprintAnalysis/blob/master/info/pose_tracking_full_body_landmarks.png" alt="Landmarks Across the Body" width="600px" />

<img src="https://github.com/adityakumar2809/SprintAnalysis/blob/master/info/PoseDetection.jpg" alt="Detected Landmarks" width="300px" />

* Using three consecutive joints as points and cosine rule as a mathematical tool, the angle formed by the middle joint is represented (Right Shoulder, Right Elbow, Right Wrist gives the angle formed at the Right Elbow)

![Angle formed at a Joint](https://github.com/adityakumar2809/SprintAnalysis/blob/master/info/JointAngle.jpg)


* These angles are continuously recorded with time and its values are recorded
* Smoothening functions are utilized to smoothen any noise found in the angles obtained

<img src="https://github.com/adityakumar2809/SprintAnalysis/blob/master/info/GraphSmoothening.png" alt="Graph Smoothening" width="500px" />

* The resulting data is then superimposed with the data of trained atheletes to the the offset

<img src="https://github.com/adityakumar2809/SprintAnalysis/blob/master/info/LiveRunning.png" alt="LiveRunning" width="500px" />

* If the offset is within the given threshold, the person is doing good, else modifications in the position are suggested and number of reps is displayed on the screen.

## Inferences
The data obtained after successful analysis for various joints and muscles across the body yields enough evidence to make a calculated estimate as to whether the  postion is correct or not.

![Joint Analysis](https://github.com/adityakumar2809/SprintAnalysis/blob/master/info/Result.png)

It involves no physical connection to the body and there is no time required to set it up, hence can be easily configured, even at a remote location. All this can ease the process of screening extremely easy for the physically challenging events people are willing to participate in  
