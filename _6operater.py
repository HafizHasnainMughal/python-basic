#operators in python
"""
  the operators are used to perform operations on variables and values.
  like addition, subtraction, multiplication, division, etc.
    operators ko hum variables aur
    values par operations perform karne kay liya use karte hain.  

"""

#types of operators in python
"""
    1. Arithmetic Operators like +, -, *, /, %, **, // etc. are used to perform arithmetic operations on variables and values.
    2. Comparison Operators like ==, !=, >, <, >=, <= etc. are used to compare the values of variables and values.
    3. Logical Operators like and, or, not etc. are used to perform logical operations on variables and values.
    4. Assignment Operators  like =, +=, -=, *=, /=, %=, **=, //= etc. are used to assign values to variables.
    5. Identity Operators like is, is not etc. are used to compare the memory locations of variables and values.
    6. Membership Operators like in, not in etc. are used to check if a value is present in a sequence or not.
    7. Bitwise Operators like &, |, ^, ~, <<, >> etc. are used to perform bitwise operations on variables and values.

"""

#Arithmetic Operators in python

a=10
b=5
c=a+b
print("Addition of a and b is : ",c)
d=a-b
print("Subtraction of a and b is : ",d)
e=a*b
print("Multiplication of a and b is : ",e)
f=a/b
print("Division of a and b is : ",f)
g=a%b
print("Modulus of a and b is : ",g) 
h=a**b
print("Exponentiation of a and b is : ",h)  


#Assignment Operators in python
i=10
print("Value of i is : ",i)
i+=5
print("Value of i after adding 5 is : ",i)
i-=3
print("Value of i after subtracting 3 is : ",i) 
i*=2
print("Value of i after multiplying by 2 is : ",i)
i/=3
print("Value of i after dividing by 3 is : ",i)


#comparison Operators in python it returns boolean value True or False
j=10
k=5
print("Is j equal to k : ",j==k) # equals to operator
print("Is j not equal to k : ",j!=k) # not equals to operator
print("Is j greater than k : ",j>k)  # greater than operator
print("Is j less than k : ",j<k) # less than operator
print("Is j greater than or equal to k : ",j>=k) # greater than or equal to operator
print("Is j less than or equal to k : ",j<=k) # less than or equal to operator


