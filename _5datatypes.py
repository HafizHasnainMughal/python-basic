# string data type in python

"""
  string data type wo type hota hai jisme hum
  string values(text format) ko store karte hain. like kisi bi cheez ka
  name "hello", "world", "python", "programming" etc.
  or is ko hum single ya double quotes me store karte hain.

"""
name = "Hafiz Hasnain Mughal"
print(name)


"""
  string datatype ko hum slice( means chotay chatay hisay karna ) kar sakte hain.
  slice karne ka formula hai [start:stop:step]
  start ka matlab hai kahan se slice karna hai,
  stop ka matlab hai kahan tak slice karna hai,
  step ka matlab hai kitne step ke baad slice karna hai like 2 steps 3 steps so on.
  strating index  always 0 say start hota hay
  means first character ko hum 0 index par consider karte hain.
  
"""
#some methods of string data type in python
"""
  for converting the string to upper case we use upper() method like name.upper()
  for converting the string to lower case we use lower() method like name.lower() 
  for converting the string to title case we use title() method like name.title()
  for converting the string to capitalize case we use capitalize() method like name.capitalize()
  for converting the string to swapcase we use swapcase() method like name.swapcase()
  for checking the string is alphanumeric or not we use isalnum() method like name.isalnum()
  for checking the string is alphabetic or not we use isalpha() method like name.isalpha()
  for checking the string is digit or not we use isdigit() method like name.isdigit()
  for checking the string is numeric or not we use isnumeric() method like name.isnumeric()
  for checking the string is space or not we use isspace() method like name.isspace()
  
"""

company_name="national university of computer and emerging sciences"

print("string methods in python")
print("upper case:",company_name.upper())
print("lower case:",company_name.lower()) 
print("title case:",company_name.title())
print("capitalize case:",company_name.capitalize())  
print("swap case:",company_name.swapcase())
print("is alphanumeric:",company_name.isalnum())
print("is alphabetic:",company_name.isalpha())
print("is digit:",company_name.isdigit())
print("is numeric:",company_name.isnumeric())
print("is space:",company_name.isspace())


# slice the string data type in python 
# formula for slicing the string datatype is [start:stop:step]
# the starting index of your string is always 0 
# the last index of your string is n-1 where n is the length of your string
# also includes the spaces in the string data type

print(name[0:5])  # prints "Hafiz"
print(name[6:13])  # prints "Hasnain"
print(name[14:19])  # prints "Mughal"

"""
    for revese slicing kay liya hum starting index ko -1 say start karte hain
    or agar hum -2 say start karte hain to ye last say second character ko consider karega
    for all string ko reverse karna ho to hum [::-1] ka use karte hain
"""

# for reverse slicing the starting index is -1 

print(name[0:-7])  # prints "Hafiz Hasnain"
print(name[::-1])


# numeric data type in python

"""
  numeric data type wo type hota hai jisme hum
  numeric values(numbers like 2, 3.14) ko store karte hain. like kisi bi cheez ka
  age, salary, price, etc.
  or is ko hum integer ya float me store karte hain.
"""


#using f string
"""
  f string hum use kartay hain print statements may kisi value ko call karan 
  syntex:
    print(f"{1value-call} print-statement {2value-call} ")
"""
print("f string method")
username="@helloworld"
passward=1234
print(f"your username is {username} and its passward {passward}")




#types of numeric data type in python
# 1. integer data type  like 1, 2, 3, 4, 5 etc. in which whole numbers are stored
# 2. float data type   like 1.1, 2.2, 3.3, 4.4, 5.5 etc. in which pointing values are stored
# 3. complex data type  like 1+2j, 3+4j, 5+6j etc. in which real and imaginary values are stored


"""
  >>>int for interger is may hum siraf whole numbers ko store karte hain (1,2,3,4,5).
  >>>float for float is may hum siraf pointing values ko store karte hain (1.1,2.2,3.3,4.4,5.5)
     for better accuracy obtain karnay kay liya .
  >>>complex for complex is may hum real and imaginary values ko store karte hain
     (1+2j,3+4j,5+6j) standard form of complex number is 
     a+bi where a is real part and b is imaginary part.
"""
age=20
print(age)

salary=50000.50
print(salary)

complex_number=3+4j
print(complex_number)



#boolean data type in python

"""
  boolean data type wo type hota hai jisme hum
  boolean values(True or False) ko store karte hain. like kisi bi cheez ka
  status, condition, etc.
  or is ko hum True ya False me store karte hain.
"""
is_student=True
print(is_student) 

is_employee=False
print(is_employee)