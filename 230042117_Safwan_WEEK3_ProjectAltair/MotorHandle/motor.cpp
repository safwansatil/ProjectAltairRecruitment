#include "motor.h"
Motor::Motor(byte forwardPin, byte backwardPin){
  this->forwardPin = forwardPin;
  this->backwardPin = backwardPin;
}
void Motor::setupMotor(){
  pinMode(forwardPin, OUTPUT);
  pinMode(backwardPin, OUTPUT);
}
void Motor::moveF(int speed){
  analogWrite(forwardPin, speed);
  analogWrite(backwardPin, 0);
}

void Motor::moveB(int speed){
  analogWrite(forwardPin, 0);
  analogWrite(backwardPin, speed);
}

void Motor::stop(){
  analogWrite(forwardPin, 0);
  analogWrite(backwardPin, 0);
}
