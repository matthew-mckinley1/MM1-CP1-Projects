#Area Calculator Matthew McKinley

def rectangle():
    length = int(input("How long do you want your square/rectangle to be?"))
    height = int(input("How tall do you want your square/rectangle to be?"))
    recArea = length * height
    print(recArea)
def triangle():
    length = int(input("How long do you want your triangle to be?"))
    height = int(input("How tall do you want your triangle to be?"))
    triArea = (length * height)/2
    print(triArea)
def circle():
    radius = int(input("How wide do you want your circle to be?"))
    circleArea = (radius**2)*3.1415926535
    print(circleArea)
def trapezoid():
    base1 = int(input("How long do you want your first base to be (bottom line)"))
    base2 = int(input("How long do you want your second base to be (top line)"))
    height = int(input("How tall do you want your trapezoid to be?"))
    trapArea = ((base1 + base2)/2)*height
    print(trapArea)

user = int(input("What area would you like to calculate?\n1 for Square or Rectangle\n2 for Triangle\n3 for circle\n4 for trapezoid\n:"))
if user == 1:
    rectangle()
elif user == 2:
    triangle()
elif user == 3:
    circle()
elif user == 4:
    trapezoid()
else:
    print("You typed something wrong! YOU BUFFALO")