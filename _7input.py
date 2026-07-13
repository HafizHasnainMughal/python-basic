#input function in python

name=input("Enter your name : ")
print("Hello your name is : ",name)
print("Type of name variable is : ",type(name))

#input function always returns string data type so 
#if we want to take integer input from user 
#we have to convert it into integer data type using int() function


age=int(input("Enter your age : "))
print("Your age is : ",age)
print("Type of age variable is : ",type(age))

#if we want to take float input from user

height=float(input("Enter your height : "))
print("Your height is : ",height)
print("Type of height variable is : ",type(height))

#if we want to take boolean input from user

status=bool(input("Enter your status : "))  
print("Your status is : ",status)
print("Type of status variable is : ",type(status)) 


#the other method to take input from user is using eval() function
# which can take any data type input from user and return the same data type as input

value=eval(input("Enter any value : ")) 
print("Your value is : ",value)
print("Type of value variable is : ",type(value))

#the other method of taking input from user ,
#this method is used when you need fast input

import sys
print("Enter your name : ")
name = sys.stdin.readline()
print(name)