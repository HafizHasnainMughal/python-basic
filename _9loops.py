#loops in python
"""

  Loop ek programming structure hai jo kisi block of code
  ko baar baar execute karta hai jab tak koi condition ya sequence khatam na ho jaye.
"""


#for loop in python
""" 
  for loop hum tab use kartay hain 
  jab humay pata ho kay user kitni dafa ik cheez ko preint karwana chata hay .
  means range ka pahlay say pata hona .
  syntex:
    for iterantion in sequence:
       statement
"""

#old method to resolve the loops
print("traditional method ...")
print("Mula Ali R.A")
print("Mula Ali R.A")
print("Mula Ali R.A")
print("Mula Ali R.A")
print("Mula Ali R.A")
print("Mula Ali R.A")
print("Mula Ali R.A")

#now in loop
print("for using loop")

for x in range(1,7):
    print("Mula Ali R.A")

for  i in range(0,4):
    print(i)
# for using  range(start,stop,step) uing three parameters 
#start wala point jider say ap start karna chahtay ho.
#stop wala point jider tak ap rukna chahtay ho us 
#   say one index pahlay tak means ager ap likhatay 3 to stop 2 tak ho ga .


#for making table using  for loop
multiple_number=int(input("enter the number you want to make the table :"))
for y in range(1,10+1):
    print(f"{multiple_number} * {y}  = {y*multiple_number} ")



#loop control statements
"""
  breake >>> used to terminate the loop entierly
  continue >> skip to the next iteration of the loop
  pass >> does nothing ,acts asa a plcaeholder

"""

print("for break condition")

for q in range(1,5):
    if q==3:
        break
    print(q)

print("continue condition  ")

for e in range(1,8):
    if e==4:
        continue
    print(e)

print("pass condition in loop ")

for r in range(1,5):
    pass


#nested for loop in python
"""
  nested loop means loop kay ander loop ka hona 
  first loop calling outer loop and second loop calling inner loop.
  syntex:
     for iteration_for_outer_loop in sequence:
         for iteration_for_inner_loop in sequence:
           statement
        statement
"""
print("nested for loop ")
outer_loop_iteration=int(input("enter the outer loop range :"))
inner_loop_iteration=int(input("enter the inner loop range :"))
symbol=input("enter the some symbol :")

for outer in range(1,outer_loop_iteration):
    for inner in range(1,inner_loop_iteration):
        print(symbol,end="")
    print()


#while loop in python

"""
  while loop tab tak chalta rehta hai jab tak condition True ho.
  while loop hum tab use kartay hain jab user 
   ko range ka na pata ho ya false condition per stop karta hay
  syntex:
    starting_point
    while condition:
        statement
        iteration
"""

print("while loop start")
a=0
while a<=7:
    print(a)
    a+=1 #increament


#using while and for loop usinf check condition

print("checking condition using while loop ")
while True:
    table=int(input("enter the number you want to create the table "))
    for tble in range(1,10+1):
        print(f"{table} * {tble} = {table*tble}")
    qest= input("if you create again table press enter otherwise enter 'no' ")
    if qest.lower()=="no":
        break
print("the loop is broke ")

#nested while loop in pyton

print("nested while loop in python  ")

j=1
while j<=6:
    k=0
    while k<7:
        k+=1
        print("$",end=" ")
    print()
    j+=1


