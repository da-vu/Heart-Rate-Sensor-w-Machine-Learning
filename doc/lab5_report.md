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

> **A.**  
> **Code:**  
>     
>     


> Q. Sketch the correlation plot that would give you an R of 0. What does an R of 0 mean?

> A.

> Q. Sketch a scatter plot of the correlation and bland-altman plot if your estimation was perfect every time. What would be the R, RMSE, Bias, and STD value of a perfect estimator?

> A.

> Q. How might we use the 1.96STD mark to assess if a given estimate might be an outlier?

> A.

> Q. What would your Bland-Altman plot look like if your algorithm always guessed 70BPM regardless of the actual heart rate? Describe some prominent features about the graph beyond just showing it.

> A.


## Tutorial 2: Frequency Domain

> Q. If your sampling rate was 120Hz, what would be your maximum frequency (the Nyquist frequency)?

> A.

> Q. If your signal bandwidth is composed of 0-10Hz, what is your minimum sampling rate to capture this signal based on the Nyquist sampling theorem? What would be recommended in general practice however?

> A.

## Tutorial 3: Baseline DC Signal

> Q. How does your detrend function modify the frequency content of the signal? Show the plot and circle the part that is most modified and explain why.

> A.

## Tutorial 4: Dominant Frequency Component

> Q. Show the code - Use np.argmax to find the actual dominant frequency of the x acceleration (currently labeled as 1Hz in the above plot). The aim here is to use argmax to get the index of the maximum value of Pxx and then use that index to get the corresponding frequency in the Freqs array. Try this with and without removing the DC offset. What do you get?

> A.

> Q. If we don’t remove the DC offset first, how can we index Pxx such that when we calculate argmax, we don’t look at the Pxx[0] (skipping the 0 index).

> A.

> Q. What is the dominant frequency for the y and z acceleration in the sample?

> A.


## Challenge 1:

> Q. Looking at the documentation for signal.butter, how would you make a high pass filter with a cut off of 0.8Hz? Of the previous time based filters in Lab 4, which filter is most like the high pass filter?

> A.

## Challenge 2: What is the Frequency Content of the PPG

> Q. How does the dominant frequency change with regards to the heart rate?

> A.

> Q. If the heart rate is 65BPM, what is approximately the fundamental frequency? What about the second and third harmonic? Why is it that even though the heart rate is 65BPM, there are higher frequency content than just the fundamental frequency? What does this imply about how you should be setting your sampling rate if you expect a heart rate maximum of 180BPM?

> A.

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