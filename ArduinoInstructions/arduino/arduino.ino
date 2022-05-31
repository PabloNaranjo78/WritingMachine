#include <AccelStepper.h>
#include <MultiStepper.h>
#include <Servo.h>
#include <ArduinoJson.h>

long positions[2]= {0,0}; 
int color[] = {90,0,190};
int instrucciones[] = {1,2,3,4};
int instruccionActual = 0;

AccelStepper motorX(AccelStepper::FULL4WIRE,2,3,5,6);
AccelStepper motorY(AccelStepper::FULL4WIRE,8,9,10,11);

Servo servo;

MultiStepper steppers;

float posicionX = 0;
float posicionY = 0;

class ComandoLapicero{
    public:
        bool cambioColor = false;
        int color = 1;

        int Xmov = 0;
        int Ymov = 0;
        String tipo = "";
        String ultimoColor = "1";


        void cargarComando(String comando){
            String XmovTemp = "";
            String YmovTemp = "";
            String colorTemp = "1";
            int contadorP = 0;
            tipo = "";

            for (int i = 0; i< comando.length(); i++){
                if (comando.charAt(i) == '%'){
                    contadorP++;
                }
                else if (contadorP<2){
                    tipo+=comando.charAt(i);
                }else if (tipo == "mover"){
                    if (contadorP<3){
                        XmovTemp+= comando.charAt(i);
                    }else if (contadorP<4){
                        YmovTemp+= comando.charAt(i);
                    }
                } else if (tipo == "color"){
                  if (contadorP<3){
                        colorTemp = comando.charAt(i);
                        if (colorTemp == "f"){
                          colorTemp = ultimoColor;
                        } else if (colorTemp == "1" || colorTemp == "2"){
                          ultimoColor = colorTemp;
                        }
                    }
                }
            }

            Xmov = XmovTemp.toInt();
            Ymov = YmovTemp.toInt();
            color = colorTemp.toInt();
        }
};

ComandoLapicero comandoLapicero;
String tempMsg;

void setup() {
  Serial.begin(115200);
  Serial.setTimeout(1);
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
 while (!Serial.available());
 if(!steppers.run()){
  delay(1);
  tempMsg = Serial.readString();
  //Serial.println(tempMsg);
  comandoLapicero.cargarComando(tempMsg);
  //Serial.println(comandoLapicero.Ymov);
  delay(1);
  Serial.println(comandoLapicero.ultimoColor);
  if (comandoLapicero.tipo == "mover"){
    motorX.enableOutputs();
    motorY.enableOutputs();
    diagonal(comandoLapicero.Xmov,comandoLapicero.Ymov);
    steppers.moveTo(positions);
  } else  if (comandoLapicero.tipo == "color"){
    colores(comandoLapicero.color);
  }else{
    motorX.disableOutputs();
    motorY.disableOutputs();
    colores(0);
    }
  /**if (instruccionActual == 1){
    motorX.enableOutputs();
    motorY.enableOutputs();
    colores(0);
    lineaX(250);
    steppers.moveTo(positions);
  }
  else if (instruccionActual == 3){
    motorX.enableOutputs();
    motorY.enableOutputs();
    colores(0);
    lineaX(-250);
    steppers.moveTo(positions);
  }
  else if (instruccionActual == 4){
    motorX.enableOutputs();
    motorY.enableOutputs();
    colores(2);
    lineaY(250);
    steppers.moveTo(positions);
  }
  else if (instruccionActual == 2){
    motorX.enableOutputs();
    motorY.enableOutputs();
    colores(2);
    lineaY(-250);
    steppers.moveTo(positions);
  }
  else if (instruccionActual == 5){
    motorX.enableOutputs();
    motorY.enableOutputs();
    colores(0);
    diagonal(230,-250);
    steppers.moveTo(positions);
  }
  else if (instruccionActual == 6){
    motorX.enableOutputs();
    motorY.enableOutputs();
    colores(2);
    diagonal(-230,250);
    steppers.moveTo(positions);
  }
  else {
    motorX.disableOutputs();
    motorY.disableOutputs();
    colores(1);
    }
  //instruccionActual++;**/
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
