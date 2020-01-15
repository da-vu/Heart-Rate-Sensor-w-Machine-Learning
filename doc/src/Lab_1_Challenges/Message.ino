void setupMessage(){
  // Serial begin at 9600 
  Serial.begin(9600);
}

void printTime(int integer_to_print){
  // Serial print integer_to_print
  Serial.print(millis());
  Serial.print(": ");
  Serial.println(integer_to_print);
}
