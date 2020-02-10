//=====timer var=====//
unsigned long time_last_tap = 0; //initiate the last tap time at 0
int timer_seconds = 0;


//===========Gesture var======//
int uthreshZ;//determine the upper threshold you need
int uthreshY;
int uthreshX;

int lthreshZ;//determine the lower threshold you need
int lthreshY;
int lthreshX;




void Lab2_C1(){
  // buzz motor at full power for 1 second
  buzzMotor(255);
  delay(1000);
  // buzz motor at half power for 1 second
  buzzMotor(127);
  delay(1000);
  // don’t buzz for 1 second
  buzzMotor(0);
  delay(1000);
}

void Lab2_C2(){
if(detectTap()) {
    //add one second to the timer and show on OLED
    addTimerOLED();
    //printADC();
}
}

void Lab2_C3(){
  receiveMessage();
}


void Lab2_C4(){
  if(detectTap()) {
    addTimerOLED();
    time_last_tap = millis();
  }
  unsigned long now = millis();
  if(now - time_last_tap >= 3000){
    runTimerOLED();
  }
  
  
}
void setup() {
  // put your setup code here, to run once:
  initDisplay();
  Serial.begin(9600);
  setupMotor();
  setupADC();
  calibrate(); //determines resting threshold - takes ~15 seconds
  
}

void loop() {
  // put your main code here, to run repeatedly:
 // Lab2_C3();
  stateMachineTimer();
  
}
