#!/usr/bin/env python
# coding: utf-8

# 1. Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them




fname=input("Enter First Name:")
lname=input("Enter Last Name:")
print(lname + " " + fname)


# 2. Write a Python program to display the first and last colors from the following list.  
# color_list = ["Red","Green","White" ,"Black"]

color_list = ["Red","Green","White" ,"Black"]
first_color=color_list[0]
last_color=color_list[len(color_list)-1]
print(first_color,last_color)


# 3. Write a Python program to get the difference between a given number and 17, if the number is greater than 17 return double the absolute difference.


num=input("Enter a number:")
x=int(num)
if (x>17):
    y=abs(x-17)
    print(y*2)
else:
    y=abs(17-x)
    print(y)


# 4. Write a Python program to calculate the sum of three given numbers, if the values are equal then return thrice of their sum


x=int(input("Enter a number:"))
y=int(input("Enter a number:"))
z=int(input("Enter a number:"))
sum=0
if(x==y and x==z):
    sum=3*(x+y+z)
else:
    sum=(x+y+z)
print(sum)


# 5. Write a Python program to count the number 4 in a given list.



x=[1,2,3,4,5,4,6,4,7,4,4]
count=0
for i in range(0,len(x),1):
    if(x[i]==4):
        count+=1
print(count)


# 6. Print table of 24, 50 and 29 using loop.



def tables(x):
    for i in range(1,11):
        print(x*i)
tables(29)


# 7. Print the following patterns using loop :
# *
# **
# ***
# ****



for i in range(1,5):
    for j in range(0,i):
        print("*",end="")
    print()






