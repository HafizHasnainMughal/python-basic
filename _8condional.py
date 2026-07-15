#conditional statements in python
"""
   conditional statements wo statemesnts hoti jhain 
   jo kisi condition ki check kartay hain 
   means ager ya ho ga tu ya cheez print ho gi
   nahi tu koi desri 
   agar ya bi nahi tu ya wali cheex print ho gi 

"""

#simple if statement
"""
 syntex:
      if condition:
          statements
"""

age=int(input("enter your age :"))
if age>=18:
    print("you can eligibal for casting vote ")


#if - else statements
"""
  syntex:
     if condition:
         statement
     else:
         statement
"""

number=int(input("enter the some number for checking positive or negative :"))
if number>0:
    print("number is positive ")
else:
    print("number is negative ")

#for checking number is either even or odd

num=int(input("enter the number to check even or odd  :"))
if num%2==0:
    print("your number is even ")
else:
    print("your entered number is odd ")


#if -elif and else statements
"""
  syntex:
    if condition:
       statement
    elif condition:
       statement
    elif condition:
       statement
    .
    .
    .
    else:
       statement
"""

marks=int(input("enter your marks : "))
if marks>=80 and marks<=100:
    print("you have A grade in the codind subject ")
elif marks>=60 and marks<80:
    print("you have B grade in the codind subject ")
elif marks>=40 and marks<60:
    print("you have C grade in the codind subject ")
elif marks>=33 and marks<40:
    print("you got passing marks in the codind subject ")
elif marks>=0 and marks<33:
    print("you are fail in the coding subject ")
else:
    print(" you  entered the wronge number ")


#nested if else statements 

"""
  syntex:
    if condition:
        if condition:
           statement
        else :
           statement
    else:
        statement

"""

username=input("enter your username :")
passward=int(input("enter your passward :"))

if username=="admin":
    if passward==2936:
        print(" valid username and passward")
    else :
        print("you enterd the wronge passward ")
elif username=="Admin":
    if passward==3629:
        print("valid username and passward")
    else :
        print("you enterd the wronge passward ")
elif username!="admin" or username!="Admin":
    if passward==3629 or passward==2936:
        print("invalid username but passward correct")
    else :
        print("you enterd the wronge username and passward  ")
else:
    print("you are enter the wronge username or passward")    



#short hand if else conditional statements 
"""
    syntex:
        statement_if-true if condition else statement-for false

"""

print("short hand if else statements " )
numb=3
print("positive number") if numb>=0 else print("negative number ")

