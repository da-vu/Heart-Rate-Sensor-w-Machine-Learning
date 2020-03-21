#include <Wire.h>
#include "MAX30105.h"

MAX30105 particleSensor;

//HR DATA
int HR_Data=0;



void setupHR(){
  if (!particleSensor.begin(Wire, I2C_SPEED_FAST)) //Use default I2C port, 400kHz speed
    {
      Serial.println("MAX30105 was not found. Please check wiring/power. ");
      while (1);
    }
    
   //Setup to sense a nice looking saw tooth on the plotter
  byte ledBrightness = 0x2F; //Options: 0=Off to 255=50mA
  byte sampleAverage = 32; //Options: 1, 2, 4, 8, 16, 32
  byte ledMode = 1; //Options: 1 = Red only, 2 = Red + IR, 3 = Red + IR + Green
  int sampleRate = 1600; //Options: 50, 100, 200, 400, 800, 1000, 1600, 3200
  int pulseWidth = 215; //Options: 69, 118, 215, 411
  int adcRange = 4096; //Options: 2048, 4096, 8192, 16384
  
  particleSensor.setup(ledBrightness, sampleAverage, ledMode, sampleRate, pulseWidth, adcRange); //Configure sensor with these settings

}

void readHR(){
  HR_Data = particleSensor.getRed()  ;//get IR pulse data
}
