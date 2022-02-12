#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1. 1.	Write a Python program to print "Hello Python"
print("hello Python")


# In[2]:


#2. 2.	Write a Python program to do arithmetical operations addition and division
a=int(input("enter first number"))


# In[3]:


b=int(input("enter second number"))


# In[4]:


print(a+b)


# In[5]:


print(a/b)


# In[7]:


#3. 3.	Write a Python program to find the area of a triangle
a=float(input("Enter first side"))
b=float(input("Enter second side"))
c=float(input("Enter third side"))

s=(a+b+c)/2
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print('The area of the triangle is %0.2f' %area)


# In[10]:


#4. Write a Python program to swap two variables
a=input("enter first value")
b=input("enter second value")
c=a
print("values before swapping:\n a: {} \n b: {} ".format(a,b))
a=b
b=c
print("values before swapping:\n a: {} \n b: {} ".format(a,b))


# In[12]:


#5.	Write a Python program to generate a random number
import random
p=random.random()
print(p)


# In[ ]:




