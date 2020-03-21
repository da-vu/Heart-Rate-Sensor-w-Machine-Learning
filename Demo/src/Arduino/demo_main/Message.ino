// ==== Message VARs ====== //
char in_text[64];            
int in_text_index = 0;

int sampling_rate = 50; //sampling rate in Hz
unsigned long sampling_delay = calcSamplingDelay(sampling_rate); //microseconds between samples
unsigned long last_sample_time = 0; //microsecond of last sample

bool sending_data = false; //to send data?

void setupMessage(){
  Serial.begin(115200);
}

void printTime(int integer_to_print){
  Serial.println(integer_to_print);
}

// ==== Message CODE ====== //
void receiveMessage(){
  if (Serial.available() > 0) { 
    char incomingChar = Serial.read(); 
    if (incomingChar == '\n'){ 
      showMessage(in_text, 1, true);
      in_text_index = 0;
      checkMessage();
      memset(in_text,0,20);
    }
    else{
      in_text[in_text_index] = incomingChar;
      in_text_index++;
    }
  }
}


void sendData(){
    receiveMessage();
    if(sending_data){
      unsigned long now = micros();
        if(now - last_sample_time > sampling_delay){
            last_sample_time = micros();
            readADC();
            readHR();
           Serial.print(last_sample_time);
           Serial.print(",");
           Serial.print(accelX_Val);
           Serial.print(",");
           Serial.print(accelY_Val);
           Serial.print(",");
           Serial.print(accelZ_Val);
           Serial.print(",");
           Serial.print(HR_Data);
           Serial.print("\n");
        }
    }
}




long calcSamplingDelay(long sampling_rate){
  int temp = 1 / sampling_rate;
  temp = temp*1000000;
    return 1000000/sampling_rate;//number of microseconds to wait between samples
}

void checkMessage(){
  String message = String(in_text); // converts in_text into a string
  if(message == "start data"){
    sending_data = true;
    delay(1000);
  }
  else if(message == "stop data"){
    sending_data = false;
  }

}
