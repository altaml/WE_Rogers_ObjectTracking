
# WE Accelerate Project
* Use Case - Players and puck detection and tracking in hockey video games.
* Client - Rogers


# Description
The specific goal for this repo is data processing for this use case which includes two parts:
* converting the video data to a group of frames
* reconstructing the video from a group of frames


The created frames will be used for training and testing our object detection model using machine learning later in azure. Furthermore, when we are done with object detection in the frames we can put the frames back together to reconstruct the video as our final output.


# Dataset
There are 3 hockey video games provided by rogers which we are going to use 2 of them for training and 1 video for testing.

# Usage
* Either open a terminal and clone the repo in your computer or download the zip of the project and unzip the folder.
```git clone https://github.com/altaml/WE_Rogers_ObjectTracking.git```

* Now you have to go to the project folder by running this command: ```cd WE_Rogers_ObjectTracking```

* Install the requirement libraries by: ```pip install -r requirements.txt```

* Put all the Rogerst video data in this folder: ``` data/Original Videos ```

* For converting video to frames, go to the dataprocessing folder (```cd dataprocessing```) and then run the following command in terminal:
```python video2frame.py --fnumber 2000```. fnumber is showing the gap between the frames that are going to be saved. You can change the value, if you want to have more (decrease fnumber) or less video frams (increase fnumber) to be saved. This will create the frames of the videos in the individual folders in this path: ``` data/Original Frames ```.

* After getting the object detection results, please put the folder of frames in ```Object Detection Results``` folder. Then you can reconstruct the video by running the following command, in the dataprocessing folder (```cd dataprocessing```).
```python frame2video.py --fps 10```. fps is showing the frame per second for creating the video. You can change this number to have faster (increase fps) or slower video (decrease fps). This will create  a new folder called ```Reconstructed Videos``` which will have the reconstructed video there.
