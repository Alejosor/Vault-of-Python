import random
'''
#Option 1
user=int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n -> '))
rock = '''
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# '''

# paper = '''
#     _______
# ---'   ____)____
#           ______)
#           _______)
#          _______)
# ---.__________)
# '''

# scissors = '''
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
'''
options = [rock,paper,scissors]
computer = random.randint(0,2)

if user==0 and computer==0:
    print(f'You choose:\n{rock}')
    print(f'Computer choose:\n{rock}')
    print('Is a tie')
elif user==0 and computer==1:
    print(f'You choose:\n{rock}')
    print(f'Computer choose:\n{paper}')
    print('You lose')
elif user==0 and computer==2:
    print(f'You choose:\n{rock}')
    print(f'Computer choose:\n{scissors}')
    print('You win')
elif user==1 and computer==1:
    print(f'You choose:\n{paper}')
    print(f'Computer choose:\n{paper}')
    print('Is a tie')
elif user==1 and computer==2:
    print(f'You choose:\n{paper}')
    print(f'Computer choose:\n{scissors}')
    print('You lose')
elif user==1 and computer==0:
    print(f'You choose:\n{paper}')
    print(f'Computer choose:\n{rock}')
    print('You win')
elif user==2 and computer==2:
    print(f'You choose:\n{scissors}')
    print(f'Computer choose:\n{scissors}')
    print('Is a tie')
elif user==2 and computer==0:
    print(f'You choose:\n{scissors}')
    print(f'Computer choose:\n{rock}')
    print('You lose')
elif user==2 and computer==1:
    print(f'You choose:\n{scissors}')
    print(f'Computer choose:\n{paper}')
    print('You win')
else:
    print('Number not allowed, please try again')
'''

#Option 2
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images=[rock,paper,scissors]

user_choice = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n -> '))
if user_choice >= 0 and user_choice <= 2:
    print(game_images[user_choice])
computer_choice = random.randint(0,2)
print('Computer Choice')
print(game_images[computer_choice])

if user_choice >= 3 or user_choice < 0:
    print('You typed an invalid number. Your lose!')
elif user_choice == 0 and computer_choice == 2:
    print('You win!')
elif computer_choice == 0 and user_choice == 2:
    print('You lose!')
elif computer_choice > user_choice:
    print('You lose!')
elif user_choice > computer_choice:
    print('You win!')
elif computer_choice == user_choice:
    print("It's a draw")