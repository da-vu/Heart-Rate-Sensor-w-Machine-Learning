// ========= Timer Var ========= //
int timer_state = 0;

void addTimer(){
  // add one to timer_seconds
  timer_seconds += 1;
  // print the time with printTime(//the integer to print)
  printTime(timer_seconds);
}

void runTimer(){
  while(timer_seconds > 0){
    // minus one second from timer_second
    timer_seconds -= 1;
    // print the time with printTime(int)
    printTime(timer_seconds);
    // wait 1 second
    delay(100);
  }
}

void runTimerOLED(){
  while(timer_seconds > 0){
    timer_seconds--;
     char message_buffer[4];
    String stringTime = String(timer_seconds); //convert timer_seconds to string
    stringTime.toCharArray(message_buffer,4); //convert string to char buffer
    showMessage(message_buffer, 1, true);
    delay(1000);
  }
}

void stateMachineTimer(){
  if (timer_state == 0){
    if(detectTap()) {
      addTimerOLED();
      time_last_tap = millis();
      timer_state = 1;
    }
  }
  else if (timer_state == 1){
    if(detectTap()) {
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
    showMessage("BUZZZZZZZZ", 2, false);
    timer_state = 3;
  }
  else if(timer_state == 3){
    buzzMotor(255);
    if(detectTap()){
      buzzMotor(0);
      timer_state = 0;
      delay(10);
      showMessage("Tap to start", 1, true);
    }
  }
}
