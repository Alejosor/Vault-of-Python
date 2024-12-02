#Randomisation and Python Lists
# #Random Module
import random
# import my_module

# num1 = random.randint(1,10) #Random number between 1 and 10
# print(num1)

# #My Module
# print(my_module.my_favorite_number) #Number -> 50

# #Random number between 0 to 1
# random_number_o_to_1 = random.random()
# print(random_number_o_to_1)

# #Random floating number
# random_float = random.uniform(1,10)
# print(random_float)

#Heads of Tail
# coin = random.randint(0,1)
# print(f'The number was: {coin}')
# if coin == 1:
#     print("Heads")
# else:
#     print('Tails')

#List
# fruits = ["orange","apple"]
# states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

# print(states_of_america[13]) #Vermont
# print(states_of_america[-1]) #Hawaii
# print(states_of_america[-2]) #Alaska

# #Change items in a list
# states_of_america[1]="Penn State"
# print(states_of_america[1])

# #Add item at the end of the list
# states_of_america.append('Alejosor')
# print(states_of_america[-1])
# print(states_of_america)

# #Delete item of the list
# states_of_america.pop(-1)
# print(states_of_america)

#Exercise - Who will pay the bill?
#Option #1
# friends = ['Alejo','Rosa','Lis','Luxo']
# payer=random.randint(0,(len(friends)-1))
# print('You are paying the bill this time',friends[payer])

#Option #2
# print('You are paying the bill this time',random.choice(friends))

#Nested Lists
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
 
dirty_dozen = [fruits, vegetables]
 
print(dirty_dozen[1][1])