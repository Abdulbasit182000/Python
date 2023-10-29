#!/usr/bin/env python
# coding: utf-8

# Write a program that asks the user to enter two numbers, obtains them from the user and
# prints their sum, product, difference, quotient and remainder.
# 

# In[2]:


x=int(input("Enter a number:"))
y=int(input("Enter a number:"))
sum=x+y
product=x*y
diff=abs(x-y)
if(x>y):
    quo=int(x/y)
    rem=x%y
else:
    quo=int(y/x)
    rem=y%x
print(sum,product,diff,quo,rem)


# The distance between two cities (in km.) is input through the keyboard. Write a program
# to convert and print this distance in meters, feet, inches and centimeters.

# In[6]:


x=int(input("Enter Km:"))
meter=x*1000
feet=x*3280.84
inches=feet*12
centi=meter*100
print(meter,feet,inches,centi)


# Write a program that takes the marks obtained by a student in five different subjects as
# input through the keyboard, then find out the total marks and percentage marks obtained
# by the student in each subject. Assume that the maximum marks that can be obtained by a
# student in each subject is 100.

# In[12]:


u=(input("Enter subject 1 marks:"))
v=(input("Enter subject 2 marks:"))
x=(input("Enter subject 3 marks:"))
y=(input("Enter subject 4 marks:"))
z=(input("Enter subject 5 marks:"))
print(u+'%')
print(v+'%')
print(x+'%')
print(y+'%')
print(z+'%')


# Temperature of a city in Fahrenheit degrees is input through the keyboard. Write a
# program to convert this temperature into Centigrade degrees.
# 

# In[17]:


x=int(input("Enter Temperature:"))
y=str(x-32)
print("The celcius is:"+y)


# The length & breadth of a rectangle are input through the keyboard. Write a program to
# calculate the area & perimeter of the rectangle.
# 

# In[19]:


x=int(input("Enter length of rectangle:"))
y=int(input("Enter breadth of rectabgle:"))
area=str(x*y)
brea=str(x+y+x+y)
print("The area is:"+area)
print("The Breadth is:"+brea)


# Two numbers (base and exponent) are entered through the keyboard. Write a program to
# find the value of base raised to the power of exponent.

# In[20]:


x=int(input("Enter base:"))
y=int(input("Enter exponent:"))
print(x**y)


# If a five-digit number is input through the keyboard, write a program to calculate the sum
# of its digits.

# In[23]:


n=int(input("Enter number:"))
sum=0
while(n>0):
    rem=n%10
    sum=sum+rem
    n=int(n/10)
print(sum)


# Write a program that reads in the radius of a circle and prints the circle‟s diameter,
# circumference and area. Use the constant value 3.14159 for pi. Perform each of these
# calculations inside the print statement(s) and use the conversion format specifier %f

# In[24]:


n=int(input("Enter radius of circle:"))
pi=3.14159
dia=n*2
circum=2*n*pi
area=pi*(n**2)
print(dia,circum,area)


# A company insures its drivers in the following cases:
# − If the driver is married.
# − If the driver is unmarried, male & above 30 years of age.
# − If the driver is unmarried, female & above 25 years of age.
# In all other cases, the driver is not insured. If the marital status, sex and age of the driver
# are the inputs, write a program to determine whether the driver is to be insured or not

# In[1]:


s = int(int(input('If married type 1, and if not, then type 0: ')))
gen = int(int(input('If you are male, then press 1, and if not, then type 0: ')))
age = int(input('Enter age: '))

if s:
    print("You are insured")
else:
    if (gen==1 and age > 30) or (gen==0 and age > 25):
        print("You are insured")
    else:
        print("You are not insured")


# Write a program that take year as an input from user. Determine whether year is leap year
# or not

# In[30]:


year = int(input('Enter your birth year:'))

if (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)):
    print("It is a leap year")
else:
    print("It is not a leap year")


# Write a program that reads an integer and determines and prints whether it‟s odd or even

# In[32]:


num=int(input("Enter a number:"))
if num % 2 ==0:
    print("even")
else:
    print("odd")


# Write a program that reads in two integers and determines and prints whether the first is a
# multiple of the second.

# In[34]:


x=int(input("Enter a number:"))
y=int(input("Enter a number:"))
if y % x ==0:
    print("multiple")
else:
    print("Not multiple")


# Write a program that asks the user to enter two integers, obtains the numbers from the
# user, then prints the larger number followed by the words “is larger.” If the numbers are
# equal, print the message “These numbers are equal.” Use only the single-selection form
# of the if statement you learned in this chapter

# In[39]:


x = int(input("Enter a number: "))
y = int(input("Enter a number: "))

if x != y:
    if x > y:
        print(str(x) + " is larger")
    else:
        print(str(y) + " is larger")
else:
    print("These numbers are equal")


# . Write a program that inputs three different integers from the keyboard (i.e num1, num2,
# num3), then prints the sum, the average, the product, the smallest and the largest of these
# numbers. The screen dialogue should appear as follows:

# In[48]:


x,y,z=input("Input three different integers: ").split()
sum=int(x)+int(y)+int(z)
Average=(int(x)+int(y)+int(z))/3
Product=int(x)*int(y)*int(z)
ls=[]
ls.append(int(x))
ls.append(int(y))
ls.append(int(z))
ls=sorted(ls)
smallest=ls[0]
largest=ls[2]
print("Sum is " + str(sum))
print("Average is " + str(Average))
print("Product is " + str(Product))
print("Smallest is " + str(smallest))
print("Largestis " + str(largest))


# (Body Mass Index Calculator) We introduced the body mass index (BMI) calculator in
# The formulas for calculating BMI are
# BMI = (weightInKilograms) / (heightInMeters * heightInMeters)
# Create a BMI calculator application that reads the user‟s weight in kilograms and height
# in meters, then calculates and displays the user‟s body mass index. Also, the application
# should display the following information from the Department of Health and Human
# Services/National Institutes of Health so the user can evaluate his/her BMI:
# BMI VALUES
# Underweight: less than 18.5
# Normal: between 18.5 and 24.9
# Overweight: between 25 and 29.9
# Obese: 30 or greater

# In[50]:


def BMIcalc(w,h):
    bmi=w/(h**2)
    if(bmi<18.5):
        print('Underweight')
    if(bmi>=18.5 and bmi<=24.9):
        print('normal')
    if(bmi>=25 and bmi<=29.9):
        print('Overweight')
    if(bmi>=30):
         print('Obese')
BMIcalc(75,1.82)
    


# Write a program to check whether a triangle is valid or not, when the three angles of the
# triangle are entered through the keyboard. A triangle is valid if the sum of all the three
# angles is equal to 180 degrees.

# In[51]:


x,y,z=input("Input three angles of triangles: ").split()
sum=int(x)+int(y)+int(z)
if sum==180:
    print('valid')
else:
    print("not valid")


# Given the length and breadth of a rectangle, write a program to find whether the area of
# the rectangle is greater than its perimeter. For example, the area of the rectangle with
# length = 5 and breadth = 4 is greater than its perimeter.

# In[55]:


x=int(input("Enter length of rectangle:"))
y=int(input("Enter breadth of rectabgle:"))
area=(x*y)
brea=(x+y+x+y)
if area>brea:
    print("Area is greater")
else:
    print('Area is not greater')


# A library charges a fine for every book returned late. For first5 days, the fine is 50 paise,
# for 6-10 days fine is one rupee and above 10 days fine is 5 rupees. If you return the book
# after 30days your membership will be cancelled. Write a program to accept the number
# of days the member is late to return the book and display the fine or the appropriate
# message.
# 

# In[57]:


def finecalc(x):
    fine = 0
    if x == 0:
        pass
    elif x <= 5:
        fine = 0.5
    elif 5 < x < 10:
        fine = 1
    elif x >= 10:
        fine = 5
    else:
        print("membership cancelled")
    return fine

print(finecalc(6))


# If the three sides of a triangle are entered through the keyboard, write a program to check
# whether the triangle is isosceles, equilateral, scalene or right-angled triangle

# In[61]:


x,y,z=input("Input three triangle lengths: ").split()
x=int(x)
y=int(y)
z=int(z)
x2=x**2
y2=y**2
z2=z**2
if(x==y and y==z):
    print('equilateral')
elif (x==y or y==z or x==z):
    print('isosceles')
elif (x2==(y2+z2)):
    print("right angle")
elif (y2==(x2+z2)):
    print("right angle")
elif (z2==(y2+x2)):
    print("right angle")
else:
    print("scalene")
    


# A university has the following rules for a student to qualify for a degree with A as the
# main subject and B as the subsidiary subject:
# (a) He should get 55 percent or more in A and 45 percent or more in B.
# (b) If he gets than 55 percent in A he should get 55 percent or more in B. However, he
# should get at least 45 percent in A.
# (c) If he gets less than 45 percent in B and 65 percent or more in A he can reappear in an
# examination in B to qualify.
# (d) In all other cases he is declared to have failed.

# In[62]:


def deg(a,b):
    if(a>=55 and b>=45):
        print("Passes")
    elif(45<=a>55 and b>=55):
        print("Passes")
    elif(a>=65 and b<45):
        print("reappear in B")
    else:
        print("Failed")
deg(55,20)


#  Write a program that calculates the squares and cubes of the numbers from 0 to 10 and
# uses tabs to print the following table of values:
# number square cube
# 0 0 0
# 1 1 1
# 2 4 8
# 3 9 27
# 4 16 64
# 5 25 125

# In[67]:


print("number",end=" ")
print("square",end=" ")
print("cube",end=" ")
print()
for i in range(0,11):
    print(i,end="       ")
    print(i**2,end="       ")
    print(i**3,end="      ")
    print()


#  Write a program that calculates and prints the sum of the even integers from 2 to 30

# In[68]:


sum=0
for i in range(2,31,2):
    sum=sum+i
print(sum)


# Write a program to find the range of a set of numbers. Range is the difference between
# the smallest and biggest number in the list. You are not allowed to use built-in range()
# function.
# 

# In[70]:


x=[2,3,4,1,9]
x=sorted(x)
s=x[0]
l=x[len(x)-1]
print(l-s)


# Write a program to produce the following output using loop:
# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 

# In[77]:


x=1
row=1
for i in range(4,0,-1):
    for j in range(0,i-1):
        print(" ",end=" ")
    for j in range(0,row):
        print(x,end="   ")
        x+=1
    print()
    row+=1
    
    


# Write a program that takes the side of a square from user and then prints that square out
# of asterisks. Your program should work for squares of all side sizes between 1 and 20.
# For example, if your program reads a size of 4, it should print

# In[80]:


x=10
for i in range(0,x):
    for j in range(0,x):
        print("*",end="")
    print()

# Write a program that displays the following checkerboard pattern:
* * * * * * *
* * * * * * * *
 * * * * * * * *
* * * * * * * *
 * * * * * * * *
* * * * * * * *
 * * * * * * * *
* * * * * * * *

# In[86]:


row=1
for i in range(0,7):
    print("*",end=" ")
print()
while(row<9):
    if(row%2==0):
        print("",end=" ")
        for i in range(0,8):
            print("*",end=" ")
    else:
        for i in range(0,8):
            print("*",end=" ")
    row=row+1
    print()
    

(Triangle-Printing Program) Write a program that prints the following patterns
separately, one below the other. Use for loops to generate the patterns. All asterisks (*)
should be printed by a single print statement of the form print "*" (this causes the
asterisks to print side by side). [Hint: The last two patterns require that each line begin
with an appropriate number of blanks.]
(A) (B)           (C)
* ********** ********** 
** ********* ********* 
*** ******** ******** 
**** ******* ******* 
***** ****** ****** 
****** ***** *****
******* **** **** 
******** *** *** 
********* ** ** 
********** * * 

# In[87]:


#(A):
for i in range(1,11):
    for j in range(0,i):
        print("*",end="")
    print()


# In[88]:


#(B):
for i in range(10,0,-1):
    for j in range(0,i):
        print("*",end="")
    print()


# In[89]:


#(C):
row=0
for i in range(10,0,-1):
    for j in range(0,row,1):
        print("",end=" ")
    for j in range(0,i):
        print("*",end="")
    row+=1
    print()

Write a program that prints the following diamond shape. You may use print statements
that print either a single asterisk (*) or a single blank. Maximize your use of repetition
(with nested for statements) and minimize the number of print statements.
*
***
*****
*******
*********
*******
*****
***
*
# In[93]:


x=5
y=1
for i in range(1,x+1):
    for j in range(0,y):
        print("*",end="")
    y=y+2
    print()
y=y-2
for i in range(1,x+1):
    for j in range(0,y):
        print("*",end="")
    y=y-2
    print()
    


# In[ ]:




