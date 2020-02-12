int red_led = 25;
int yellow_led = 27;
int blue_led = 13;

void setupLED()  { 
  //Code for pin setups 
  pinMode(red_led, OUTPUT);
  pinMode(yellow_led, OUTPUT);
  pinMode(blue_led, OUTPUT);
  pinMode(LED_BUILTIN, OUTPUT);
}
void condition1(){ 
  //Code for Condition 1 - builtin LED blinks at 1hz
  digitalWrite(LED_BUILTIN, HIGH);
  delay(500);
  digitalWrite(LED_BUILTIN, LOW);
  delay(500);
}

void condition2(){ 
  //Code for Condition 2 - builtin LED blinks at 10hz
  digitalWrite(LED_BUILTIN, HIGH);
  delay(50);
  digitalWrite(LED_BUILTIN, LOW);
  delay(50);
}

void condition3(){ 
  //Code for Condition 3 - builtin LED blinks at 50hz
  digitalWrite(LED_BUILTIN, HIGH);
  delay(10);
  digitalWrite(LED_BUILTIN, LOW);
  delay(10);
}

void condition4(){ 
  //Code for Condition 4 - red LED on for 1s & off for 100ms
  digitalWrite(red_led, HIGH);
  delay(1000);
  digitalWrite(red_led, LOW);
  delay(100);
}

void condition5(){ 
  //Code for Condition 4 - yellow LED on for 200ms & off for 50ms
  digitalWrite(yellow_led, HIGH);
  delay(200);
  digitalWrite(yellow_led, LOW);
  delay(50);
}


void condition6(){ 
  //Code for Condition 4 - yellow LED on for 20ms & off for 10ms
  digitalWrite(blue_led, HIGH);
  delay(20);
  digitalWrite(blue_led, LOW);
  delay(10);
}
