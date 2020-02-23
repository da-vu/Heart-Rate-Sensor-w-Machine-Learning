# ECE 16 LAB 4 REPORT
Dan Vu  
A14596430

2/24/2020
- - -
## Tutorials:

### MAX30105 Pulse Sensor:
> Q1. Note that you can connect both the heart rate sensor and your OLED at the same time, both of which use the I2C SDA and SCL lines. Why does this work?

> A1. The I2C protocol allows the "master" (MCU) to connect with multiple "slave" devices- in this case, the 2 "slave" devices are the OLED and the heart rate sensor. This works because the OLED and the heart-rate sensor have unique addresses that are sent (in the first data frame) and allow the MCU to select which device is going sending or receiving data. Setting and selecting the device addresses are configured by the MCU through the Wire.h library.

> Q2. Notice the while(1) statement. What happens if the device is not connected? What happens if the error is printed and then you connect the device? Will the code proceed? Try it and describe the behavior.

> A2. If the device is not connected, an error message " MAX30105 was not found. Please check wiring/power. " is printed into the serial monitor. If you connect the device after the error is printed, the code will not continue to proceed because it can not exit the while(1) loop. To proceed you must reset the MCU and make sure the sensor is connected.

> Q3. what would the settings look like if you were to: set the led brightness to 25mA, use only the Red + IR LED, Sample at 200Hz, and use an ADC range of 8192?

> A3. 
>
>     byte ledBrightness = 0x80; //Options: 0=Off to 255=50mA
>     byte sampleAverage = 8; //Options: 1, 2, 4, 8, 16, 32
>     byte ledMode = 2; //Options: 1 = Red only, 2 = Red + IR, 3 = Red + IR + Green
>     int sampleRate = 200; //Options: 50, 100, 200, 400, 800, 1000, 1600, 3200
>     int pulseWidth = 411; //Options: 69, 118, 215, 411
>     int adcRange = 8192; //Options: 2048, 4096, 8192, 16384

> Q4. What are the units of the pulse width? Would the bigger the pulseWidth result in a more intense or less intense measurement? Why?

> A4. According to the data sheet, the pulseWidth units are in micro-seconds. It seems like a higher pulseWidth results in a less intense measurement (measured amplitude). 

> Q5. How many bits are needed for an ADC range of 16384?

> A5. 2^14 = 16384, therefore 14 bits are needed for an ADC range of 16384

> Q6. What is the peak wavelength of the R, IR, and G LEDs?

> A6. According to the datasheet, the typical peak wavelengths for each LEDs are:  
> Red:660nm, IR: 880nm, Green: 537nm. 

> Q7. If you want to read the Green value, what Mode do you need the setting to be in and what function will you need to use to get the green signal?

> A7. LED MODE needs to be 3, and you will call the `.getGreen()` function.

### Matplotlib:

> Q8. What was plotted? What does this tell you about how plt.plot interprets the input? Remember that
>
>     a = [1, 2, 3, 4]
>         [1, 4, 9,16]

>A8. plt.plot interprets 

> Q9. Try your best to replicate the above plot by shaking your accelerometer. The above was sampled at 50Hz for 10 seconds. Make a gif of you running your program, shaking your accelerometer, and a plot showing up similar to the one above

> A9.  

> Q10. What is approximately the frequency of oscillation of the x axis signal in the plot above?

> A10.

### Filtering Signals
#### Removing mean offset
#### Smoothing with moving average
#### Detrending a moving average
> Q11. Try different n_avg and document, with plots, the result for a few different n_avg and describe which n_avg worked well in emphasizing the taps? 

> A11.

#### Looking at the signal in different ways
> Q12. Try using np.diff(s) to calculate the gradient of the signal s and plot the signal. 

> A12. 

## Challenges:

### Challenge 1:

### Challenge 2: 

### Challenge 3:

