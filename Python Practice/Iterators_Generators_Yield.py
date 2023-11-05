#!/usr/bin/env python
# coding: utf-8

# Write a generator which computes the running average.

# In[11]:


def runningavg(li):
    sum=0
    count=0
    for i in li:
        sum+=i
        count+=1
        yield sum/count
numbers=[1,2,3,4,5]
avg=runningavg(numbers)


# In[12]:


for i in avg:
    print(i)


# Write a generator frange, which behaves like range but accepts float values.

# In[39]:


def ran(start,stop,step):
    while(start<stop):
        yield start
        start+=step
ra=ran(2.1,6,0.3)


# In[40]:


for i in ra:
    print(i)


#  Write a generator trange, which generates a sequence of time tuples from start to stop incremented by step. A time tuple is a 3-tuple of integers: (hours, minutes, seconds) So a call to trange might look like this:trange((10, 10, 10), (13, 50, 15), (0, 15, 12) )

# In[45]:


def trange(start,stop,step):
    start=list(start)
    stop=list(stop)
    step=list(step)
    while(start<stop):
        yield (tuple(start))
        #second
        start[2]=start[2]+step[2]
        if(start[2]>=60):
            start[2]=start[2]-60
            start[1]=start[1]+1
        #minute
        start[1]=start[1]+step[1]
        if(start[1]>=60):
            start[1]=start[1]-60
            start[0]=start[0]+1
        #Hour
        if(start[0]>=24):
            start[0]=start[0]-24
tim=trange((10, 10, 10), (13, 50, 15), (0, 15, 12))
for i in tim:
    print(i)


# In[ ]:




