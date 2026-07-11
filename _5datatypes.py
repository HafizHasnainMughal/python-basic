# string variables

"""
  string variable wo variable hota hai jisme hum
  string values ko store karte hain. like kisi bi cheez ka
  name "hello", "world", "python", "programming" etc.
  or is ko hum single ya double quotes me store karte hain.

"""
name = "Hafiz Hasnain Mughal"
print(name)


"""
  string variable ko hum slice( means chotay chatay hisay karna ) kar sakte hain.
  slice karne ka formula hai [start:stop:step]
  start ka matlab hai kahan se slice karna hai,
  stop ka matlab hai kahan tak slice karna hai,
  step ka matlab hai kitne step ke baad slice karna hai like 2 steps 3 steps so on.
  strating index  always 0 say start hota hay
  means first character ko hum 0 index par consider karte hain.
  
"""


# slice the string variables 
# formula for slicing the string variables is [start:stop:step]
# the starting index of your string is always 0 
# the last index of your string is n-1 where n is the length of your string
# also includes the spaces in the string variables

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


