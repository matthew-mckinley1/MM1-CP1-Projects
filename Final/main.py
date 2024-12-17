maxHp = 80
tempHp = 80
atkPwr = 20
defense = 5


        
    

def gnomeguardcombat():
    global maxHp
    global tempHp
    global atkPwr
    global defense
    guardHealth = 70
    guardDamage = 20
    while guardHealth > 0 and tempHp > 0:
        print("\nThe gnome guards have", guardHealth, "health left")
        print("You have", tempHp, "health left\n")
        playerinp = int(input("Press 1 to attack or press 2 to heal\n:"))
        if playerinp == 1:
            guardHealth = guardHealth - atkPwr
        elif playerinp == 2:
            if tempHp <= 40:
                tempHp = tempHp + 40
            elif tempHp < 80:
                tempHp = 80
        else:
            print("You didn't put a 1 or a 2")
            continue
        reduced = guardDamage - defense
        tempHp = tempHp - reduced

    if guardHealth <= 0:
        print("The Gnome Guards are DEAD!!!!")
        room3()
    
    elif tempHp <= 0:
        print("YOU DIED")


def gnomedogcombat():
    global maxHp
    global tempHp
    global atkPwr
    global defense
    gnomedoghealth = 70
    gnomedogdamage = 20
    while gnomedoghealth > 0 and tempHp > 0:
        print("\nThe gnome dogs have", gnomedoghealth, "health left")
        print("You have", tempHp, "health left\n")
        playerinp = int(input("Press 1 to attack or press 2 to heal\n:"))
        if playerinp == 1:
            gnomedoghealth = gnomedoghealth - atkPwr
        elif playerinp == 2:
            if tempHp <= 40:
                tempHp = tempHp + 40
            elif tempHp < 80:
                tempHp = 80
        else:
            print("You didn't put a 1 or a 2")
            continue
        reduced = gnomedogdamage - defense
        tempHp = tempHp - reduced

    if gnomedoghealth <= 0:
        print("The Gnome Dogs are DEAD!!!!")
        room5()

    elif tempHp <= 0:
        print("You died")



def gnomewizardcombat():
    global maxHp
    global tempHp
    global atkPwr
    global defense
    gnomewizardhealth = 100
    gnomewizarddamage = 30
    while gnomewizardhealth > 0 and tempHp > 0:
        print("\nThe gnome wizard has", gnomewizardhealth, "health left")
        print("\nYou have", tempHp, "health left\n")
        playerinp = int(input("Press 1 to attack or press 2 to heal\n:"))
        if playerinp == 1:
            gnomewizardhealth = gnomewizardhealth - atkPwr
        elif playerinp == 2:
            if tempHp <= 40:
                tempHp = tempHp + 40
            elif tempHp < 80:
                tempHp = 80
        else:
            print("You didn't put a 1 or a 2")
            continue
        reduced = gnomewizarddamage - defense
        tempHp = tempHp - reduced



        if gnomewizardhealth <= 0:
            print("\nThe Gnome wizard is DEAD!!!!")
            print("\nYou see a blue bubbly liquid inside of a flask. You drink it. You obtained more health, and your health has been restored.")
            maxHp = 130
            tempHp = 130
            inp1 = int(input(("Press 1 to go left and press 2 to go right")))
            if inp1 == 1:
                room7()
            elif inp1 == 2:
                room8()

        elif tempHp <= 0:
            print("You died")



def gnomearchercombat():
    global maxHp
    global tempHp
    global atkPwr
    global defense
    gnomearcherhealth = 90
    gnomearcherdamage = 30
    while gnomearcherhealth > 0 and tempHp > 0:
        print("\nThe gnome archers have", gnomearcherhealth, "health left")
        print("You have", tempHp, "health left\n")
        playerinp = int(input("Press 1 to attack or press 2 to heal\n:"))
        if playerinp == 1:
            gnomearcherhealth = gnomearcherhealth - atkPwr
        elif playerinp == 2:
            if tempHp <= 90:
                tempHp = tempHp + 40
            elif tempHp < 130:
                tempHp = 130
        else:
            print("You didn't put a 1 or a 2")
            continue
        reduced = gnomearcherdamage - defense
        tempHp = tempHp - reduced



        if gnomearcherhealth <= 0:
            print("The Gnome archers are DEAD!!!!")
            print("You see a shiny shield and equip it")
            defense = 20
            room9()

        elif tempHp <= 0:
            print("You died")


def gnomeroguecombat():
    global maxHp
    global tempHp
    global atkPwr
    global defense
    gnomeroguehealth = 90
    gnomeroguedamage = 30
    while gnomeroguehealth > 0 and tempHp > 0:
        print("\nThe gnome rogue has", gnomeroguehealth, "health left")
        print("You have", tempHp, "health left\n")
        playerinp = int(input("Press 1 to attack or press 2 to heal\n:"))
        if playerinp == 1:
            gnomeroguehealth = gnomeroguehealth - atkPwr
        elif playerinp == 2:
            if tempHp <= 90:
                tempHp = tempHp + 40
            elif tempHp < 130:
                tempHp = 130
        else:
            print("You didn't put a 1 or a 2")
            continue
        reduced = gnomeroguedamage - defense
        tempHp = tempHp - reduced


        if gnomeroguehealth <= 0:
            print("The Gnome rogue is DEAD!!!!")
            print("you see a shiny shield and equip it")
            defense = 20
            room9()

        elif tempHp <= 0:
            print("You died")

def gnomebosscombat():
    global maxHp
    global tempHp
    global atkPwr
    global defense
    gnomebosshealth = 200
    gnomebossdamage = 50
    while gnomebosshealth > 0 and tempHp > 0:
        print("\nThe gnome boss has", gnomebosshealth, "health left")
        print("You have", tempHp, "health left\n")
        playerinp = int(input("Press 1 to attack or press 2 to heal\n:"))
        if playerinp == 1:
            gnomebosshealth = gnomebosshealth - atkPwr
        elif playerinp == 2:
            if tempHp <= 90:
                tempHp = tempHp + 40
            elif tempHp < 130:
                tempHp = 130
        else:
            print("You didn't put a 1 or a 2")
            continue
        reduced = gnomebossdamage - defense
        tempHp = tempHp - reduced


        if gnomebosshealth <= 0:
            print("The Gnome boss is DEAD!!!!")
            break

        elif tempHp == 0:
            print("You died")

def room1():
    print("You have entered a gnome cave.")
    inp2 = int(input("Press 1 to go straight and press 2 to go right\n:"))
    if inp2 == 1:
        room2()
    elif inp2 == 2:
        room4()
def room2():
    print("You have entered the room that was straight ahead")
    gnomeguardcombat()
def room3():
    global atkPwr
    print("You have entered the room past the gnome guards, and you see a shiny sword! You equip it and leave behind your copper spork")
    atkPwr = 35
    room6()
def room4():
    print("You have entered the room to the right of the entrance")
    gnomedogcombat()
def room5():
    global atkPwr
    print("You have entered the room past the gnome guards, and you see a shiny sword! You equip it and leave behind your copper spork")
    atkPwr = 35
    room6()
def room6():
    print("You see a big gnome with a wizard hat")
    gnomewizardcombat()
def room7():
    print("You have entered the room to the left, and you see a gnome archer")
    gnomearchercombat()
def room8():
    print("You have entered the room to the right, when all of a sudden, a rogue gnome jumps out from the shadows behind you.")
    gnomeroguecombat()
def room9():
    print("You have entered the FINAL ROOM HAHAHAHAHAHAAHHAHAHA. There is one big gnome in the center of an arena")
    gnomebosscombat()
room1()