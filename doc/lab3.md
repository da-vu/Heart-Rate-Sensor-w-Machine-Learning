# ECE16 LAB 3 REPORT
Dan Vu
A14596430

Date: 02/11/2020
- - -
## Tutorials: 

### Python Basics Tutorial:

> Q. Show the code - Starting with a = “Hello World!!!”, come up with a code that will give us b = “Hello” and c = “World” and d = “!!!” . Also, in code, check if “ello” is in a.

> A.
>
>     a = "Hello World!!!"
>     b = a[:5]
>     c = a[6:11]
>     d = a[11:]
> 
>     if "ello" in a:
>         print(b,c,d)

> Q. In the following code, what is the output of the print statement? Why doesn’t original_list = ['hi','how','are','you']?

> A.
>
>     Output:
>     ['hi', 1, 2, 'you']
> Original list is unchanged because when we defined newer_list = new_list[1:3], the brackets make it so that a new list is created instead of a copy/reference of the original. If we omitted the [1:3], then original_list (as well as new_list) would change accordingly.

### Connecting Arduino and Python

> Q. Try sending without the .encode. What happens?

> A. There is a python error
>
>     TypeError: unicode strings are not suppported, please encode to bytes: 'Hello World\n'

> Q. Identify in the above code, (1) which python command prints to the python’s own console, and (2) which python command prints to the serial port to the MCU?

> A.  
> `print(ser.name)` prints to the python console.  
> `ser.write(S.encode('utf-8'))` prints to the MCU serial port 


> Q. What happens if you take out the \n in the string? Why?

> A. Without the \n, the message is still sent to the serial, but it is stored in the character buffer and not printed into the OLED. This is because the code in the arduino is set to print to the OLED when it detects '\n'

> Q. Describe the output you observe on the Python side? 

> A. The output is what you would expect on the serial monitor from arduino but only 30 bytes before it prints and closes the serial.

> Q. Change the code to read 10 bytes instead of 30. Now what do you get? What are the 10 bytes you received? Remove decode might help you understand

> A. This time, the ser.read only reads 10 bytes instead of 30 bytes. Some hidden bytes are the '\n' and '\r' which can be seen when you remove the .decode. 

### Receiving a Byte at a Time

> Q. Describe the output you observe on the Python side? Is it the same as before? What does this tell you about the print() function of python?

> A. This time, it reads and appends all 30 bytes into a string which then prints it all out at once. 


### Knowing when to quit

> Q. We purposely made a few errors above. What were they?

> A. `Try:` --> `try:`   
> &nbsp;&nbsp;&nbsp; `s = ser.read(1)`  --> `s = ser.read(1).decode('utf-8')`    

### Numpy

###### Numpy Array
> Q. Show the code - Make an Numpy Array called test_array  from a list = `[0,10,4,12]`. Subtract 20 from the test_array, what do you get? What is the shape of the test_array

> A. Code:
>
>     test_array = np.array( [0,10,4,12])
>     print(test_array-20)
>     print(test_array.shape)
>     print(test_array.dtype)
> Output:
>
>     [-20 -10 -16  -8] # array after subtracting 20
>     (4,) # shape of array 4x1
>     int32

> Q. Show the code - Make a 2D array of test_2D_array from:  
> `[0,10,4,12]`  
> `[1,20,3,41]`  

> A. Code: 
> 
>     test_2D_array = np.array([(0,10,4,12),
>                               (1,20,3,41)])
>     print(test_2D_array.shape)

###### Zeros and Ones
> Q. Make a 2D array of zeros with shape of 10x20 and then print it out

> A. Code: `print(np.zeros((10,20)))`

###### hstack and vstack
> Q. Show the code - Out of the test_array, create the following using hstack and vstack.
>
>     [0,10,4,12,0,10,4,12]
>     [0,10,4,12,0,10,4,12]
>     [0,10,4,12,0,10,4,12]
>     [0,10,4,12,0,10,4,12]

> A. Code:
> 
>     test_array = np.array([0,10,4,12])
>     h_arr = np.hstack((test_array, test_array))
>     v_arr = np.vstack((h_arr,h_arr))
>     final_arr =np.vstack((v_arr,v_arr))
>     print(final_arr)

###### arange
> Q. Show the code - Using arange, make an array called arange_array1 to equal `[-3, 3,9,15]` and arange_array2 to equal `[ -7,  -9, -11, -13, -15, -17, -19]`

> A. Code:
> 
>     arange_array1 = np.arange(-3,16,6)
>     arange_array2 = np.arange(-7,-20,-2)
>     print(arange_array1)
>     print(arange_array2)

###### linspace
>   Q. Make an array call linspace_array using linspace that goes from 0 to 100 with 49 steps. 

> A. Code:
>
>     linspace_array = np.linspace(0,100,num=49)
>     print(linspace_array)


> Q. How does linspace and arange differ? When might you use one over the other?

> A. linspace arranges the array with evenly spaced samples or steps, where you specify the number of steps. It also ends exactly on the end point. arange arranges the array with evenly stepped elements but you specify the step yourself. arange may end before the endpoint if the specified step exceeds the endpoint. You might want to use linspace when you want evenly spaced steps in a range but you dont know how large each step should be. 

###### Indexing and slicing
> Q. What is an array of size 3x4 that would produce the following results. Show your work on how you deduced your answer on paper or some kind of graphics :
>
>     print(e[0])     >>> [12 3 1 2]
>     print(e[1,0])   >>> 0
>     print(e[:,1])   >>> [3 0 2]
>     print(e[2, :2]) >>> [4 2]
>     print(e[2, 2:]) >>> [3 1] 
>     print(e[:,2])   >>> [1 1 3]
>     print(e[1,3])   >>> 2

> A.  
> `print(e[0])     >>> [12 3 1 2]` --> first row = [(12, 3, 1, 2)]  
> `print(e[1,0])   >>> 0` --> row 2, column 1 = 0   
> `print(e[:,1])   >>> [3 0 2]` --> column 2 = [(3, 0, 2)]  
> `print(e[2, :2]) >>> [4 2]` --> first 2 elements of 3rd row = [(4, 2)]  
> `print(e[2, 2:]) >>> [3 1] ` --> row 3, last elements 3rd and 4th elements = [(4, 2)]  
> `print(e[:,2])   >>> [1 1 3]` --> column 3 = [(1,1,3)]  
> `print(e[1,3])   >>> 2` --> row 2, column 4 = 2  

###### setting values of array

> Q. Show your code - Now solve the above indexing and slicing problem by writing the code using array assignment.

> A. Code:
>
>     e = np.zeroes((3,4))
>     e[1,0] = 0
>     e[:,1] = [(3, 0, 2)]
>     e[2, :2] = [(4, 2)]
>     e[2, 2:] = [(3,2)]
>     e[:,2] = [(1,1,3)]
>     e[1.3] = 2
>
>Output:
>
>     [[0. 3. 1. 0.]
>     [0. 0. 1. 2.]
>     [4. 2. 3. 2.]]

###### Setting values of array from comma separated values

> Q. Using fromstring, vstack, and a for loop, create an array of 100x4 from s:  
> `[[1,2,3,4],[1,2,3,4],[1,2,3,4]…..[1,2,3,4]]`

> A. Code:  
>
>     s = '1,2,3,4'
>     print(s)
>     arr = np.fromstring(s,dtype=int,sep=',')
>     final_array = arr
>     for x in range(100):
>         final_array = np.vstack((final_array,arr))
>     print(final_array)

- - - 
## Challenges:

### Challenge 1: Setting your Watch to Send Data

> Q. What happens if you don’t decode the incoming char?

> A. 

> Q. Try removing the logic for checking if the data_array is empty and always vstack even if the data_array is empty. What is the error that gets thrown? Why?

> A.

> Q. Try removing the 1 second delay on the MCU when starting data sending. Describe what happens?

> A.

### Challenge 2: Reading Accelerometer Data

>Q. What happens if you don’t decode the incoming char?

> A.

> Q. Try removing the logic for checking if the data_array is empty and always vstack even if the data_array is empty. What is the error that gets thrown? Why?

> A.

> Q. Try removing the 1 second delay on the MCU when starting data sending. Describe what happens?

> A.

### Challenge 3: Calculate the Sampling Rate

> Q. Start with Baud rate of 115200. What is your calculated sampling rate when you set the sampling rate to 10Hz,50Hz,100Hz,1000Hz on the MCU. Make a plot (using a spreadsheet program) of the actual sampling rate (y-axis) vs expected sampling rate (x-axis).

> A.

> Q. How does this change with Baud rate 9600 vs 115200 vs 230400 vs 460800. For 1000Hz, make a plot of the actual sampling rate (y-axis) vs Baud Rate (x-axis).

> A.

>Q. What happens if you use millis instead of micros for timing and Why?

> A.
- - -
## Part 2

### Challenge 4

> In a video, show the MCU unplugged from USB and powered by the battery. Use the Python code to request the device to send a chunk of data and calculate the sampling rate. 

> A