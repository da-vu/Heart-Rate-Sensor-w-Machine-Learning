R = correlation coefficieant
rmse = accuracy
std = precision
bias = bias lol

What does an R of 0 mean?
uncorrelated completely, y-values constant

What would be the R, RMSE, Bias, and STD value of a perfect estimator?
R =1, RMSE = 1, Bias = 0, STD = 0?

How might we use the 1.96STD mark to assess if a given estimate might be an outlier?
Anything outside of the 1.96STD marks are outliers

Q. If your sampling rate was 120Hz, what would be your maximum frequency (the Nyquist frequency)?
60 because Fs = 120, Half of the sampling frequency is 60hz which is the highest frequency component that is capture. 


Q. If your signal bandwidth is composed of 0-10Hz, what is your minimum sampling rate to capture this signal based on the Nyquist sampling theorem? What would be recommended in general practice however?
20hz is the minimum nyquist rate. 40 is the practical. 


Q. How does your detrend function modify the frequency content of the signal? Show the plot and circle the part that is most modified and explain why

Q. Looking at the documentation for signal.butter, how would you make a high pass filter with a cut off of 0.8Hz? Of the previous time based filters in Lab 4, which filter is most like the high pass filter?

change b-type to highpass, and change the cut off to 0.8/(fs/2)
signal_diff is most like a high pass filter
moving average is most like a alow pass

how dom freq hange
it go up when heart rate ^^^
dom x 60 ~ hr 
65/60 ~ fundamental freq
/120 second
/180 third 

70/15/15
but we do 70/20/10~9/2/1

sum ppl diff hr, be weird group diff
