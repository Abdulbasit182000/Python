#!/usr/bin/env python
# coding: utf-8

# In[1]:


def func(myit):
    while(True):
        try:
            print(next(myit))
        except:
            print("List finished")
            break


# In[2]:


x=[1,2,3,4,5]
myit=iter(x)
func(myit)


# In[6]:


x='abcd'
if not type(x) is int:
    raise TypeError("X should be an integer")


# In[ ]:




