#Matthew McKinley What ARE these numbers

num = input("What number would you like to change?")
num = int(num)
comma = "The number with thousand seperators is {num}"
float = "The number with 4 decimal places is"
percent = "The number as a percentage is "
dollar = "The number as a dollar amount is {num:.2f} dollars"

print("The number as a dollar amount is {num:.2f} dollars".format(num))