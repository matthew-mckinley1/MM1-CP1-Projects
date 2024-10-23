#Matthew McKinley What ARE these numbers

x = float(input("What number would you like to change?"))

thous = "The number in thousands is {tho:,.0f}"
print(thous.format(tho = x))

dollar = "The number as a dollar amount is {price:.2f} dollars"
print(dollar.format(price = x))

floaty = "The number as a float with 4 decimal places is {floaty:.4f}"
print(floaty.format(floaty = x))

percent = "The number as a percentage is {percents:.0%}"
print(percent.format(percents = x))