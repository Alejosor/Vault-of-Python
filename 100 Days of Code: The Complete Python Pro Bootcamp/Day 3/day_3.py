#Control Flow and Logical Operators
#Conditional if / else
"""
if condition
    do this
else:
    do this
"""
#The indentation is important 
#Example:
# water_level=50
# if water_level > 80:
#     print("Drain water")
# else:
#     print("Continue")

#Problem 1: Ticket park
# print("Welcome to the rollercoaster!")
# height=int(input("Please, enter your height in cm:\n"))
# if height > 120:
#     print("You can ride")
# else:
#     print("You can't ride")

'''
Comparison Operators
> - Greater than
< - Less than
>= - Greater than or equal to
<= - Less than or equal to
== - Equal to
!= - Not Equal to
'''

#Check Odd or Even
# number=int(input("Please enter a number:\n"))
# if number%2== 0:
#     print("Your number is a Even number")
# else:
#     print("Your number is a Odd number")

#Nested if statements and elif statements
'''
Nested if / else
if condition:
    if another condition:
        do this
    else:
        do this
else:
    do this
'''
'''
Nested if / else
if condition:
    if another condition1:
        do A
    elif another condition2:
        do B
    else:
        do this
else:
    do this
'''
# Problem 2: Ticket park
# print("Welcome to the rollercoaster!")
# height=int(input("Please, enter your height in cm:\n"))
# if height > 120:
#     print("You can ride")
#     age=int(input("Please enter your age:\n"))
#     if age > 18:
#         print("Please pay $12")
#     elif age >=12:
#         print("Please pay $7")
#     else:
#         print("Please pay $5")
# else:
#     print("Sorry,you can't ride")

# Multiple if Statements in Succession
# print("Welcome to the rollercoaster!")
# height=int(input("Please, enter your height in cm:\n"))
# bill = 0
# if height > 120:
#     print("You can ride")
#     age=int(input("Please enter your age:\n"))
#     if age > 18:
#         print("Adult tickets are $12")
#         bill=12
#     elif age >=12:
#         print("Youth tickets are $7")
#         bill=7
#     else:
#         print("Child tickets are $5")
#         bill=5
        
#     photo=input("Do you want to have a photo take? Type y for Yes or n for No\n")
#     if photo == 'y':
#         bill+=3
    
#     print(f"Yoour final bill is ${bill}")
# else:
#     print("Sorry,you can't ride")

# Python Pizza
# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M or L: ")
# pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
# extra_cheese = input("Do you want extra cheese? Y or N: ")

# bill = 0
# if size == 'S':
#     bill+=15
# elif size == 'M':
#     bill +=20
# elif size == 'L':
#     bill +=25
# else:
#     print("Wrong characters")

# if pepperoni == 'Y':
#     if size == 'S':
#         bill += 2
#     else:
#         bill += 3


# if extra_cheese == 'Y':
#     bill+=1

# print(f"Your final bill is: ${bill}.")

# Logical Operators
# and
# or
# not