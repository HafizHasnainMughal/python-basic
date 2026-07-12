#  variables in python

"""
  variable just like a container in which we can store any data.
  variables wo cheez hoti hai jisme hum kisi bi cheez ka data store karte hain. like kisi bi cheez ka
  name, age, salary, price, etc.
  variables ko hum kisi bi data type me store karte hain. like string, integer, float, boolean, etc.
  or variable ka name capital ya small letter ya underscore(_) say start ho sakta hain.
"""


#  variables name start with capital or small letter or underscore(_)
#  and can not start with a number

"""
    variable ka name capital ya small letter ya underscore(_) say start ho sakta hai
    or variable ka name number say start nahi ho sakta hai 
    ya role hay 
    like variable ka name 1name = "Hafiz Hasnain Mughal" ye galat hay
    variable kay name case sensitive hotay hain 
    means agar hum 'name' ko small letter say likhtay hain
    to ye 'name' variable ko consider karega.
    or agar hum 'Name' ko capital letter say likhtay hain 
    to ye 'Name' variable ko consider karta hay.

"""

name="enter your name : "
Name="enter your nick name : "
_name="enter your last name : "

print(name)
print(Name)
print(_name)

# for knoeing the type of variable we use type() function
"""
  kisi bi variable ka type jan'ne kay liya hum type() function ka use karte hain
"""
print(type(name))

age=20
print(type(age))

boolean=True
print(type(boolean))
