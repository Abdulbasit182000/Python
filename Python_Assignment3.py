#!/usr/bin/env python
# coding: utf-8

# Implement a function that meets the specification below. Use a try-except block.
# def sumDigits(s):
# """Assumes s is a string
# Returns the sum of the decimal digits in s
# For example, if s is 'a2b3c' it returns 5"""
# 

# In[3]:


def sumDigits(s):
    sum=0
    for i in range (0,len(s),1):
        try:
            sum=sum+int(s[i])
        except:
            pass
    return sum
sumDigits('a2b3c')


# With a given integer number n provided by the user, write a program to generate a dictionary
# that contains {i: i*i} as its key:value pair such that all the integer numbers between 1
# and n are included). At the end, your program should print the dictionary. Suppose the
# following input is supplied to the program:

# In[12]:


x={}
num=int(input("Enter a number:"))
for i in range(0,num):
    x[str(i+1)]=((i+1)*(i+1))
print(x)


# Write a program that accepts a comma separated sequence of words as input and prints the
# words in a comma-separated sequence after sorting them alphabetically. Suppose the
# following input is supplied to the program:
# without,hello,bag,world
# Then, the output should be:
# bag,hello,without,world
# 

# In[23]:


s='without,hello,bag,world'
new_string=''
for i in range(0,len(s),1):
    if(s[i]!=','):
        new_string=new_string+s[i]
    else:
        new_string=new_string+' '
w=new_string.split()
for i in range(0,len(w),1):
    w[i]=w[i].lower()
ans=sorted(w)
new_string=''
for i in range(0,len(w),1):
    new_string=new_string+w[i]+','
i=len(new_string)
print(new_string)

