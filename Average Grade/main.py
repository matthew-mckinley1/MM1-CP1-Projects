#Matthew McKinley average grade

#all grades inputs make sure they're floats
grade1 = input("What is the grade in your first class?")
grade2 = input("What is the grade in your second class?")
grade3 = input("What is the grade in your third class?")
gradeadv = input("What is the grade in your advisory class?")
grade6 = input("What is the grade in your sixth class?")
grade7 = input("What is the grade in your seventh class?")
grade8 = input("What is the grade in your eigth class?")

grade1 = float(grade1)
grade2 = float(grade2)
grade3 = float(grade3)
gradeadv = float(gradeadv)
grade6 = float(grade6)
grade7 = float(grade7)
grade8 = float(grade8)

totalaverage = (grade1 + grade2 + grade3 + gradeadv + grade6 + grade7 + grade8) / 7
float(totalaverage)
print("Your average grade or GPA is", totalaverage)