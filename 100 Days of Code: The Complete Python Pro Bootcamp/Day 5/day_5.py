#Python Loops

# For Loop
# for item in list_of_items:
    #Do somethingto each item

#Syntax
# for <variable name of each item> in <a List>:
#     <do something>
#     <do something else> 

# fruits = ['Apple','Peach','Pear']
# for fruits in fruits:
#     print(fruits)
#     print(fruits + " pie")
'''
Apple
Apple pie
Peach
Peach pie
Pear
Pear pie
'''

#Add results - Function sum()
# student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
#Option 1
# total_score = sum(student_scores)
# print(f'The total score is {total_score}')

#Option 2
# score = 0
# for note in student_scores:
#     score+=note
# print(f'The total score is {score}')

#Highest score - Function sum()
# student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]

#Option 1
# max_score = max(student_scores)
# print(f'The highest score is {max_score}')

#Option 2
# score = 0
# for max in student_scores:
#     if max > score:
#         score = max
# print(f'The highest score is {score}')

#For Loops - Function range()
# for number in range(a,b):
#     print(number)

# for number in range(1,10):
#     print(number)
'''
1
2
3
4
5
6
7
8
9
'''

# for number in range(1,10,2):
#     print(number)
'''
1
3
5
7
9
'''

#The Gauus Challenge
# result = 0
# for number in range(1,101):
#     result += number
# print(f'The final answer is {result}')

#FizzBuzz game
for number in range(1,101):
    if (number%3 == 0) and (number%5 == 0):
        print("FizzBuzz")
    elif (number%5 == 0):
        print("Buzz")
    elif (number%3 == 0):
        print("Fizz")
    else:
        print(number)