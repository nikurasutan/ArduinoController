#include <Servo.h>

char serialData;
String inputString = "";
Servo meinServo;

void setup() {
  pinMode(LED_BUILTIN, OUTPUT);
  Serial.begin(9600);
  inputString.reserve(200);
  meinServo.attach(10);
  
}

void loop() {
  
}

void serialEvent(){
  inputString = "";
  while (Serial.available()){
    char inChar = (char)Serial.read(); //Lies den neuen Byte ein und parse in in einen Char
    inputString += inChar;
  }
  if (inputString == "1"){
     meinServo.write(90);
     delay(1000);
     meinServo.write(0);
  }
}
