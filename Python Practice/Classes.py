#!/usr/bin/env python
# coding: utf-8

# Property

# In[ ]:


class Celsius:
    def __init__(self, temperature=0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    def get_temp(self):
        print("getting value")
        return self.temperature

    def set_temp(self, temp):
        print("setting value")
        self.temperature = temp

    temperature = property(get_temp, set_temp)

cel = Celsius(37)
print(cel.temperature)
print(cel.to_fahrenheit())


# ClassMethod

# In[7]:


class Student:
    def __init__(self,Marks=0):
        self.Marks=Marks
    
    def totalmarks(self,Mar):
        self.Marks=Mar
        x=str(Mar)
        print(f"Total marks are: " + x)
Student.printmarks=classmethod(Student.totalmarks)
Student.printmarks(88)


# StaticMethod

# In[10]:


class mathe:
    def adddition(x,y):
        return x+y
mathe.adddition=staticmethod(mathe.adddition)
x=mathe.adddition(6,11)
print(x)


# Custom Data Type

# In[12]:


class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return f"{self.name},{self.age}"
    def sayhello(self):
        print("Hello my name is " + self.name)
obj=Person("Abdul",22)
print(obj)
    


# In[ ]:




