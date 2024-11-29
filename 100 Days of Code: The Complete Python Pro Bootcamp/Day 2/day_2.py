#Primitive Data Types
# Strings
print("This is a String")
# Integers
print(2)
# Floats
print(3.14159)
# Booleans
print(True)

#Length 
print(len(str(12345))) #5

#Type Checking
print(type("This is a String")) # <class 'str'>
print(type(12)) # <class 'int'>
print(type(3.14159)) # <class 'float'>
print(type(True))# <class 'bool'>
#Exercise
#print("Number of letters in your name: " + str(len(input("Enter your name: "))))

#Mathematical Operations
print(10+5) #addition
print(10-5) #subtraction
print(10*5) #multiplication
print(11/5) #division
print(11//5) 
print(11%5)
print(2**3)

#Number Manipulation
# Flooring a Number
print(int(3.738492)) # Becomes 3

# Rounding a Number
print(round(3.738492)) # Becomes 4
print(round(3.14159)) # Becomes 3
print(round(3.14159, 2)) # Becomes 3.14

# Assignment Operators
score=0
# +=
score += 3 # score = 3
# -=
score -= 1 # score = 2
# *=
score *= 2 # score = 4
# /=
score /= 2 # score = 2

# f-Strings
age = 12
print(f"I am {age} years old")# I am 12 years old.