"""
Create a calculator.py program that calculates the area of one of the following shapes:
    1) Square
    2) Rectangle
    3) Triangle
    4) Circle

The program should present a menu for the user to choose which shape to calculate, 
then ask them for the appropriate values (side, length, width, etc.).
"""
import math
print("==================\nArea Calculator 📐\n==================")
print("1) Triangle\n2) Rectangle\n3) Square\n4) Circle\n5) Quit")
choice = int(input("\nPlease select one shape:\n"))

if choice == 1:
    #Triangle
    height = float(input("\nPlease enter the height of the triangle:\n"))
    base = float(input("Please enter the base of the triangle:\n"))
    triangle = (height*base)/2
    print("\n==================\nArea Result ✅\n==================")
    print(f"The area of the triangle: {round(triangle,2)}")
elif choice == 2:
    #Rectangle
    length = float(input("\nPlease enter the length of the rectangle:\n"))
    width = float(input("Please enter the width of the rectangle:\n"))
    rectangle = length * width
    print("\n==================\nArea Result ✅\n==================")
    print(f"The area of the rectangle: {round(rectangle,2)}")
elif choice == 3:
    #Square
    side = float(input("\nPlease enter the side of the square:\n"))
    square = side ** 2
    print("\n==================\nArea Result ✅\n==================")
    print(f"The area of the square: {round(square,2)}")
elif choice == 4:
    #Circle
    radius = float(input("\nPlease enter the radius of the circle:\n"))
    circle = (math.pi)*(radius**2)
    print("\n==================\nArea Result ✅\n==================")
    print(f"The area of the circle: {round(circle,2)}")
elif choice == 5:
    #Quit
    print("\nThanks for stopping by! Keep calculating and have a great day!")
else:
    print("\nInvalid input, please select only from the given options.")