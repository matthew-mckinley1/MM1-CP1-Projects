#Matthew McKinley Counting Characters

grid = [
['A', 'B', 'C', 'A', 'D'],
['C', 'A', 'B', 'D', 'E'],
['A', 'D', 'C', 'E', 'A'],
['B', 'A', 'C', 'A', 'D'],
['D', 'C', 'B', 'E', 'A'] ]

a = int(0)
b = int(0)
c = int(0)
d = int(0)
e = int(0)

for row in grid:
    for letter in row:
        if letter == "A":
            a = a + 1
        elif letter == "B":
            b = b + 1
        elif letter == "C":
            c = c + 1
        elif letter == "D":
            d = d + 1
        elif letter == "E":
            e = e + 1
print("A =",a,"B =",b,"C =",c,"D =",d,"E =",e)
