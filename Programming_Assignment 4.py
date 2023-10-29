#!/usr/bin/env python
# coding: utf-8

# Convert a non-negative integer to its English words representation and print in
# reverse if total characters in English words are more than total words in a
# sentence.

# In[14]:


def numtoeng(str1, multiple):
    numbers = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
    tens = ['Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
    leng = len(str1)
    num = int(str1)
    str2 = ""

    if leng == 1:
        str2 = str2 + numbers[num]
    elif leng == 2:
        if num < 20:
            str2 = str2 + numbers[num]
        else:
            y = int(str1[0])
            str2 = str2 + tens[y - 2]
            y = int(str1[1])
            if y == 0:
                pass
            else:
                str2 = str2 + " " + numbers[y]
    else:
        y = int(str1[0])
        str2 = str2 + numbers[y] + " Hundred"
        num = str1[1:]
        num = int(num)
        if num < 20:
            str2 = str2 + " and " + numbers[num]
        else:
            y = int(str1[1])
            if y != 0:
                str2 = str2 + " and " + tens[y - 2]
                y = int(str1[2])
                if y != 0:
                    str2 = str2 + " " + numbers[y]

    return str2 + " " + multiple


# In[20]:


x = '1234567'
num = 0
multi = 1
count = 0
Multiple = [' ',' Thousand', ' Million', ' Billion', ' Trillion']
li = []
mu = 0

if len(x) <= 3:
    str1 = ""
    for i in range(0, len(x), 1):
        str1 = str1 + x[i]
    y = numtoeng(str1, " ")
    li.append(y)
else:
    for i in range(len(x) - 1, -1, -1):
        if i == 0:
            num = (int(x[i]) * multi) + num
            num = str(num)
            y = numtoeng(num, Multiple[mu])
            li.append(y)
        else:
            if count != 3:
                num = (int(x[i]) * multi) + num
                multi = multi * 10
                count = count + 1
            if count == 3:
                num = str(num)
                y = numtoeng(num, Multiple[mu])
                li.append(y)
                mu = mu + 1
                count = 0
                num = 0
                multi = 1

if count > 0:
    num = str(num)
    y = numtoeng(num, Multiple[mu])
    li.append(y)

str2=""
for j in range(len(li)-1,-1,-1):
    str2=str2+" "+li[j]
print(str2)


# Given an input n, count the total number of digit 1 appearing in all nonnegative integers less than or equal to n.
# For example:
# Given n = 13,
# Return 6, because digit 1 occurred in the following numbers: 1, 10, 11, 12, 13

# In[8]:


def count1(n):
    count=0
    while(n>0):
        rem=n%10
        if(rem==1):
            count+=1
        n=int(n/10)
    return count


# In[13]:


num=int(input("Enter a number:"))
sum=0
for i in range(0,num,1):
    x=count1(i+1)
    sum=sum+x
print(sum)


# Given an array, Rotate (shift left) an array of n elements to the right by k steps.
# For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated
# to [5,6,7,1,2,3,4].
# After rotating the array add in into another array and display array index with
# minumum value.

# In[1]:


def leftshift(k,x):
    arr=[]
    y=len(x)
    start=y-k
    for i in range(start,y):
        arr.append(x[i])
    for i in range(0,start):
        arr.append(x[i])
    return arr

x=[1,2,3,4,5,6,7]
leftshift(3,x)


# You are given an n x n 2D matrix representing an image.
# Rotate the image by 180 degrees (anti-clockwise) but after sorting the n*n 2D array

# In[22]:


mat = [
    [4, 9, 8],
    [7, 6, 2],
    [1, 3, 5]
]
n = len(mat)
x = []

for i in mat:
    for j in i:
        x.append(j)

x.sort()
m=0
for i in range(0,len(mat),1):
    for j in range(0,len(mat),1):
        mat[i][j]=x[m]
        m+=1
        


# In[29]:


x=[]
for i in range(n-1,-1,-1):
    for j in range(n-1,-1,-1):
        x.append(mat[i][j])
m=0
for i in range(0,len(mat),1):
    for j in range(0,len(mat),1):
        mat[i][j]=x[m]
        m+=1
print(mat)


# Given a string containing just the characters '(' and ')', find the length of the longest
# and shortest valid (well-formed) parentheses substring.
# For "(()", the longest valid parentheses substring is "()", which has length = 2.
# Another example is ")()())", where the longest valid parentheses substring is "()()",
# which has length = 4

# In[26]:


#lets find all possible substrings
x=[]
s=")()())"
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


# In[27]:


def real(x):
    while True:
        if '()'in x:
            x=x.replace('()','')
        else:
            return not x  
            
        


# In[28]:


count=0
for i in range(0,len(x),1):
    if (real(x[i])==True):
        y=len(x[i])
        if(y>=count):
            count=y
print(count)
    


# In[ ]:




