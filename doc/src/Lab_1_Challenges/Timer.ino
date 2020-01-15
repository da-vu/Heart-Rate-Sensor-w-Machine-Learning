int timer_seconds = 0;

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
    delay(1000);
  }
}
