#Matthew McKinley Fibbonacci Sequence Generator

num1 = 0
num2 = 1
num3 = num1+num2
printo = ""

for num3 in (0,3000):
    num1 = num2
    num2 = num3
    num3 = num1+num2
    printo+=str(num1)
    num1 = int(num1)
    print(printo)


#print(printo)
#printo+=num1