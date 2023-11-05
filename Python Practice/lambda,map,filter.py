#!/usr/bin/env python
# coding: utf-8

# In[1]:


sum=lambda x,y: x+y
sum(3,4)


# In[6]:


def fahrenheit(T):
    return ((float(9)/5)*T + 32)
def celsius(T):
    return (float(5)/9)*(T-32)
temps=[36.5,37,37.5,38,39]
F=map(fahrenheit,temps)
far=list(F)
C=map(celsius,far)
cel=list(C)


# In[7]:


print(far,cel)


# In[10]:


C = [39.2, 36.5, 37.3, 38, 37.8] 
F = list(map(lambda x: (float(9)/5)*x + 32, C))
print(F)


# In[11]:


C = list(map(lambda x: (float(5)/9)*(x-32), F))
print(C)


# In[12]:


fibonacci = [0,1,1,2,3,5,8,13,21,34,55]
x=list(filter(lambda x: x%2!=0,fibonacci))
print(x)


# In[ ]:




