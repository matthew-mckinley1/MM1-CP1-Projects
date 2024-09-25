#Personal Information Converter Matthew McKinley

name = input("What is your name?")
age = input("How old are you?")
heightMeters = input("What is your height in meters")
favnum = input("What is your favorite number?")

newAge = int(age)
newFavNum = int(favnum)
newHeightMeters = float(heightMeters)

print("Your name is", name, "You are", age, "or", newAge, "years old, you are", newHeightMeters,"or", heightMeters, "meters tall, and your favorite number is", favnum, "and", newFavNum)