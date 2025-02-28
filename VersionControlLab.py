#Version Control Lab

#get randint
from random import randint

def main():
    user_question = input("What would you like to ask the magic 8-ball: ") #ask the user a question to ask the 8-ball
    user_choice = input("Would you like to shake the magic 8-ball (enter y or n): ")#take the user's choice
    check_input(user_choice)


    while user_choice == "y":
        spin = randint(1,15)




def check_input(user_choice):
    while user_choice != "y" and user_choice != "n": #check for valid input
        print("You did not give a valid input for shaking the magic 8-ball. Try again!")
        user_choice = input("Would you like to shake the magic 8-ball (enter y or n): ")#take the user's choice

main()

