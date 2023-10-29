#!/usr/bin/env python
# coding: utf-8

# Write a function named isIn that accepts two strings as arguments and returns True if either
# string occurs anywhere in the other as a substring, and False otherwise. Hint: you might
# want to use the built-in str operation in.

# In[3]:


def isln(str1,str2):
    if((str1 in str2) or (str2 in str1)):
        return True
    else:
        return False
isln("ban","banana")


# Write a function primeFactor that takes one parameter as its argument and obtain the prime
# factors of the number. Hint: Find all the prime number that multiply together to make the
# original number. e.g. prime factors of 15 are 5 and 3.

# In[1]:


def isprime(num):
    x=num-1
    count=0
    while(x!=0):
        if(num%x==0):
            count+=1
        x=x-1
    if(count==1):
        return True
    else:
        return False


# In[2]:


def primefactor(num):
    x=num-1
    while(x!=0):
        if(num%x==0 and isprime(x)):
            print(x)
        x=x-1
        


# In[3]:


primefactor(42)


# Take an integer number as an input from user, write a function that checks weather a given
# number is Armstrong or not. Hint: If sum of the cubes of each digit of the number is equal to
# the number itself, then the number is called an Armstrong number. For example, 153 = (1 * 1
# * 1) + (5 * 5 * 5) + (3 * 3 * 3)

# In[9]:


def armstrong(num):
    sum=0
    x=num
    while(x>0):
        rem=x%10
        x=int(x/10)
        sum=sum+(rem**3)
    if(sum==num):
        return True
    else:
        return False
armstrong(153)


# Write your own Range function that take three parameters (start, stop and step) as an input
# and return the list of integer numbers.

# In[5]:


def ran(st,so,s):
    li=[]
    for i in range(st,so,s):
        li.append(i)
    return li
x=ran(0,10,1)
print(x)


# Write a function binary2Decimal that take binary number as input and return decimal
# equivalent of the given number.

# In[14]:


def binary2Decimal(num):
    x=1
    sum=0
    while(num>0):
        rem=num%10
        if(rem==1):
            sum=sum+x
        num=int(num/10)
        x=x*2
    return sum
binary2Decimal(1010)


# Write a function Multiple that considers a pair of integers and determines whether the
# second integer is the multiple of the first or not. The function should take two integers as
# arguments and return True if the second is a multiple of the first, and False otherwise.

# In[17]:


def multi(f,s):
    if(s%f==0):
        return True
    else:
        return False
multi(3,10)


# Write a function that displays a solid square of a character whose side and the character to be
# printed are specified in integer and character as the function parameters. For example, if side
# is 5 and character is ‘#’, the function should display:
# #####
# #####
# #####
# #####
# #####

# In[21]:


def prin(num,cha):
    for i in range(0,num):
        for j in range(0, num):
            print(cha,end="")
        print()
prin(5,'#')


# An integer number is said to be a perfect number if its factors, including 1 (but not the
# number itself), sums up to the number. For example, 6 is a perfect number because 6 = 1 + 2
# + 3. Write a function perfect that determines whether parameter number is a perfect number.
# Use this function in a program that determines and prints all the perfect numbers between 1
# and 1000.

# In[23]:


def perfec(num):
    x=num-1
    count=0
    sum=0
    while(x!=0):
        if(num%x==0):
            sum=sum+x
        x=x-1
    if(sum==num):
        return True
    else:
        return False
for i in range(1,1001,1):
    if perfec(i):
        print(i)


# Write a program that simulates coin tossing. For each toss of the coin, the program should
# print Heads or Tails. Let the program toss the coin 100 times, and count the number of times
# each side of the coin appears and then print the results. The program should call a separate
# function flip that takes no arguments and returns 0 for tails and 1 for heads. Note: To get
# random 1 or 0 you can import a random module and then use random.randint(0,1)

# In[24]:


import random
def flip():
    return random.randint(0,1)
head=0
tail=0
for i in range(0,100):
    x=flip()
    if(x==0):
        tail+=1
    else:
        head+=1
print(head,tail)
    


# Declare a list of 10 random integers and then find mean, median and mode of integers.

# In[30]:


def cou(num,li):
    count=0
    for i in range(0,len(li),1):
        if(num==li[i]):
            count+=1
    return count


# In[31]:


li=[1,2,3,4,5,6,7,8,9,10]
sum=0
count=0
for i in range(0,len(li),1):
    sum=sum+li[i]
print(sum/len(li))
li.sort()
median=(li[4]+li[5])/5
print(median)
mode=li[0]
count=cou(li[0],li)
for i in range(0,len(li),1):
    x=cou(li[i],li)
    if(x>=count):
        mode=li[i]
print(mode)


# Declare a list of 20 integers that has duplicate numbers, write a program to delete duplicate
# numbers from list.

# In[6]:


random_list = [5, 12, 7, 3, 8, 15, 7, 10, 4, 6, 12, 19, 11, 5, 2, 16, 9, 3, 17, 8]
x=[]
for i in random_list:
    if i not in x:
        x.append(i)
print(x)


# Write a function that takes a tuple of 10 number as a parameter and return the minimum of all
# the numbers.

# In[8]:


def mini(x1,x2,x3,x4,x5,x6,x7,x8,x9,x10):
    x=[]
    x.append(x1)
    x.append(x2)
    x.append(x3)
    x.append(x4)
    x.append(x5)
    x.append(x6)
    x.append(x7)
    x.append(x8)
    x.append(x9)
    x.append(x10)
    m=x[0]
    for i in x:
        if (m>i):
            m=i
    return m
mini(5,7,8,9,1,2,3,4,6,110)


# Write a program that take 10-time, name (string) and marks (integer) as an input from the
# user. Populate a list such that all even indices have name and odd indices with the
# corresponding marks. e.g. [‘Ahmad’, 29, ‘Asad’, 15, ‘Zainab’, 20]. At the end print the list.
# Hint: You can use append function of list data type.

# In[35]:


li=['Ahmad', 29, 'Asad', 15, 'Zainab', 20]
for i in range(0,len(li),2):
    print(li[i],li[i+1])


# Implement a program that starts by asking the user to enter a login id (i.e., a string). The
# program then checks whether the id entered by the user is in the list ['Ahmad', 'Zainab',
# 'Hina', 'Ali'] of valid users. Depending on the outcome, an appropriate message should be
# printed. Regardless of the outcome, your function should print “Done” before terminating.
# Here is an example of a successful login:

# In[9]:


li=['Ahmad', 'Zainab', 'Hina', 'Ali']
name=input('Enter your name:')
if name in li:
    print('You are in')
else:
    print('Login Failed')
print('Done')


# Take a name (i.e., a string) as an input from the user and insert it into a list, then pass this list
# to a function swap that exchange the first and last values of list. After swapping print the
# resultant list.

# In[11]:


def swap(li):
    n=len(li)
    temp=li[0]
    li[0]=li[n-1]
    li[n-1]=temp
    print(li)


# In[12]:


li=['Ahmad', 'Zainab', 'Hina', 'Ali']
name=input('Enter your name:')
li.append(name)
swap(li)


# Write a for loop that iterates over a list of strings myList and prints the first three characters
# of every word. e.g. If myList is the list ['January', 'February', 'March'] thenthe following
# should be printed:

# In[13]:


li= ['January', 'February', 'March']
for i in li:
    print(i[0:3])


# Write a program that requests an integer n from the user and append the squares of all
# numbers from 0 up to, but not including, n. At the end print the list.

# In[42]:


num=int(input("Enter a Number:"))
x=[]
for i in range(0,num):
    x.append(i**2)
print(x)


# 21. Implement a function ion2e() that takes a string as input and returns a copy of the string with
# the following change: if the entered word (input string) ends in 'ion', then 'ion' is replaced
# with 'e', otherwise it returns the same word.

# In[16]:


def ion2e(str1):
    if str1.endswith('ion'):
        return str1[:-3]+'e'
    else:
        return str1
print(ion2e('Completion'))


# In[ ]:




