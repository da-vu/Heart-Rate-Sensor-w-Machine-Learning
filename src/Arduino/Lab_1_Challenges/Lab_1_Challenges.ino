// the setup function runs once when you press reset or power the board

void Lab1_C2(){
  if(!getButton()){
    addTimer();
    delay(1000);
  }
  else{
    runTimer();
  }
      
      
}

void setup() {
setupLED(); //keep it from challenge 1
setupButton();
setupMessage();

}
// the loop function runs over and over again forever
void loop() {
condition4();
//condition5();
//condition6();
//Lab1_C2();
} 