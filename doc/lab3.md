# ECE16 LAB 3 REPORT
Dan Vu
A14596430

Date: 02/11/2020

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

