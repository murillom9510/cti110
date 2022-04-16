# This program gives simple math quizzes
# 4/15/2022
# CTI-110 P5HW2 - Math Quiz
# Mateo Murillo
#

import random

# defining the addRandom to add the random generated numbers
def addRandom():
    # generates two random numbers between 0 and 1000 and asks the user to enter the answer
        n1=random.randint(0,1000)
        n2=random.randint(0,1000)
        print(f"{n1:>6}")
        print(f"+{n2:>5}")
        print("Enter answer")
        ans=int(input())
        while ans!=n1+n2:
        
                # prints if the answer was incorrect and asks user to try again, if the answer is correct prints congratz
                if ans<n1+n2:
                        print("Sorry, guess is too low.")
                else:
                        print("Sorry, guess is too high")

                ans=int(input("try again : "))
        print("Congratulations!!!! your answer is correct...")
# defining the subRandom to subtract the random 
def subRandom():
    # generates two random numbers between 0 and 1000 and asks the user to enter the answer
        n1=random.randint(0,1000)
        n2=random.randint(0,1000)
        print(f"{n1:>6}")
        print(f"-{n2:>5}")
        print("Enter answer")
        ans=int(input())
        while ans!=n1-n2:
        
                # prints if the answer was incorrect and asks user to try again, if the answer is correct prints congratz
                if ans<n1-n2:
                        print("Sorry, guess is too low.")
                else:
                        print("Sorry, guess is too high")
                ans=int(input("try again : "))
        print("Congratulations!!!! your answer is correct...")

# displays the main menu to the user and uses the user input to display the game features       
if __name__=="__main__":

        while 1:

                print("MAIN MENU")
                print("----------------------")
                print("1) Adding Random Numbers ")
                print("2) Subtracting Random Numbers")
                print("3) Exit")
                num=int(input("Please choose one of the menu options: "))
                if num==3:
                        print("Thank you for playing...")
                        print("Bye!!")
                        break
                if num==1:
                        addRandom()
                if num==2:
                        subRandom()
