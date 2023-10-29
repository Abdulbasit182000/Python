#!/usr/bin/env python
# coding: utf-8

# Write a program which should count Vowels in the strings and return vowels in
# reverse order.

# In[1]:


Vowels=['A','a','E','e','I','i','O','o','U','u']
x="Hello World"
j=-1
reverse_list=[]
count=0
for i in range(0,len(x),1):
    y=x[j]
    if y in Vowels:
        reverse_list.append(y)
        count+=1
    j=j-1
print(count,reverse_list)


# Write a function which should add the two vowels in the arrays and generate
# third array

# In[2]:


Vowels=['A','a','E','e','I','i','O','o','U','u']
x="Hello World"
w="What is up"
li=[]
for i in range(0,len(x),1):
    y=x[i]
    if y in Vowels:
        li.append(y)
for i in range(0,len(w),1):
    y=w[i]
    if y in Vowels:
        li.append(y)
print(li)


# Given a string and a non-negative int a, return a larger string that is n copies of
# the original string.

# In[8]:


def string_times(st,count):
    i=0
    stw=""
    while(i<count):
        stw=stw+st
        i+=1
    return stw


# In[14]:


print(string_times("Hi",5))


# Given an array of ints, return True if .. 1, 2, 3,.. appears in the array
# somewhere.

# In[23]:


arr=[1,1,2,1,2,3]
a=False
for i in range(0,len(arr),1):
    if((i+2)<len(arr)):
        if(arr[i]==1 and arr[i+1]==2 and arr[i+2]==3):
            a=True
            break
print(a)
    


# Given 2 arrays of ints, a and b, return True if they have the same first element or
# they have the same last element. Both arrays will be length 1 or more.

# In[28]:


arr1=[1,2,3]
arr2=[1,3]
x=len(arr1)
y=len(arr2)
a=False
if(arr1[0]==arr2[0]or arr1[x-1]==arr2[y-1]):
    a=True
print(a)


# Given 3 int values, a b c, return their sum. However, if one of the values is the
# same as another of the values, it does not count towards the sum.

# In[38]:


def sumcheck(num,x):
    count=0
    for i in range(0,len(x),1):
        if(num==x[i]):
            count+=1
    return count

def lone_sum(a,b,c):
    x=[]
    x.append(a)
    x.append(b)
    x.append(c)
    sum=0
    for i in range(0,len(x),1):
        if(sumcheck(x[i],x)<2):
            sum=sum+x[i]
    return sum


# In[41]:


lone_sum(3,3,3)


# You are provided a string with only digits [0 - 9], your task is to count the
# number of subsequences of string divisible by 6.
# For e.g. The given string is 1234566
# The subsequences divisible by 6 are 12, 24, 36, 6, 6, 66
# Hence the answer should be 6

# In[1]:


s="1234566"
x=[]
new_str=""
leng=len(s)
while(s!=""):
    for i in range(0,leng,1):
        new_str=new_str+s[i]
    x.append(new_str)
    new_str=""
    leng=leng-1
    if(leng==0):
        s=s[1:]
        leng=len(s)
print(x)


# In[4]:


count=0
for i in range(0,len(x),1):
    num=int(x[i])
    if(num%6==0):
        count=count+1
print(count)


# Write a the function LongestWord (sen) take the sen parameter being passed and
# return the largest word in the string. If there are two or more words that are the
# same length, return the first word from the string with that length. Ignore
# punctuation and assume sen will not be empty.

# In[6]:


def LongestWord(sen):
    word=sen.split()
    x=len(word[0])
    wo=word[0]
    for i in range(0,len(word),1):
        if(len(word[i])>x):
            x=len(word[i])
            wo=word[i]
    print(wo)
LongestWord("This is my sentence")
    


# Write a function AlphabetSoup(str) take the str string parameter being passed
# and return the string with the letters in alphabetical order (ie. hello becomes
# ehllo). Assume numbers and punctuation symbols will not be included in the
# string.

# In[7]:


def  AlphabetSoup(str1):
    x=[]
    for i in range(0,len(str1),1):
        x.append(str1[i])
    x.sort()
    print(x)
AlphabetSoup('HELLO')
        


# In[ ]:




