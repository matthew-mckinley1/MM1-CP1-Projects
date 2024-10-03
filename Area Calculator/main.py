#Area Calculator Matthew McKinley





def rectangle():
    length = int(input("How long do you want your rectangle to be?"))
    height = int(input("How tall do you want your rectangle to be?"))
    recArea = length * height
    print(recArea)


user = input("What area would you like to calculate?\n1 for Square or Rectangle\n2 for Triangle\n3 for circle\n4 for trapezoid")
if user == 1:
    rectangle()
elif user == 2:
    triangle()
elif user == 3:
    circle()
elif user == 4:
    trapezoid()
else