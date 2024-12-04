import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Version 1
# firts = []
# for lett in range(0,nr_letters):
#     rand_index= random.randint(0,(len(letters)-1))
#     firts.append(letters[rand_index])

# second = []
# for lett in range(0,nr_symbols):
#     rand_index= random.randint(0,(len(symbols)-1))
#     second.append(symbols[rand_index])

# thrid = []
# for lett in range(0,nr_numbers):
#     rand_index= random.randint(0,(len(numbers)-1))
#     thrid.append(numbers[rand_index])

# # Easy Level
# # password_list = firts + second + thrid
# # password = "".join(password_list)
# # print(f'Your password: {password}')

# #Hard Level
# password_list = firts + second + thrid
# random.shuffle(password_list)
# password = "".join(password_list)
# print(f'Your password: {password}')

# Version 1.2
password_list = []

for char in range(nr_letters):
    password_list.append(random.choice(letters))

for char in range(nr_symbols):
    password_list.append(random.choice(symbols))

for char in range(nr_numbers):
    password_list.append(random.choice(numbers))

random.shuffle(password_list)
password = ''.join(password_list)
print(f'Su nueva contraseña: {password}')