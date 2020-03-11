# ECE 16 Lab Report 5
Dan Vu

A14596430

3/11/2020

## Part 1

## Tutorial 1: Correlation and Bland-Altman Plot

> Q. Which metric (R,RMSE,STD,Bias) do you use to look at each of the four key analysis?

> **A.**  
> **R** = correlation coefficieant  
> **RMSE** = accuracy  
> **STD** = precision  
> **BIAS** = bias 

> Q. Using the above code, plot the correlation and bland-altman plot of your lab 4 HR estimation vs the reference. What is your R value, bias, and 95% limits of agreement?

> A. 
> **Code:** `/src/Python/correlation_bland_altman.py`  
> **Plot:**  
> ![Image of Challenge](fig/bamp.png)  
> **R = 0.94, BIAS = 5.87, 95% limits of agreement(upper,lower) = 16.55,-4.82**   
> An *R* value close to `1` would mean that it is closely correlated (1 is perfectly correlated)  
> A *Bias* value of '5.87' means the estimate is biased to be around 5.87 off from the reference  
> The *upper,lower limits of agreements* show if there is an outlier that is outside of the 1.96 STD(95%) 

> Q. Sketch the correlation plot that would give you an R of 0. What does an R of 0 mean?  

> A.  
> **Plot:**  
> ![Image of Challenge](fig/nocorrbamp.png)  
> In this case, *R = 0* because no matter what the reference is, the estimate is always constant (100). This means that there is no correlation between the estimate and reference.

> Q. Sketch a scatter plot of the correlation and bland-altman plot if your estimation was perfect every time. What would be the R, RMSE, Bias, and STD value of a perfect estimator?

> A.  
> **Plot:**  
> ![Image of Challenge](fig/prefbamp.png)  
> In this case, *R = 1* meaning that is perfectly correlated. The limits of agreements and Bias are 0 meaning that everything is no bias and everything is precise. 

> Q. How might we use the 1.96STD mark to assess if a given estimate might be an outlier?

> A.  The 1.98STD line marks the upper and lower limits of agreement. Anything outside of the 1.96STD lines means that the estimate is probably an outlier or does not correlate well to the rest of the estimates. 

> Q. What would your Bland-Altman plot look like if your algorithm always guessed 70BPM regardless of the actual heart rate? Describe some prominent features about the graph beyond just showing it.

> A.  
> ![Image of Challenge](fig/70bamp.png)  
> In this case, *R = 0* because the estimate is completely uncorrelated with the reference. Some prominent features in the bland-altman plot is that the points plotted is a straight line that can be represented by y=mx+b.


## Tutorial 2: Frequency Domain

> Q. If your sampling rate was 120Hz, what would be your maximum frequency (the Nyquist frequency)?

> A. 60 because Fs = 120, Half of the sampling frequency is 60hz which is the highest frequency component that is captured. 

> Q. If your signal bandwidth is composed of 0-10Hz, what is your minimum sampling rate to capture this signal based on the Nyquist sampling theorem? What would be recommended in general practice however?

> A. Based on the Nyquist sampling theorem, 20hz is the minimum nyquist rate because you would want to sample at 2x the highest frequency captured. However, 40hz (or 4x the max) is the practical recommended frequency. 

## Tutorial 3: Baseline DC Signal

> Q. How does your detrend function modify the frequency content of the signal? Show the plot and circle the part that is most modified and explain why.

> A. Detrending your signal removes the moving average from the signal. Without detrending, the moving average may be captured as the dominant frequency (often near the 0hz<1hz mark). This is why you see the high peak near the 0hz mark  below.  
> **Plot:**  
> ![Image of Challenge](fig/l5t3-1.png)  
> After detrending the signal (effectively removing the moving average), the frequency plot should look like this:  
>![Image of Challenge](fig/l5t3-2.png)   


## Tutorial 4: Dominant Frequency Component

> Q. Show the code - Use np.argmax to find the actual dominant frequency of the x acceleration (currently labeled as 1Hz in the above plot). The aim here is to use argmax to get the index of the maximum value of Pxx and then use that index to get the corresponding frequency in the Freqs array. Try this with and without removing the DC offset. What do you get?

> A. 
> **Code:**  
>  
>     import numpy as np
>     import matplotlib.pyplot as plt
>     from Libraries.HR import HR
>     from Libraries.Data import Data
>     
>     data_array = np.genfromtxt('data/appendix_a.csv', delimiter=',')#get data from >     Appendix A and save as .csv.
>     data = Data()
>     data.add_data(data_array)
>     print(data.get_num_samples())
>     
>     fs = int(data.calc_sampling_rate()) #sampling rate in Hz
>     t = (data_array[:,0] - data_array[0,0])/1e6#get the time array
>     s = data_array[:,1] #get the x-acceleration array
>     s = HR.detrend(s,fs)
>     
>     plt.clf()
>     plt.subplot(211)
>     plt.plot(t, s)
>     plt.subplot(212)
>     Pxx, Freqs = plt.psd(s, NFFT=len(t), Fs=fs) #plot the power spectral density
>     plt.show()
>     
>     plt.clf()
>     plt.plot(Freqs, Pxx)
>     plt.show()
>     
>     print(Freqs[np.argmax(Pxx)])
> **Plot w/ removing DC offset:**  
>![Image of Challenge](fig/domfreq1.png)  
> **Plot w/o removing DC offset:**  
>![Image of Challenge](fig/domfreq2.png)  
> When we dont remove the DC offset using detrend, the dominant frequency is 0 because it captures the moving average. When we remove the DC offset, the actual dominant frequency is 1.764Hz shown by `print(Freqs[np.argmax(Pxx)])`



> Q. If we don’t remove the DC offset first, how can we index Pxx such that when we calculate argmax, we don’t look at the Pxx[0] (skipping the 0 index).

> A. We can add the following code (below) to the previous code (above) while removing the line `s=HR.detrend(s,fs)`
> **Code:**
> 
>     while np.argmax(Pxx) == 0:
>        Pxx = np.delete(Pxx, 0)
>        Freqs = np.delete(Freqs, 0)
>
>     plt.clf()
>     plt.plot(Freqs, Pxx)
>     plt.show()
> The code will detect the captured moving average (which is usually at the 0hz mark) and therefore effectively showing the actual dominant frequency

> Q. What is the dominant frequency for the y and z acceleration in the sample?

> A. domfreq of y = 1.764, domfreq of z = 1.96
> **Plots y-accel:**  
>![Image of Challenge](fig/ydomfreq.png)  
> **Plots z-accel:**  
>![Image of Challenge](fig/zdomfreq.png)  

## Challenge 1:

### Low Pass Filter 
**Code:**  

    filter_order = 3
    filter_cutoff = 5/(fs/2)
    b,a = signal.butter(filter_order, filter_cutoff, btype='lowpass')

    s_filt = signal.lfilter(b,a,s)
    w, h = signal.freqz(b,a)

**Plot:**  
![Image of Challenge](fig/l5ch1.png)


> Q. Looking at the documentation for signal.butter, how would you make a high pass filter with a cut off of 0.8Hz? Of the previous time based filters in Lab 4, which filter is most like the high pass filter?

> A.
> **Code:**  
>
>     filter_order = 3
>     filter_cutoff = 0.8
>     b,a = signal.butter(filter_order, filter_cutoff, btype='highpass')
>
>     s_filt = signal.lfilter(b,a,s)
>     w, h = signal.freqz(b,a)
>**Plot High Pass Filter:**  
> ![Image of Challenge](fig/l5ch1.2.png)
> Based on the previous time based filter, signal_diff() seems most like a high pass filter while moving_average() seemed most like a low pass. 


## Challenge 2: What is the Frequency Content of the PPG

**Plot:**    
![Image of Challenge](fig/big.png)  
***Note: dominant frequency titled in middle graph of each row*** 

> Q. How does the dominant frequency change with regards to the heart rate?

> A. The dominant frequency increases when heart rate increases.  
> `HeartRate(BPM) ÷ Dominant frequency(Hz) ≈ 60`
> The above equation shows that if the heartrate goes up, the dominant frequency must also go up to satisfy the equation. I derived this from noticing that the units of HR is `beats per minute` (beats per 60 seconds) and dominant frequency's units are `Hz` (beats per second). 

> Q. If the heart rate is 65BPM, what is approximately the fundamental frequency? What about the second and third harmonic? Why is it that even though the heart rate is 65BPM, there are higher frequency content than just the fundamental frequency? What does this imply about how you should be setting your sampling rate if you expect a heart rate maximum of 180BPM?

> A. Using the above equation, the approximate fundamental frequency for 65 BPM is `≈ 65/60 or 1.083Hz`.  The second and third harmonics are `≈ 1.08HZ*2 or 2.16Hz` and `1.08HZ*3 or 3.25Hz`. 

> A. Since a heart rate signal, it is not a perfect sinusoidal wave there will be other frequencies other than the fundamental frequency. These frequencies can be noise or other captured impurities like the moving average. Even with a noise-filtered and detrended signal, a heart rate signal is still triangular-like which could possibly require other harmonics to build the signal. 

> A. This might imply that for a Max HR of 180 BPM, we would only care about the dominant frequency which is 3Hz. According to the nyquist rate theory, the minimum sampling rate would be 6Hz, but in practice we would like to do at least 12Hz (4x the max)
 
## Challenge 3: Calculate Heart Rate with Frequency Domain Features

> Q. What are some failure modes of your frequency domain solution?

> A. 

> Q. Compare and contrast the two different algorithms. Which has a lower error? Which has a bias closer to 0? Do you see any signs of mean tracking in either algorithm? Use the correlation and difference plots to support your argument.

> A.

## Part 2

## Tutorial 1: Collecting Data

## Tutorial 2: List All Files in Directory

> Q. what is the correct regex to get trial “0” for any subject given our naming convention “ID_Trial_HR.csv”.

> A.

## Tutorial 3: Manipulating Filenames

## Challenge 4: Data for ML

> Q. According to the lecture, what is the recommended split between training and testing on a small dataset?

> A.

> Q. Why is it important to split on subjects and not to treat each file as an independent sample?

> A.

## Challenge 5: Gaussian Mixture Model for Heart Rate

> Q. What is the difference between leave-one-out validation and leave-one-subject-out validation? Which are we doing and why is this important, and why would it be an issue if we used the other validation method given what we are building?

> A.

## Challenge 6: OOP