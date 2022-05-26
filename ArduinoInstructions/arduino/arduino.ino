#include <AccelStepper.h>
#include <MultiStepper.h>
#include <Servo.h>

long positions[2]= {0,0}; 
int color[] = {0,90,190};
int instrucciones[] = {1,2,3,4};
int instruccionActual = 1;

AccelStepper motorX(AccelStepper::FULL4WIRE,2,3,5,6);
AccelStepper motorY(AccelStepper::FULL4WIRE,8,9,10,11);

Servo servo;

MultiStepper steppers;

float posicionX = 0;
float posicionY = 0;


void setup() {
  Serial.begin(9600);
  motorX.setMaxSpeed(200);
  motorY.setMaxSpeed(200);
  motorX.setAcceleration(200);
  motorY.setAcceleration(200);
  

  motorX.disableOutputs();
  motorY.disableOutputs();

  steppers.addStepper(motorX);
  steppers.addStepper(motorY);

  servo.attach(13);
  
}

void loop() {
 steppers.moveTo(positions);
 if(!steppers.run()){
  if (instruccionActual == 1){
    colores(0);
  lineaX(250);
  }
  if (instruccionActual == 3){
    colores(0);
  lineaX(-250);
  }
  if (instruccionActual == 4){
    colores(2);
  lineaY(250);
  }
  if (instruccionActual == 2){
    colores(2);
  lineaY(-250);
  }
  if (instruccionActual == 5){
    colores(0);
  diagonal(230,-250);
  }
  if (instruccionActual == 6){
    colores(2);
  diagonal(-230,250);
  }
  if (instruccionActual >= 7){
    motorX.disableOutputs();
    motorY.disableOutputs();
    colores(1);
    }
  instruccionActual++;
  delay(1000);
  }
  
}

void lineaX(int pos){
  positions[0] = pos + motorX.currentPosition();
  positions[1] = 0 + motorY.currentPosition();
}
void lineaY(int pos){
  positions[0] = 0 + motorX.currentPosition();
  positions[1] = pos + motorY.currentPosition();
}
void diagonal(int posX, int posY){
  positions[0] = posX + motorX.currentPosition();
  positions[1] = posY + motorY.currentPosition();
}

void colores(int x){
  servo.write(color[x]);
  delay(500);
  }
