#!/usr/bin/env python
# coding: utf-8

# 1(A)Print the following pattern using for loop:
# **********
# **********
# **********
# **********



for j in range(0,4):
    for i in range(0,10):
        print("*",end="")
    print()


# 1(B): 1 2 3 4 5 6 7 8 9 10 
# 2 4 6 8 10 12 14 16 18 20
#  3 6 9 12 15 18 21 24 27 30 
# 4 8 12 16 20 24 28 32 36 40
#  5 10 15 20 25 30 35 40 45 50



x=[1,2,3,4,5,7,8,9,10]
for j in range(1,6):
    for i in range(0,len(x),1):
        w=str(x[i]*j)
        print(w + " ",end="")
    print()
    
    


# 1(C): 
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5



for i in range(1,6):
    for j in range(0,i):
        w=str(j+1)
        print(w + " ",end="")
    print()


# 2.Write a Python program to multiplies all the items in a list.



x=[1,2,3,4,5,6]
num=1
for i in range(0,len(x),1):
    num=num*x[i]
print(num)


# 3.Write a Python program to get the smallest number from a list.



x=[2,3,4,5,1,6,8]
smol=x[0]
for i in range(1,len(x),1):
    if (x[i]<smol):
        smol=x[i]
print(smol)


# 4.Write a Python program to remove duplicates from a list



x=[1,1,2,5,7,8,1,5,8]
x=list(set(x))
print(x)


# 5.Write a Python program to clone or copy a list.



x=[1,2,3,4,5]
y=x
print(x)
print(y)


# 6. Write a Python program to print a specified list after removing the 0th, 4th and 5th elements. 


x=['Red','Green','White','Black','Pink','Yellow']
x.pop(0)
x.pop(3)
x.pop(3)
    
print(x)


# In[ ]:




