# 2022-2023 DE Engineering 3 - Robotic Cartesian Arm 
## Anton Weder    
## Sophie Chen

##### Table of Contents  
* Project Description
* Link to Project Planning
* Proof of Concept 
   - Openbuilds

## Project Description
Our goal for this project is to create a **working robotic arm** which, when complete, will be able to use **stepper motors** and servos to succesfully move a writing utensil around on paper to write things down. 

## Link to Project Planning
The link to our project planning Google Doc can be found here: [link](https://docs.google.com/document/d/1Sfuq9OfWJm28hZP6IfdwjBN-oqiLh9iVy0cK-eDuprw/edit)

Attached below are early sketches of our project planning:
---
#### Image 1: Overall Sketch

![name](https://github.com/aweder05/Sophie-Anton-Robotic-Arm-2022-2023/blob/main/media/PorjectPlanning.png?raw=true)
---
####### In the above image is a sketch of what we originally thought was going to be what our project looked like. It looks a bit like a 3D Printer
---
![name](https://github.com/aweder05/Sophie-Anton-Robotic-Arm-2022-2023/blob/main/media/ProjectPlaning.png?raw=true)

## Proof of Concept
For our proof of concept, we decided to create something that might emulate what the final product would look like. To do this, we first looked at a few examples of 3D printers around the engineering lab to see what cartesian arms were made of. 
After this, we thought why not just mimic how 3d printers work, but use it for our own purposes? Eventually we found out about Openbuilds, more on that later. We used openbuilds to recreate a single axis of movement using wheel bearings, a stepper motor and a carbon fiber belt drive chain. After wiring everything together, our completed proof of concept was able to move a plate on an axis using a stepper motor. Photos attached below.


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
