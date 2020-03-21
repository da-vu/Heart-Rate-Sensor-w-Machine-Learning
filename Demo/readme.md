# How to run the Demo

**LINK TO YOUTUBE DEMO:**  
## https://youtu.be/3ukGYTXiOgA

## Setup

1. Upload the arduino code from `/Demo/src/Arduino/demo_main` onto the MCU
2. Make sure the firebeetle is plugged in with power.
    * For best results, plug in using USB, not battery

## Solution #1 Demo: Detect Tap from any Orientation
### Calibration at start up to dynamically assign more accurate tap detection threshold values regardless of orientation
1. Start the program by pressing the RST button on the firebeetle
    * the OLED should prompt you that it is calibrating and that you should NOT move the accelerometer
    * The calibration period is about 10 seconds as set in the Arduino code
2. After Calibration is complete, the OLED should display "Tap to start"
3. At this point you can test the tap detection by tapping to see if the timer will increment
4. You can repeat steps 1-3 with any orientation of the accelerometer to test if the solution is working properly
    * Upsidedown, on either side, standing up, at any angle, etc...

*Note* As explained in the Final report, if you change the orientation after calibration is complete, to have the BEST results, you must recalibrate by repeating steps 1-3. Refer to the final report for more details.

## Solutions #2 and #3 Demo: Shake-2-Reset-Timer
### Shake detection and non-blocking logic to interrupt timer countdown

* Precautions: This demo is built off of Solution #1 but will work **BEST** when the accelerometer is laying flat with the +Z axis pointing up. Refer to the final report for more details as to why. 

1. Calibrate the device with the accelerometer laying flat.
    * read precaution
2. Tap the accelerometer to increment the timer
    * Go as high as you want ;) you won't have to restart because of the built in Shake-2-reset 
3. After setting the last tap, wait 3 seconds
    * This step is required for the Shake-2-reset function to work. More details in final report.
4. Once you see that the timer has started the countdown, you can now shake the device to reset the timer back to 0
5. After shaking the OLED should display "RESETTING TIMER".
    * For best results, DO NOT shake the timer anymore when this display is on 
    * After about 5 seconds, the OLED should display "Tap to start" again meaning that the timer has properly reset
6. Repeat steps 2-4 as many time as you want to test this solution


