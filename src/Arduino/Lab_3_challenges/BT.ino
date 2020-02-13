//#include "BluetoothSerial.h"
//BluetoothSerial SerialBT;
//
//// ==== Message VARs ====== //
//char in_text[64];                // Character buffer
//int in_text_index = 0;
//
//
//
//void setupMessage(){
//  SerialBT.begin("DAVU_FireBeetle");
//}
//
//void printTime(int integer_to_print){
//  // Serial print integer_to_print
//  SerialBT.println(integer_to_print);
//}
//
//// ==== Message CODE ====== //
//void receiveMessage(){
//  if (SerialBT.available() > 0) { 
//    char incomingChar = SerialBT.read(); // read byte from serial
//    if (incomingChar == '\n'){ 
//      //show the in_text with show message
//      checkMessage();
//      showMessage(in_text, 1, true);
//      //reset the in_text index back to 0
//      in_text_index = 0;
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
//    receiveMessage();
//    if(sending_data){
//      unsigned long now = micros();
//        if(now - last_sample_time > sampling_delay){
//            last_sample_time = micros();//update last_sample_time with current micros()  
//            readADC();//read all ADC values
//           SerialBT.print(last_sample_time);
//           SerialBT.print(",");
//           //Serial.print(": X Value:");
//           SerialBT.print(accelX_Val);
//           SerialBT.print(",");
//           //Serial.print(": Y Value:");
//           SerialBT.print(accelY_Val);
//           SerialBT.print(",");
//           //Serial.print(": Z Value:");
//           SerialBT.print(accelZ_Val);//Serial print last_sample_time,x_val,y_val,z_val\n
//           SerialBT.print("\n");
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
//    delay(2000);
//  }
//  else if(message == "stop data"){
//    sending_data = false;
//  }
//  // set sending_data according to the message received 
//  //delay for 1 second after setting send_data to true.
//}
