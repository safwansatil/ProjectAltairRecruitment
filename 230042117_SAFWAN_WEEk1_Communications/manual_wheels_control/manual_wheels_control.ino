#include <Arduino.h>


const int NUM_CHANNELS = 8;
int channels[NUM_CHANNELS] = {0};  


String inputBuffer = "";
bool newDataAvailable = false;
unsigned long lastDataTime = 0;


void readChannel() {
  
  while (Serial1.available()) {
    char c = Serial1.read();
    
    if (c == '\n') {
     
      newDataAvailable = true;
      lastDataTime = millis();
      break;
    } else if (c != '\r') {
      inputBuffer += c;
    }
  }

  if (newDataAvailable) {
    int tempChannels[NUM_CHANNELS] = {0};
    int channelIndex = 0;
    String value = "";

  
    for (unsigned int i = 0; i < inputBuffer.length(); i++) {
      if (inputBuffer[i] == ',' || i == inputBuffer.length() - 1) {
        // last value
        if (i == inputBuffer.length() - 1 && inputBuffer[i] != ',') {
          value += inputBuffer[i];
        }
        
        // Convert to integer and store
        if (channelIndex < NUM_CHANNELS && value.length() > 0) {
          tempChannels[channelIndex] = value.toInt();
          channelIndex++;
        }
        value = ""; 
      } else {
        value += inputBuffer[i];
      }
    }

    
    if (channelIndex == NUM_CHANNELS) {
      for (int i = 0; i < NUM_CHANNELS; i++) {
        channels[i] = tempChannels[i];
      }
      
  
      Serial.print("Channels received: ");
      for (int i = 0; i < NUM_CHANNELS; i++) {
        Serial.print(channels[i]);
        if (i < NUM_CHANNELS - 1) Serial.print(", ");
      }
      Serial.println();
    } else {
      Serial.print("Error: Expected ");
      Serial.print(NUM_CHANNELS);
      Serial.print(" channels, got ");
      Serial.println(channelIndex);
    }

    
    inputBuffer = "";
    newDataAvailable = false;
  }

  

  

void setup() {
  
  Serial.begin(115200);
  
  
  Serial1.begin(115200);
  
  
  for (int i = 0; i < NUM_CHANNELS; i++) {
    channels[i] = 0;
  }
  
  
}

void loop() {
  
  readChannel();
  
  
  
  
  static unsigned long lastPrint = 0;
  if (millis() - lastPrint > 2000) {
    lastPrint = millis();
    
    
    for (int i = 0; i < NUM_CHANNELS; i++) {
      Serial.print(channels[i]);
      if (i < NUM_CHANNELS - 1) Serial.print(", ");
    }
    
  }
  
  
  delay(10);
}