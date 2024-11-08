#Matthew McKinley the impossible quiz

score = 0
questions = 0
wrong = False

print("The subject for this trivia is animals! Write numbers for each of the questions and it will tell you your score at the end!")
#normal first question
def q1():
    q1 = int(input("What is the only mammal capable of true flight? \n 1) Flying Fox\n 2) Colugo\n 3) Flying Squirrel\n 4) Bat\n"))
    global wrong
    global score
    global questions
    wrong = False
    if q1 == 4:
        score = score + 1
        questions = questions + 1
    elif q1 == 1 or  q1 == 2 or q1 == 3:
        questions = questions + 1
        wrong = True
    else:
        print("You did something wrong!")
        q1()
#hard
def q2():
    q2 = int(input("Which animal possesses the largest brain relative to its body size? \n 1) Elephant\n 2) Sperm Whale\n 3) Dolphin\n 4) Gorilla\n"))
    global wrong
    global score
    global questions
    wrong = False
    if q2 == 2:
        score = score + 1
        questions = questions + 1
    elif q2 == 1 or  q2 == 3 or q2 == 4:
        questions = questions + 1
        wrong = True
    else:
        print("You typed something wrong!")
        q2()
#easy
def q3():
    q3 = int(input("What is the name of the smallest species of penguin? \n 1) Little blue penguin\n 2) Adélie penguin\n 3) Chinstrap penguin\n 4) Gentoo penguin\n"))
    global wrong
    global score
    global questions
    wrong = False
    if q3 == 1:
        score = score + 1
        questions = questions + 1
    elif q3 == 2 or  q3 == 3 or q3 == 4:
        questions = questions + 1
        wrong = True
    else:
        print("You did something wrong!")
        q3()
#easy
def q4():
    q4 = int(input("Which insect hold the record for the fastest flying insect in the world? \n 1) Dragonfly\n 2) Hawk Moth\n 3) Housefly\n 4) Bee\n"))
    global wrong
    global score
    global questions
    wrong = False
    if q4 == 1:
        score = score + 1
        questions = questions + 1
    elif q4 == 2 or  q4 == 3 or q4 == 4:
        questions = questions + 1
        wrong = True
    else:
        print("You did something wrong!")
        q4()
#easy
def q5():
    q5 = int(input("What is the name of the small, elusive mammal native to Australia that is capable of laying eggs? \n 1) Tasmanian devil\n 2) Kangaroo\n 3) Platypus\n 4) Koala\n"))
    global wrong
    global score
    global questions
    wrong = False
    if q5 == 3:
        score = score + 1
        questions = questions + 1
    elif q5 == 1 or  q5 == 2 or q5 == 4:
        questions = questions + 1
        wrong = True
    else:
        print("You did something wrong!")
        q5()
#hard
def q6():
    q6 = int(input("Which bird species is known for its ability to mimic chainsaws and other mechanical sounds? \n 1) Mockingbird\n 2) Lyrebird\n 3) Parrot\n 4) Starling\n"))
    global wrong
    global score
    global questions
    wrong = False
    if q6 == 2:
        score = score + 1
        questions = questions + 1
    elif q6 == 1 or  q6 == 3 or q6 == 4:
        questions = questions + 1
        wrong = True
    else:
        print("You did something wrong!")
        q6()
#easy
def q7():
    q7 = int(input("What is the only species of bear found in the Southern Hemisphere? \n 1) Polar Bear\n 2) Brown Bear\n 3) Spectacled Bear\n 4) Panda Bear\n"))
    global wrong
    global score
    global questions
    wrong = False
    if q7 == 3:
        score = score + 1
        questions = questions + 1
    elif q7 == 1 or  q7 == 2 or q7 == 4:
        questions = questions + 1
        wrong = True
    else:
        print("You did something wrong!")
        q7()

#hard
def q8():
    q8 = int(input("Which animal has the most complex eyesight in the animal kingdom? \n 1) Mantis Shrimp\n 2) Eagle\n 3) Owl\n 4) Cuttlefish\n"))
    global wrong
    global score
    global questions
    wrong = False
    if q8 == 1:
        score = score + 1
        questions = questions + 1
    elif q8 == 2 or  q8 == 3 or q8 == 4:
        questions = questions + 1
        wrong = True
    else:
        print("You did something wrong!")
        q8()

#hard
def q9():
    q9 = int(input("What is the name of the largest living species of turtle, known for its distinctive ridged shell and often found in tropical and subtropical oceans? \n 1) Loggerhead Turtle\n 2) Leatherback Sea Turtle\n 3) Green Sea Turtle\n 4) Hawksbill Turtle\n"))
    global wrong
    global score
    global questions
    wrong = False
    if q9 == 1:
        score = score + 1
        questions = questions + 1
    elif q9 == 2 or  q9 == 3 or q9 == 4:
        questions = questions + 1
        wrong = True
    else:
        print("You did something wrong!")
        q9()

def end():
    print(str(score)+" / "+str(questions))

q1()
if wrong == False:
    q2()
    if wrong == False:
        q6()
        if wrong == False:
            q8()
            if wrong == False:
                q9()
                end()
            else:
                q7()
                end()
        else:
            q5()
            if wrong == False:
                q9()
                end()
            else:
                q7()
                end()
    else:
        q4()
        if wrong == False:
            q8()
            if wrong == False:
                q9()
                end()
            else:
                q7()
                end()
        else:
            q5()
            if wrong == False:
                q9()
                end()
            else:
                q7()
                end()
else:
    q3()
    if wrong == False:
        q6()
        if wrong == False:
            q8()
            if wrong == False:
                q9()
                end()
            else:
                q7()
                end()
        else:
            q5()
            if wrong == False:
                q9()
                end()
            else:
                q7()
                end()
    else:
        q4()
        if wrong == False:
            q8()
            if wrong == False:
                q9()
                end()
            else:
                q7()
                end()
        else:
            q5()
            if wrong == False:
                q9()
                end()
            else:
                q7()
                end()
#()J@O *@OIQJW AN*@OI HOI#!O)H#JNfcIOFHUEFHIjifoejparif