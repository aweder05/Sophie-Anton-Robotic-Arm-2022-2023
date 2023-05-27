# 2022-2023 DE Engineering 3 - Robotic Cartesian Arm 
## Anton Weder    
## Sophie Chen

##### Table of Contents  
* Project Description
* Link to Project Planning
* Proof of Concept 
   - Openbuilds
* Commented Code
* Problems

## Project Description
Our goal for this project is to create a **working robotic arm** which, when complete, will be able to use **stepper motors** and servos to succesfully move a writing utensil around on paper to write things down. 

## Link to Project Planning
The link to our project planning Google Doc can be found here: [link](https://docs.google.com/document/d/1Sfuq9OfWJm28hZP6IfdwjBN-oqiLh9iVy0cK-eDuprw/edit)

Attached below are early sketches of our project planning:
---
#### Image 1: Overall Sketch

<img src="https://github.com/aweder05/Sophie-Anton-Robotic-Arm-2022-2023/blob/main/media/PorjectPlanning.png?raw=true" width="500" height="500">


###### In the above image is a sketch of what we originally thought was going to be what our project looked like. It looks a bit like a 3D Printer
---
<img src="https://github.com/aweder05/Sophie-Anton-Robotic-Arm-2022-2023/blob/main/media/ProjectPlaning.png?raw=true" width="500">

###### In the above image is a diagram of how we were going to control the up and down pencil movemen on our finished product. Unfortunately, this design was never fully realized, and eventually we opted for something else. 

## Proof of Concept
For our proof of concept, we decided to create something that might emulate what the final product would look like. To do this, we first looked at a few examples of 3D printers around the engineering lab to see what cartesian arms were made of. 
After this, we thought why not just mimic how 3d printers work, but use it for our own purposes? Eventually we found out about Openbuilds, more on that later. We used openbuilds to recreate a single axis of movement using wheel bearings, a stepper motor and a carbon fiber belt drive chain. After wiring everything together, our completed proof of concept was able to move a plate on an axis using a stepper motor. Photos attached below.

Materials:

For our proof concept, the materials used were:
(The materials below were all later used in the final project)

* Openbuilds Solid V Wheel
* Openbuilds GT2-2M Timing Belt
* Openbuilds Stepper Motor V-Slot Gantry Plate
* Openbuilds 20mm V-Slot Gantry Plate
* Openbuilds Idler Pulley Plate
* Nema 17 Stepper Motor 

## What is Openbuilds?

OpenBuilds is an online community focused on open-source hardware and DIY machine building. It provides a platform for sharing designs, ideas, and resources for building anything from small robots to large CNC machines.

![name](https://openbuilds.com/attachments/picture-assem2-jpg.10522/)

## Commented Code

```python

#include <Servo.h>
#include <Stepper.h>
// change this to the number of steps on your motor
#define STEPS 200 //defining the number of steps

int servoPin = 3; //defining pin to arduino
// Create a servo object
Stepper stepper(STEPS, 4, 5, 6, 7); // assigning pins to stepper
Stepper myStepper2(STEPS, 8, 9, 10, 11); //assigning pins to myStepper2
Servo Servo1;

void setup() {
   // We need to attach the servo to the used pin number
   Servo1.attach(servoPin);
   Serial.begin(9600); //start serial printer
   Serial.println("Stepper test!"); //print on serial printer
  // set the speed of the motor to 30 RPMs
  stepper.setSpeed(60); //setting the speed of the stepper
  myStepper2.setSpeed(60);//right

  stepper.step(-1000); //minus -1000 steps
}
void loop(){
   // Make servo go to 0 degrees
   Servo1.write(0);
   delay(1000);
   // Make servo go to 90 degrees
   Servo1.write(90);
   delay(1000);
   // Make servo go to 180 degrees
   Servo1.write(90);
   delay(1000);

  

  // step one revolution in one direction:
Serial.println("clockwise"); //print on serial printer
myStepper2.step(STEPS); //my second stepper is to go the int: STEPS
stepper.step(STEPS); //assigning value to amount of steps
delay(500);
}

```

## Code Reflection

There wasn't a lot of time to complete the code in this project. Because of how long it took to build a proper plan, materialize our plans in Onshape, and fabricate/assemble, there wasn't time for coding. Unfortunately, we coded in Arduino, thinking that it would be faster and simpler to write. From this, we learned that it's more important to complete tasks properly, and not cut corners. While we were able to get all parts of the robot arm moving, we weren't able to control the arm to write letters.

## Wiring

![wanted to kms](https://github.com/aweder05/Sophie-Anton-Robotic-Arm-2022-2023/assets/112981462/284fba07-54c9-4ba6-955f-db5b4ffeac1f)

## Wiring Reflection

As we were going through and wiring everything, we realized that it would be quite complicated to create a reliable wiring diagram for someone to use. The L2930s that you can see in between the breadboards and other components of the wiring diagram are actually DRV8833 Dual H-Bridge Motor Drivers. Since we used Tinkercad in the wiring diagram process, were were unable to 100% accurately display our type of motor driver. In Hindsight, from now on if we encounter a problem similar to the one described in Tinkercad, we will be using fritzing, as the online libraries and ability to import custom parts is built in already. 

----

## **Evidence**

<img src="https://github.com/aweder05/Sophie-Anton-Robotic-Arm-2022-2023/blob/main/media/ezgif.com-crop.gif?raw=true" height="400">

## CAD

Because it took so long to originally finish our proof of concept, and because of the uncertainty with how to continue our project, our CAD work was slowed and we ended up just starting off with some basic 3D outlines. Eventually we started modeling the circular gear, using the original proof of concept build as a guideline for the rest of the project. First, we needed to model a base made out of acrylic to bring all the parts together. The plate was too big to be cut from a single sheet, so we sectioned it off and used H-brackets, also out of acrylic, to join the two plates together. After that was done, we needed to figure out a way in which the whole thing could spin from a central point, and how the gears on the Openbuilds slide could align perfectly with the circular teeth. The way that we accomplished this was by simply having two circular parts overlap, one attached to the base acrylic sheet, and one bolted to the openbuilds slide. Surprisingly, it worked quite well for such a simple design. The last CAD that we had to do consisted of the Way that the gears would be attached to the slide. The stepper motor was not centered on the slide, so the whole thing was  a bit off balance. To counteract this, we just screwed on another stepper motor to the slide and attached a 3D printed gear to it, just this time without a stepper motor. 

----

<img src="https://github.com/aweder05/Sophie-Anton-Robotic-Arm-2022-2023/assets/112981462/6ac2ffb2-994b-40ad-a807-7dad97720611" width="500">

###### The above image displays an Isometric veiw of our CAD for our Project. The only thing missing would be all of the wheels and such on the Gantry Plate on the beam to make the part slide. Other than that, this image is a good representation of what the whole project would look like, as you can see all of the individual parts. 
----

<img src="https://github.com/aweder05/Sophie-Anton-Robotic-Arm-2022-2023/assets/112981462/e3e8f60a-7dd8-481a-be16-627af06f3840" height="300">

###### This image displays a top-down view of our CAD. We decided to include this image to help the viewer understand the motion of our project, and the different lines and axis that it can cover. You can see how the circular shaped teeth of the gear help the center mechanism rotate 45 degrees in any direction, and how the center piece decides how close to the center and how far away from the gears the gantry plate is. One thing about this image that does bother me a little bit is how the gears attached to the Stepper motors are not perfectly in line with the gears. When we fabricated all of our parts, they did fit fine, this must've been caused by a slight misstep during fastening.
----

![CAD2023 2](https://github.com/aweder05/Sophie-Anton-Robotic-Arm-2022-2023/assets/112981462/6d52582b-5008-4bc4-a385-bf7b626a896e)

###### This image provides valuable insight into how we attached the stepper motors to the openbuilds V-Slot rail. In this image, you can clearly see how the gears align with the 45 degree gear. 

----

# **Overall Building Materials**

Materials:

* A 35 CM Openbuilds V-Slot Rail
* Openbuilds Solid V Wheel
* Openbuilds GT2-2M Timing Belt
* Openbuilds Stepper Motor V-Slot Gantry Plate
* Openbuilds 20mm V-Slot Gantry Plate
* Openbuilds Idler Pulley Plate
* Nema 17 Stepper Motor 
* 3.18 mm Cast Acrylic
* Stepper motor mount
* 3D Printed Parts
* H-Bridge Brackets (Acrylic)
* Multiple nuts, bolts, and screws
* Arduino Uno
* Breadboard, wires, resistors, etc.

# **Problems**

Like every big project, we too encountered problems which were not very helpful at all in eventually coming to a finished project. Below is a more in-depth analysis about our problems, and where exactly it went wrong. 

**Lack of adequate planning**

We worked together to form a plan, but the project idea was overwhelming, and how to achieve our goal was an immense feat. We asked for help from Mr. H when Sophie came back from her trip, and he helped us create a project plan based on what we had. We followed through with the plan, and the machine worked efficiently, but wrapping our heads around how the mechanics would work took a lot of time from project building. Because we didn’t have a tangible plan from the beginning, precious time was taken from building a code. This caused us to scramble at the end of the project-building-time.

**Lack of attendance due to scheduled conflicts**

Neither partners were consistent by being in class due to extracurricular activities, which put a strain on the project-making timeline, further resulting in the tardy submission of the project.

## **Camera Images**

----
|  |  | |
| ------------- | ------------- | ------------- |
| <img src="https://github.com/aweder05/Sophie-Anton-Robotic-Arm-2022-2023/blob/main/media/5.25.1.jpg?raw=true" width="300">  | <img src="https://github.com/aweder05/Sophie-Anton-Robotic-Arm-2022-2023/blob/main/media/5.25.2.jpg?raw=true" width="500">  | <img src="https://github.com/aweder05/Sophie-Anton-Robotic-Arm-2022-2023/blob/main/media/5.25.3.jpg?raw=true" width="500"> |
| The purpose of this image is to show how all of the electrronics were mounted onto the main plate of our arm  | This image perfectly shows how the gears were aligned onto our circular rack and pinion  | This image provides a side perspective on our project that shows how the Openbuilds V-Slot moves like a clock hand on the rack and pinion gear |
| | | | 
----

## Reflection:

Many mistakes were made along the journey of creating the handwriting robot arm. The poor planning and change of ideas resulted in the loss of time, further causing us to scramble to complete the project without a timely manner. One thing that my partner and I learned was to have a concrete, reliable plan created in the time given. Another factor that wasn’t helpful for the overall project was our change of plans, halfway through project-making time. Because of this, we had to reshape both the way we thought about the mechanics of the arm, as well as how we were going to complete the project (the CAD and the code). Attendance was a crucial factor in which we lacked; because both partners were committed to extra curricular activities, one person was always stranded to plan and build on their own, resulting in a motivation deficiency, and loss of time. We learned that there will be an output from the time we put into the project; when we worked outside of class to make up the time we had lost inside of class, there was a dramatic difference in the production of our project. When we didn’t put in the time we had missed from being absent, we would fall into the cycle of loss of incentive, lack of production, lack of incentive, lack of production. Many lessons were learned while making the handwriting robot; next project we will be sure to create a solidified plan, and commit time outside of school to avoid the cycle of unproductivity, and circumvent last minute scrambling at the end of the project.

