// ========= Timer Var ========= //
int timer_state = 0;
bool reset = false;

void runTimerOLED(){
  unsigned long before = millis();
  while(timer_seconds > 0){
    unsigned long now = millis();
    if(now - before >= 1000){
    timer_seconds--;
     char message_buffer[4];
    String stringTime = String(timer_seconds); //convert timer_seconds to string
    stringTime.toCharArray(message_buffer,4); //convert string to char buffer
    showMessage(message_buffer, 1, true);
    before=now;
    }
    else if (detectGesture()==2){
      reset = true;
      return;
    }
  }
}

void stateMachineTimer(){
  if (timer_state == 0){
    if(detectGesture()==1) {
      addTimerOLED();
      time_last_tap = millis();
      timer_state = 1;
    }
  }
  else if (timer_state == 1){
    if(detectGesture()==1) {
      addTimerOLED();
      time_last_tap = millis();
    }
    unsigned long now = millis();
    if(now - time_last_tap >= 3000){
      timer_state = 2;
    }
  }
  else if (timer_state == 2){
    runTimerOLED();
    if(reset){
      showMessage("RESETTING TIMER", 1, true);
      delay(5000);
      showMessage("Tap to start", 1, true);
      timer_seconds = 0;
      reset = false;
      timer_state = 0;
    }
    else{
      timer_state = 3;
    }
  }
  else if(timer_state == 3){
    showMessage("BUZZZZZZZZ", 2, false);
    buzzMotor(255);
    digitalWrite(yellow_led, HIGH);
    if(detectGesture()==1){
      buzzMotor(0);
      digitalWrite(yellow_led, LOW);
      timer_state = 0;
      showMessage("Tap to start", 1, true);
    }
  }
}
