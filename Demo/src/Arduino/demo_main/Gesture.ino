unsigned long t = millis();
//===========Gesture var======//
int uthreshZ = 3667;//determine the upper threshold you need
int uthreshY = 2737;
int uthreshX = 2799;

int lthreshZ = 3395;//determine the lower threshold you need
int lthreshY = 2559;
int lthreshX = 2695;

int usthreshZ = 4000;
int usthreshY = 3000;
int usthreshX = 2900;

int lsthreshZ = 2550;
int lsthreshY = 2050;
int lsthreshX = 1800;

// ===== Gesture Code  ========//
int detectGesture(){
  readADC();
  int gest_detected = 0;
  if(accelZ_Val >= uthreshZ && accelY_Val >= uthreshY && accelX_Val >= uthreshX){
      if(accelZ_Val >= usthreshZ || accelY_Val >= usthreshY || accelX_Val >= usthreshX){
        Serial.println("shake detected upper");  
        gest_detected = 2;
        return gest_detected;
      }
    gest_detected = 1; 
  }
  else if(accelZ_Val <= lthreshZ && accelY_Val <= lthreshY && accelX_Val <= lthreshX){
    if(accelZ_Val <= lsthreshZ || accelY_Val <= lsthreshY || accelX_Val <= lsthreshX){
        Serial.println("shake detected lower");  
        gest_detected = 2;
        return gest_detected;
      } 
    gest_detected = 1;
  }
  return gest_detected;
}


void calibrate(){
  showMessage("Calibrating...", 1, true);
  showMessage("Don't move", 2, false);
  
  int maxZ = analogRead(accelZ);
  int minZ = analogRead(accelZ);
  int maxY = analogRead(accelY);
  int minY = analogRead(accelY);
  int maxX = analogRead(accelX);
  int minX = analogRead(accelX);
  
  while(t < 10000){
    accelZ_Val = analogRead(accelZ);
    accelY_Val = analogRead(accelY);
    accelX_Val = analogRead(accelX);
    
    if(accelZ_Val > maxZ){
      maxZ=accelZ_Val;
    }
    if(accelZ_Val < minZ){
      minZ=accelZ_Val;
    }
    if(accelY_Val > maxY){
      maxY=accelY_Val;
    }
    if(accelY_Val < minY){
      minY=accelY_Val;
    }
  
    if(accelX_Val > maxX){
      maxX=accelX_Val;
    }
    if(accelZ_Val < minX){
      minX=accelX_Val;
    }
    t = millis();
   }
   
    showMessage("Calibration Complete!", 1, true);
    showMessage("Tap to start", 1, true);
    Serial.print("Lower threshold for Z:");
    Serial.print(minZ);
    Serial.print(" ");
    Serial.print("Upper threshold for Z:");
    Serial.println(maxZ);
    Serial.print("Lower threshold for Y:");
    Serial.print(minY);
    Serial.print(" ");
    Serial.print("Upper threshold for Y:");
    Serial.println(maxY);
    Serial.print("Lower threshold for X:");
    Serial.print(minX);
    Serial.print(" ");
    Serial.print("Upper threshold for X:");
    Serial.println(maxX);
  
    uthreshZ = maxZ;
    lthreshZ = minZ;
  
    uthreshY = maxY;
    lthreshY = minY;
  
    uthreshX = maxX;
    lthreshX = minX;
}
