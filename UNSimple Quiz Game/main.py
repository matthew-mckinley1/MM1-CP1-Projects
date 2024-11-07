#Matthew McKinley the impossible quiz

score = 0
questions = 0


print("The subject for this trivia is animals! Write numbers for each of the questions and it will tell you your score at the end!")
#normal first question
def q1():
    q1 = int(input("What is the only mammal capable of true flight? \n 1) Flying Fox\n 2) Colugo\n 3) Flying Squirrel\n 4) Bat\n"))
    if q1 == 4:
        score = score + 1
        questions = questions + 1
    elif q1 == 1 or  q1 == 2 or q1 == 3:
        questions = questions + 1
    else:
        print("You did something wrong!")
        q1()
#
def q2():
    q2 = int(input("Which animal possesses the largest brain relative to its body size? \n 1) Elephant\n 2) Sperm Whale\n 3) Dolphin\n 4) Gorilla\n"))
    if q2 == 2:
        score = score + 1
        questions = questions + 1
    elif q2 == 1 or  q2 == 3 or q2 == 4:
        questions = questions + 1
    else:
        print("You typed something wrong!")
        q2()
#
def q3():
    q3 = int(input("What is the name of the smallest species of penguin? \n 1) Little blue penguin\n 2) Adélie penguin\n 3) Chinstrap penguin\n 4) Gentoo penguin\n"))
    if q3 == 1:
        score = score + 1
        questions = questions + 1
    elif q3 == 2 or  q3 == 3 or q3 == 4:
        questions = questions + 1
    else:
        print("You did something wrong!")
        q3()
#
def q4():
    q4 = int(input("Which insect hold the record for the fastest flying insect in the world? \n 1) Dragonfly\n 2) Hawk Moth\n 3) Housefly\n 4) Bee\n"))
    if q4 == 1:
        score = score + 1
        questions = questions + 1
    elif q4 == 2 or  q4 == 3 or q4 == 4:
        questions = questions + 1
    else:
        print("You did something wrong!")
        q4()
#
def q5():
    q5 = int(input("What is the name of the small, elusive mammal native to Australia that is capable of laying eggs? \n 1) Tasmanian devil\n 2) Kangaroo\n 3) Platypus\n 4) Koala\n"))
    if q5 == 3:
        score = score + 1
        questions = questions + 1
    elif q5 == 1 or  q5 == 2 or q5 == 4:
        questions = questions + 1
    else:
        print("You did something wrong!")
        q5()
#
def q6():
    q6 = int(input("Which bird species is known for its ability to mimic chainsaws and other mechanical sounds? \n 1) Mockingbird\n 2) Lyrebird\n 3) Parrot\n 4) Starling\n"))
    if q6 == 2:
        score = score + 1
        questions = questions + 1
    elif q6 == 1 or  q6 == 3 or q6 == 4:
        questions = questions + 1
    else:
        print("You did something wrong!")
        q6()
#
def q7():
    q7 = int(input("Which bird species is known for its ability to mimic chainsaws and other mechanical sounds? \n 1) Mockingbird\n 2) Lyrebird\n 3) Parrot\n 4) Starling\n"))
    if q7 == 2:
        score = score + 1
        questions = questions + 1
    elif q7 == 1 or  q7 == 3 or q7 == 4:
        questions = questions + 1
    else:
        print("You did something wrong!")
        q7()