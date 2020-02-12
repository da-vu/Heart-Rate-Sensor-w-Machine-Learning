
// ==== Message VARs ====== //
char in_text[64];                // Character buffer
int in_text_index = 0;



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

// ==== Message CODE ====== //
void receiveMessage(){
  if (Serial.available() > 0) { 
    char incomingChar = Serial.read(); // read byte from serial
    if (incomingChar == '\n'){ 
      //show the in_text with show message
      showMessage(in_text, 1, true);
      //reset the in_text index back to 0
      in_text_index = 0;
      memset(in_text,0,20); // this will clear the in_text buffer
    }
    else{
      //assign in_text[index] to the incoming char
      in_text[in_text_index] = incomingChar;
      //increment the index
      in_text_index++;
    }
  }
}
