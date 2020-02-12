//
//// ==== Message VARs ====== //
//char in_text[64];                // Character buffer
//int in_text_index = 0;
//
//
//
//void setupMessage(){
//  // Serial begin at 9600 
//  Serial.begin(9600);
//}
//
//void printTime(int integer_to_print){
//  // Serial print integer_to_print
//  Serial.print(millis());
//  Serial.print(": ");
//  Serial.println(integer_to_print);
//}
//
//// ==== Message CODE ====== //
//void receiveMessage(){
//  if (Serial.available() > 0) { 
//    char incomingChar = Serial.read(); // read byte from serial
//    if (incomingChar == '\n'){ 
//      //show the in_text with show message
//      showMessage(in_text, 1, true);
//      //reset the in_text index back to 0
//      in_text_index = 0;
//      checkMessage();
//      memset(in_text,0,20); // this will clear the in_text buffer
//    }
//    else{
//      //assign in_text[index] to the incoming char
//      in_text[in_text_index] = incomingChar;
//      //increment the index
//      in_text_index++;
//    }
//  }
//}
//
//
//// LAB 3 STUFF
//
//
//int sampling_rate = 50; //sampling rate in Hz
//unsigned long sampling_delay = calcSamplingDelay(sampling_rate); //microseconds between samples
//unsigned long last_sample_time = 0; //microsecond of last sample
//
//bool sending_data = false; //to send data?
//
//
//void sendData(){
//    if(sending_data){
//      unsigned long now = micros();
//        if(now - last_sample_time > sampling_delay){
//            last_sample_time = micros();//update last_sample_time with current micros()  
//            readADC();//read all ADC values
//           Serial.print(last_sample_time);
//           Serial.print(",");
//           //Serial.print(": X Value:");
//           Serial.print(accelX_Val);
//           Serial.print(",");
//           //Serial.print(": Y Value:");
//           Serial.print(accelY_Val);
//           Serial.print(",");
//           //Serial.print(": Z Value:");
//           Serial.print(accelZ_Val);//Serial print last_sample_time,x_val,y_val,z_val\n
//           Serial.print("\n");
//        }
//    }
//}
//
//
//
//
//long calcSamplingDelay(long sampling_rate){
//  int temp = 1 / sampling_rate;
//  temp = temp*1000000;
//    return temp;//number of microseconds to wait between samples
//}
//
//void checkMessage(){
//  String message = String(in_text); // converts in_text into a string
//  if(message == "start data"){
//    sending_data = true;
//    delay(1000);
//  }
//  else if(message == "stop data"){
//    sending_data = false;
//  }
//  // set sending_data according to the message received 
//  //delay for 1 second after setting send_data to true.
//}
