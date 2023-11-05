#!/usr/bin/env python
# coding: utf-8

# Parameterised Decorator: Create a decorator @repeat(n) that repeats the decorated function n times. It should also accept an argument for whether to print the results each time. Apply this decorator to a simple function

# In[35]:


def repeat(n):
    def my_decorator(func):
        def my_wrapper(x):
            for i in range(0,n):
                print(func(x))
        return my_wrapper
    return my_decorator

@repeat(3)
def foo(x):
    return x+1


# In[36]:


foo(10)


# Timing Decorator: Write a decorator @timing that measures the time it takes for a function to execute and prints the execution time. Apply this decorator to various functions and compare their execution times.

# In[7]:


import time

def timing_decorator(func):
    def helper(*args, **kwargs):
        s=time.time()
        y=func(*args, **kwargs)
        e=time.time()
        result=e-s
        print(result)
        return y
    return helper

@timing_decorator
def func(y):
    return y+1
@timing_decorator
def isln(str1,str2):
    if((str1 in str2) or (str2 in str1)):
        return True
    else:
        return False
@timing_decorator
def name(y):
    str1=input("Enter your name:")
    if(str1==y):
        return True
    else:
        False


# In[8]:


func(13)


# In[9]:


isln("ban","banana")


# In[10]:


name('Ali')


# Basic Decorator:Create a decorator called @uppercase_decorator that converts the result of a function to uppercase. Apply this decorator to a function that returns a string and test it.

# In[11]:


def uppercase_decorator(func):
    def helper(*args, **kwargs):
        x=func(*args, **kwargs)
        x=x.upper()
        return x
    return helper

@uppercase_decorator
def name():
    str1=input("Enter tour name:")
    return str1


# In[12]:


name()


# In[ ]:




