#!/usr/bin/env python
# coding: utf-8

# In[17]:


f=open("demofile.txt",'r')


# In[18]:


for x in f:
    print(x)
f.close()


# In[19]:


f=open("demofile.txt",'a')
f.write("file has more lines now")
f.close()


# In[26]:


f=open('mytext.txt','x')


# In[27]:


f.close()


# In[28]:


import os
if os.path.exists("mytext.txt"):
    os.remove("mytext.txt")
else:
    print("File does not exist")


# In[ ]:




