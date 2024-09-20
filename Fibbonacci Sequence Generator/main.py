#fibbonacci sequencec genearator i hate this project Matthew McKinley



totalruns = 20
num1 = 0
num2 = 1
num3 = num2  
runs = 1

while totalruns >= runs:
    print(num3, end=" ")
    runs += 1
    num1, num2 = num2, num3
    num3 = num1 + num2
print()