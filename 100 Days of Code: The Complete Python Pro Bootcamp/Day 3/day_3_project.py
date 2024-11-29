print('Welcome to Treasure Island.')
print('Your mission is to find the treasure.')

spot_1=input("You're at a cross road. Where do you want to go?\n\tType \"left\" or \"right\":\n").lower()
if spot_1 == 'left':
    print("You've come to a lake. There is an island in the middle of the lake.")
    spot_2=input("\t Type \"wait\" to wait for a boat. Type \"swim\" to swin across.\n").lower()
    if spot_2 == 'wait':
        print("You arrive at the island unharmed. There is a house with 3 doors.")
        spot_3=input("\tOne red, one yellow and one blue. Which colour do you choose?\n").lower()
        if spot_3 == 'red':
            print("Burned by fire.Game Over.")
        elif spot_3 == 'yellow':
            print("You Win!")
        elif spot_3 == 'blue':
            print("Eaten by beasts.Game Over.")
        else:
            print("Game Over.")
    else:
        print("Attacked by trout.Game Over.")
else:
    print("Fall into a hole.Game Over.")