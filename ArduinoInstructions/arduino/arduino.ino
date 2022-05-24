#include <AccelStepper.h>
#include <MultiStepper.h>
#include <Servo.h>

long positions[2];
int colores[] = {0,90,180};

AccelStepper motorX(AccelStepper::DRIVER,2,3,5,6);
AccelStepper motorY(AccelStepper::DRIVER,8,9,10,11);

Servo servo;

MultiStepper steppers;

float posicionX = 0;
float posicionY = 0;


void setup() {
  Serial.begin(9600);
  motorX.setMaxSpeed(70);
  motorY.setMaxSpeed(70);

  steppers.addStepper(motorX);
  steppers.addStepper(motorY);

  servo.attach(12);
  
}

void loop() {
  while(true){
    delay(1000);
   steppers.run();
   delay(1000);

    
    }

}
