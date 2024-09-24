#Matthew McKinley Graded Quiz

print("It will ask questions, make sure to answer TRUE or FALSE and have them uncapitalized")

score = 0

q1 = input("Does the adult human skeleton have 206 bones?")
if q1 == "true":
    score+=1
else:
    print("Sorry, you got this one wrong!")


q2 = input("Is the amazon river the longest river in the world?")
if q2 == "false":
    score+=1
else:
    print("Sorry, you got this one wrong!")


q3 = input('Is a group of crows called a "murder"')
if q3 == "true":
    score+=1
else:
    print("Sorry, you got this one wrong!")


q4 = input("Can I jump higher than the Eiffel Tower")
if q4 == "true":
    score += 1
else:
    print("Sorry, you got this one wrong!")


q5 = input("Do dolphins sleep with both eyes closed?")
if q5 == "false":
    score += 1
else:
    print("Sorry, you got this one wrong!")
print("You got",score,"out of 5 questions correct!")

