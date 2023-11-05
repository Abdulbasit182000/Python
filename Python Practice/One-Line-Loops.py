#!/usr/bin/env python
# coding: utf-8

# In[1]:


squares=[]
for i in range(0,10):
    if(i%2==0):
        squares.append(i**2)
print(squares)


# In[2]:


squares=[i**2 for i in range(0,10) if(i%2==0)]


# In[3]:


squares


# In[4]:


list1=[1,4,5,8,9,11,13,12]
list2=[x+1 if x%2==0 else x for x in list1]
list2


# In[ ]:




