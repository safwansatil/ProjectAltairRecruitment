#include "motor.h"
// dummy values
Motor leftMotor(9,10);
Motor rightMotor(5,6);
void setup() {
  leftMotor.setupMotor();
  rightMotor.setupMotor();
}

void loop() {
  // fwd
  leftMotor.moveF(200);
  rightMotor.moveF(200);
  delay(2000);
  //stp
  leftMotor.stop();
  rightMotor.stop();
  delay(1000);
  //bck
  leftMotor.moveB(150);
  rightMotor.moveB(150);
  delay(2000);

}
