// OLED library includes
#include <U8g2lib.h>
#include <U8x8lib.h>
#include <Wire.h>


// OLED setup
#define OLED_RESET 4 // this value resets the OLED
U8X8_SSD1306_128X32_UNIVISION_HW_I2C u8x8(OLED_RESET);

// =========== OLED Code ============ //

// ----------------------------------------------------------------
// Initialize the OLED with base font for fast refresh
// ----------------------------------------------------------------
void initDisplay() {
  u8x8.begin();
  u8x8.setPowerSave(0);
  u8x8.setFont(u8x8_font_amstrad_cpc_extended_r);
  u8x8.setCursor(0, 0);
}
// ----------------------------------------------------------------
// A function to write a message on the display
// "row" specifies which row to print on... 1, 2, 3, etc.
// "clearDisplay" specifies if everything should be wiped or not
// ----------------------------------------------------------------
void showMessage(const char * message, int row, bool cleardisplay) {
  if(cleardisplay){
    u8x8.clearDisplay();
  }
  u8x8.setCursor(0, row);
  u8x8.print(message);
}
void addTimerOLED(){
  char message_buffer[4];
  //increment timer_seconds
  timer_seconds++;
  String stringTime = String(timer_seconds); //convert timer_seconds to string
  stringTime.toCharArray(message_buffer,4); //convert string to char buffer
  // show message_buffer with showMessage
  showMessage(message_buffer, 1, true);
  
}
