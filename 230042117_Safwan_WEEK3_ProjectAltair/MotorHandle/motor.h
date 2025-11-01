#ifndef MOTOR_H
#define MOTOR_H
#include <Arduino.h>
class Motor{
  public:
    Motor(byte forwardPin,byte backwardPin);
    void setupMotor();
    void moveF(int speed);
    void moveB(int speed);
    void stop();
  private:
    byte forwardPin;
    byte backwardPin;
};


#endif