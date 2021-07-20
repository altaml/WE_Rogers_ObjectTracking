# WE Accelerate Project
usecase - Players and puck detection and tracking in the hockey video games.
Client - Rogers


# Description

The specific goal for this repo is data processing for this usecase which inclues two parts:
* converting the video data to a group of frames
* reconstructing the video from a group of frames

The created frames will be used for training and testing our object detection model using machine leaerning later in azure. 
Furthremore, when we are done with object detection in the frames we can put the frames back togeter to reconstruct the video as our final output. 


# Dataset
There are 3 hockey video game provided by rogers which we are going to use 2 of them for training and 1 video for testing.

# Usage
* Either open a terminal and clone the repo in your computer or download the zip of the project and unzip the folder.
```git clone https://github.com/altaml/WE_Rogers_ObjectTracking.git```

* Put all the Rogerst video data in this folder: ``` data/Original Videos ```
* For converting video to frames, first go to the cloned repository root and then run the following command in terminal or run the video2frame.py in any IDE:
```python dataprocessing/video2frame.py ```
This will create the frames of the videos in individual folders in this path: ``` data/Original Frames ```

* After getting the object detection results, please put the folder of frames back in ```Object Detection Results``` folder. Then you can reconstruct the video back by running the follwing command in the root of the repo:
```python dataprocessing/frame2video.py```
