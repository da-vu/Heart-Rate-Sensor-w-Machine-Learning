unsigned long time_last_tap = 0; //initiate the last tap time at 0
int timer_seconds = 0;

void setup() {
  setupLED();
  setupButton();
  setupMessage();
  initDisplay();
  setupMotor();
  setupADC();
  setupHR();
  calibrate();
  
}

void loop() {
  // put your main code here, to run repeatedly:
  demo();
}

void demo(){
  sendData();
  stateMachineTimer();
}
