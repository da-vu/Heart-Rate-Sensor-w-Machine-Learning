unsigned long t = millis();


// ===== Gesture Code  ========//
bool detectTap(){
  //read the ADC values. Note that the ADC values are global so you don’t need to define a local variable for them. 
  readADC();
  bool tap_detected = false; // first set to false
  if(accelZ_Val >= uthreshZ && accelY_Val >= uthreshY && accelX_Val >= uthreshX){
   // printADC();
    tap_detected = true; //if the accel values meet the rule, set to true
  }
  else if(accelZ_Val <= lthreshZ && accelY_Val <= lthreshY && accelX_Val <= lthreshX){
   // printADC();
    tap_detected = true;
  }
  return tap_detected;
}

void calibrate(){
  Serial.println("DON'T MOVE ACCELEROMETER!");
  showMessage("Calibrating...", 1, true);
  showMessage("Don't move", 2, false);
  
  int maxZ = analogRead(accelZ);
  int minZ = analogRead(accelZ);
  int maxY = analogRead(accelY);
  int minY = analogRead(accelY);
  int maxX = analogRead(accelX);
  int minX = analogRead(accelX);
  
  
  
  while(t < 5000){
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
    Serial.println("DONE CALIBRATING");
    showMessage("DONE!", 1, true);
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
