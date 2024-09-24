#Matthew McKinley Graded Quiz

print("It will ask questions, make sure to answer yes or no and have them uncapitalized")

score = 0

q1 = input("Are blobfish ugly?")
if q1 == "no":
    score+=1
else:
    print("Sorry, you got this one wrong!")


q2 = input("Are goldfish better than dogs?")
if q2 == "yes":
    score+=1
else:
    print("Sorry, you got this one wrong!")


q3 = input("Are pancakes better than waffles?")
if q3 == "no":
    score+=1
else:
    print("Sorry, you got this one wrong!")


q4 = input("Are dinosaur-shaped chicken nuggets a calzone?")
if q4 == "yes":
    score += 1
else:
    print("Sorry, you got this one wrong!")


q5 = input("Is a tomato a fruit?")
if q5 == "no":
    score += 1
else:
    print("Sorry, you got this one wrong!")
print("You got",score,"out of 5 questions correct!")

