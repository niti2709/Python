#!/usr/bin/env python
# coding: utf-8

# In[3]:


#1. Write a Python program to convert kilometers to miles?

d=float(input("enter the kilometers travelled "))
miles= d* 0.621371
print("miles travelled: {} miles".format(miles) )


# In[5]:


#2. Write a Python program to convert Celsius to Fahrenheit?
celcius = float(input("enter the temperature in celcius "))
faren = (celcius * 9/5) + 32
print("temperature in farenheit is : ", faren)


# In[6]:


#3. Write a Python program to display calendar?
import calendar
y = int(input("enter the year "))
m = int(input("enter the month "))
print(calendar.month(y,m))


# In[7]:


#4. Write a Python program to solve quadratic equation?
# Python program to find roots of quadratic equation
import math


# function for finding roots
def equationroots( a, b, c):
    dis = b * b - 4 * a * c
    sqrt_val = math.sqrt(abs(dis))
# checking condition for discriminant
    if dis > 0:
        print(" real and different roots ")
        print((-b + sqrt_val)/(2 * a))
        print((-b - sqrt_val)/(2 * a))

    elif dis == 0:
        print(" real and same roots")
        print(-b / (2 * a))

# when discriminant is less than 0
    else:
        print("Complex Roots")
        print(- b / (2 * a), " + i", sqrt_val)
        print(- b / (2 * a), " - i", sqrt_val)

# Driver Program
a = 1
b = 10
c = -24

# If a is 0, then incorrect equation
if a == 0:
    print("Input correct quadratic equation")

else:
    equationroots(a, b, c)


# In[8]:


#5. Write a Python program to swap two variables without temp variable?
a = 5
b = 6
print("before swapping : ", a,b)
a,b=b,a
print("after swap : ", a, b)


# In[ ]:




