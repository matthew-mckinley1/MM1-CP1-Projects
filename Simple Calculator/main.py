#Matthew McKinley Simple Calculatoer
#nums
num1 = input("What is the first number you would like to have math done on?")
num2 = input("What is the second number you would like to have math done on?")
#integers cuz why not
num1 = int(num1)
num2 = int(num2)

#ALL OF THE POSSIBLE OPTIONS?!!?!
#add sub mult div mod expo FLOORdivision
operator = input("Push 1 for addition\nPush 2 for subtraction\nPush 3 for multiplication\nPush 4 for division\nPush 5 for modulo\nPush 6 for exponents\nPush 7 for rounded division")
operator = int(operator)
if operator == 1:
    num3 = num1+num2
    print(str(num3))
elif operator == 2:
    num3 = num1-num2
    print(str(num3))
elif operator == 3:
    num3 = num1*num2
    print(str(num3))
elif operator == 4:
    num3 = num1/num2
    print(str(num3))
elif operator == 5:
    num3 = num1%num2
    print(str(num3))
elif operator == 6:
    num3 = num1**num2
    print(str(num3))
elif operator == 7:
    num3 = num1//num2
    print(str(num3))
else:
    print("You typed something wrong! YOU IDIOT")

