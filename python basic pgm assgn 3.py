#!/usr/bin/env python
# coding: utf-8

# In[3]:


#1. Write a Python Program to Check if a Number is Positive, Negative or Zero?
num = int(input("enter the number : "))
if (num == 0):
    print("The number is zero!")
elif (num < 0):
    print("The number is negative!!")
else:
    print("The number is positive!!!!")


# In[5]:


#2. Write a Python Program to Check if a Number is Odd or Even?
num = int(input("enter the number : "))
if (num % 2 == 0):
    print("Even number ")
else:
    print("ODD number")


# In[20]:


#3. Write a Python Program to Check Leap Year?
year=int(input("input the year : "))
if(year % 4 == 0) and (year % 100 != 0):
    print("It is a leap year")
elif(year % 100 == 0) and (year % 400 == 0):
    print("It is a leap year")
else:
    print("It is NOT a leap year")


# In[29]:


# 4. Write a Python Program to Check Prime Number?
num = int(input("enter the number to check : "))
c=0
for i in range(2,num):
    if (num%i == 0):
        c=c+1
if(c == 0):
    print("It is a prime number")
else:
    print("It is not a prime number")


# In[31]:


#5. Write a Python Program to Print all Prime Numbers in an Interval of 1-10000
c=0
for i in range(1,10001):
    for j in range(1,i+1):
        if(i%j == 0):
            c = c+1
    if(c==2):
        print("prime : ", i)
    c=0


# In[ ]:




