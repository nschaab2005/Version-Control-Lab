#Version Control Lab

#get randint
from random import randint

def main():
    user_question = input("What would you like to ask the magic 8-ball: ") #ask the user a question to ask the 8-ball
    user_choice = input("Would you like to shake the magic 8-ball (enter y or n): ")#take the user's choice
    check_input(user_choice)
    comments = ["It is certain" , "It is decidedly so ", "Without a doubt", "Yes definitely", 
            "You may rely on it", "Reply hazy, try again" , "Ask again later" ,
            "Better not tell you now", "Cannot predict now", "Concentrate and ask again",
            "Don't count on it", "My reply is no", "My sources say no", "Outlook not so good", "Very doubtful"]

    while user_choice.lower() == "y":
        spin = randint(0,14)
        print(f"The Eight Ball Commands: {comments[spin]}")
        user_choice = input("Would You Like to Spin Again: 'y' or 'n' ")
        check_input(user_choice)



def check_input(user_choice):
    while user_choice != "y" and user_choice != "n": #check for valid input
        print("You did not give a valid input for shaking the magic 8-ball. Try again!")
        user_choice = input("Would you like to shake the magic 8-ball (enter y or n): ")#take the user's choice









main()

