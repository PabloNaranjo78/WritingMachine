#include <AccelStepper.h>
#include <MultiStepper.h>
#include <Servo.h>

long positions[2];
int colores[] = {0,90,180};

AccelStepper motorX(AccelStepper::FULL4WIRE,2,3,5,6);
AccelStepper motorY(AccelStepper::FULL4WIRE,8,9,10,11);

Servo servo;

MultiStepper steppers;

float posicionX = 0;
float posicionY = 0;

int x;
bool entra;
void setup() {
 Serial.begin(115200);
  motorX.setMaxSpeed(2000);
  motorY.setMaxSpeed(1000);
  motorX.setAcceleration(2000);
  motorY.setAcceleration(2000);
  

  motorX.disableOutputs();
  motorY.disableOutputs();

  steppers.addStepper(motorX);
  steppers.addStepper(motorY);

  servo.attach(12);

}
void loop() {
 while (!Serial.available()){
  delay(1000);
  x = Serial.readString().toInt();
 if (x == 1){
    Serial.print("Uno");
    servo.write(colores[x-1]);
    delay(1000);
    }
    else if (x == 2){
      Serial.print("Dos");
      servo.write(colores[x-1]);
    delay(1000);
      }
   else if (x==3){
      servo.write(colores[x-1]);
    }
  
  }
  
 
}
