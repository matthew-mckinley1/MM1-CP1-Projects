#Matthew McKinley Number Geussing Game
#PROJECT GOAL to have a random number and have the person guess it
#it is going to have a random number and allow the user to input a number, telling them if it's higher or lower, and telling them if they win or not
#import random, loop until they can get it right
#Github and VScode
#pseudocode
#import random
#pick random number from 1-10
#allow the user to input number
#see if it is correct
#tell them higher or lower
#loopyloop


#import random to get the random number
import random
#set it to a variable
currentNum = random.randint(1,10)
#have it loopable with main()
def main():
    #take the user input as a variable
    userInp = int(input("What number would you like to guess? (1-10)"))
    #have if the user input is equal to the current number, if so then you win
    if userInp == currentNum:
        print("You guessed the correct number!")
        exit()
    #have if the user input is greater than the current number, if so it tells you that it's less and then loops (I could reverse the input and number)
    elif userInp > currentNum:
        print("It is lower than the number you inputted")
        main()
    #have if the user input is less than the current number, if so it tells you that it's more and then loops (I could reverse the input and number)
    elif userInp < currentNum:
        print("It is higher than the number you inputted")
        main()
    #if it's a letter or something then it lets you try again
    else:
        print("You inputted something wrong!")
        main()
#run the darned function you buffalo if you don't you're dumb
main()


#Luke and Nick tested it, I tested it, and it worked every time!
#the program runs, I did make it break if you got it right, and it loops every time if you get it wrong
#They knew what it was doing because they were doing their own, easy to understand.
#Maybe what the code does, but it says (1-10) in the input thing so it should be easy to understand
#tell the people what the code is doing before they just do it, have the user input the range, and maybe have it see if the number is bigger than 10 before it tells higher or lower