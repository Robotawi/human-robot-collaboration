# Human-robot Collaborative Assembly
This is the second part of my study on the Human-Robot collaborative assembly. The first part is described [here](https://github.com/Robotawi/constrained_motion_planning) without deep technicalities. The first part developed a method to enhance the robot capabilities of manipulating heavy objects.

## The big picture
The aim of the human-robot collaborative assembly framework is to make assembly tasks less physically requiring for the humans. The robot is expected to manipulate heavy objects with an improved capability, while the human will focus on the fine tasks like screwing, and aligning the assembly parts. For example, the human and his robot assistant will assemble the following cabinet together.
<img src=./project_images/cabinet.png>

## Handovers planning
This second part develops a module to plan robot-to-human handover poses that are both comfortable for the human, and reachable for the robot. The process happens in the flow described by the next figure and its implementation is in the file [sample_step4_calculate_handover_pose.py](./sample_step4_calculate_handover_pose.py).
<img src=./project_images/goalselectionsequence2.png>

## The planning steps:
The specific goal of every sub task in the assembly process is take a single workpiece (board in the above cabinet) and plan a handover pose for it. Here are the details how the handover pose is decided:


### Step (1)
The story of the planning starts with knowing how the final assembly is like, and hence the pose of every work piece in this assembly. Let’s take the **side board**, highlighted in yellow in the above figure, as an example. 

### Step (2)
The candidate poses for the handover are sampled and distributed with respect to the assembly pose (shown in yellow) of the target workpiece. The samples are shown in grey in the above figure. 

### Step (3)
The samples are checked for being both reachable, and comfortable to the human. The reachability is decided using inverse kinematics, and the comfortableness is estimated using the inverse of the condition number of the human arm (similar in principle to the manipulability defined by Yoshikawa sensei). The set of reachable, comfortable poses are shown in orange. 


### Step (4)
The set of the human reachable, comfortable poses are then tested for being reachable to the robot. In deed, a check for shared grasps for dual-arm manipulation is carried out here (have a look below for a bit more of details). The subset of poses that are inverse kinematics (IK) feasible as well as human comfortable is shown in dark orange.

### Step (5)
The satisfactory poses from the previous step are ranked according to the distance from the target assembly pose. The nearest comfortable pose is selected to be the handover pose for the subtask. The selected pose is shown in red with the approximated human grasp and the exact robot grasp.

## Would like some interesting details?
For a bit of the internals of the above described flows, the predefined robot and human poses for one of the objects are shown. If we break it down, then the above inverse kinematics check is to find some hands (robot, and human) that are connectable to the arms at each pose of the workpieces.
<img src=./project_images/predefined_grasps.png>

* **How is the dual-arm (robot-to-robot) handover decided?**

For this we need to find some shared grasps at two different poses of the object. This comes within the above-mentioned fourth step. The green arm below indicates a shared grasp at two different handover poses. The start pose is in blue and the goal pose is in red.
<img src=./project_images/startgoalsharedgrasp2.png>

* **How to connect a robot-to-robot handover and robot-to-human handover to get the task done?**

As I mentioned above, there is a need for a shared grasp at two different poses. The first of those poses is the robot-to-robot handover, and the second is the robot-to-human handover. If we connect this knowledge to the criteria based on which the human-to-robot handover is selected (the steps), it would appear as follows. This is the whole lovely story! 
<img src=./project_images/human_robot_shared.png>

## Practical result for next-generation manufacturing
The result of this module is given to the [motion planning module]() to generate the robot motion that takes the object from the table to the handover pose. The knowledge of the object poses is calculated by [this]() vision module. The following is the result of fully assembling a cabinet with the described approach.

[![Human-Robot Collaborative assembly](./project_images/vid_cover.png)](https://www.youtube.com/watch?t=24s&v=t_-89-N_RgM)

The details of this project are published in the journal of Transactions on Automation Science and Engineering. Here is a link to [the paper](https://ieeexplore.ieee.org/document/9044335).


## Contact
If you are interested in the presented work/ideas, or if you have any questions, feel free to connect with me on [LinkedIn](https://www.linkedin.com/in/mohraess). We can disuss about this project and other interesting projects.

