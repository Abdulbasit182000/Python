#!/usr/bin/env python
# coding: utf-8

# Itertools

# In[19]:


from itertools import compress
shapes = ['circle', 'triangle', 'square', 'pentagon']
selections = [ 'a' in i for i in ['a','b','ac','da']  ]
result = compress(shapes, selections)


# In[20]:


for each in result:
    print(each)


# In[18]:


from itertools import filterfalse
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = filterfalse(lambda x:x<4, data)
for each in result:
    print(each)


# In[23]:


from more_itertools import flatten
x=(0, 1)
y=[2,3]
iterable = [x, y]
list(flatten(iterable))


# In[24]:


from more_itertools import chunked
iterable = [0, 1, 2, 3, 4, 5, 6, 7, 8]
list(chunked(iterable, 6))


# In[25]:


from itertools import chain
colors = ['red', 'orange', 'yellow', 'green', 'blue']
shapes = ['circle', 'triangle', 'square', 'pentagon']
result = chain(colors, shapes)
for each in result:
    print(each)


# In[27]:


from itertools import takewhile
result = takewhile(lambda x: x<5, [1,4,4,6,1,])
list(result)


# In[28]:


from itertools import zip_longest
colors = ['red', 'orange', 'yellow', 'green', 'blue',]
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,]
for each in zip_longest(colors, data, fillvalue=None):
    print(each)


# In[29]:


from itertools import dropwhile
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1]
result = dropwhile(lambda x: x<5, data)
for each in result:
    print(each)


# Functools

# In[30]:


from functools import reduce
print(reduce(lambda x, y: x + y, [1, 2, 3]))


# In[32]:


from functools import reduce
print(reduce(lambda x,y: x+y+1,[1,2,3]))


# In[33]:


from functools import partial

def target_func(arg_one, arg_two):
    print(f"arg_one = {arg_one}, arg_two = {arg_two}")

partial_one = partial(target_func, arg_two="World!")
partial_two = partial(target_func, arg_one="Love")

partial_one(arg_one="Hello")
partial_two(arg_two="Python")


# In[34]:


from functools import partial
def power(n,x):
    print(n**x)
p1=partial(power,x=2)
for i in range(0,10):
    p1(i)


# In[35]:


from functools import cache

@cache
def fibonacci(n):
    if n in [0, 1]:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(4)) # called 5 times
print(fibonacci(11)) # called 7 tim


# In[ ]:




