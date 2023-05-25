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
