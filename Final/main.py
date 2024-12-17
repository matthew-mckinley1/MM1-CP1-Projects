maxHp = 80
tempHp = 80
atkPwr = 20
defense = 5
hpPotions = 10
GnomeGuardsDead = False
GnomeDogsDead = False

def playerDeath():
    print("You died!")
    playagain()
def playagain():
    inp3 = input("Would you like to play again? Y/N")
        if inp3 == "Y"
            room1()
        elif inp3 == "N"
            break
        else:
            print("You did not put a Y or an N")
            continue
    

def gnomeguardcombat():
    global maxHp
    global tempHp
    global atkPwr
    global defense
    global hpPotions
    global GnomeGuardsDead
    guardHealth = 70
    guardDamage = 20
    while guardHealth > 0 and tempHp > 0:
        print("The gnome guards have", guardHealth, "health left")
        print("You have", tempHp, "health left")
        playerinp = int(input("Press 1 to attack or press 2 to heal\n:"))
        if playerinp == 1:
            guardHealth = guardHealth - atkPwr
        elif playerinp == 2:
            hpPotions = hpPotions - 1
            if tempHp <= 50:
                tempHp = tempHp + 30
            elif tempHp < 80:
                tempHp = 80
        else:
            print("You didn't put a 1 or a 2")
            continue

        reduced = guardDamage - defense
        tempHp = tempHp - reduced

    else:
        if tempHp == 0:
            playerDeath()
        elif guardHealth == 0:
            GnomeGuardsDead = True
            print("The Gnome Guards are DEAD!!!!")
            room3()


def gnomedogcombat():
    global maxHp
    global tempHp
    global atkPwr
    global defense
    global hpPotions
    global GnomeDogsDead
    gnomedoghealth = 70
    gnomedogdamage = 20
    while gnomedoghealth > 0 and tempHp > 0:
        print("The gnome dogs have", gnomedoghealth, "health left")
        print("You have", tempHp, "health left")
        playerinp = int(input("Press 1 to attack or press 2 to heal\n:"))
        if playerinp == 1:
            gnomedoghealth = gnomedoghealth - atkPwr
        elif playerinp == 2:
            hpPotions = hpPotions - 1
            if tempHp <= 50:
                tempHp = tempHp + 30
            elif tempHp < 80:
                tempHp = 80
        else:
            print("You didn't put a 1 or a 2")
            continue
        reduced = gnomedogdamage - defense
        tempHp = tempHp - reduced

    else:
        if tempHp == 0:
            playerDeath()
        elif gnomedoghealth == 0:
            gnomedoghealth = True
            print("The Gnome Dogs are DEAD!!!!")
            room5()


def gnomewizardcombat():
    global maxHp
    global tempHp
    global atkPwr
    global defense
    global hpPotions
    gnomewizardhealth = 100
    gnomewizarddamage = 30
    while gnomewizardhealth > 0 and tempHp > 0:
        print("The gnome wizard has", gnomewizardhealth, "health left")
        print("You have", tempHp, "health left")
        playerinp = int(input("Press 1 to attack or press 2 to heal\n:"))
        if playerinp == 1:
            gnomewizardhealth = gnomewizardhealth - atkPwr
        elif playerinp == 2:
            hpPotions = hpPotions - 1
            if tempHp <= 50:
                tempHp = tempHp + 30
            elif tempHp < 80:
                tempHp = 80
        else:
            print("You didn't put a 1 or a 2")
            continue

        reduced = gnomewizarddamage - defense
        tempHp = tempHp - reduced

    else:
        if tempHp == 0:
            playerDeath()
        elif gnomewizardhealth == 0:
            gnomewizardhealth = True
            print("The Gnome wizard is DEAD!!!!")
            inp1 = int("Press 1 to go left and press 2 to go right")
            if inp1 == 1
                room7()
            elif inp == 2
                room8()


def gnomearchercombat():
    global maxHp
    global tempHp
    global atkPwr
    global defense
    global hpPotions
    gnomearcherhealth = 90
    gnomearcherdamage = 30
    while gnomearcherhealth > 0 and tempHp > 0:
        print("The gnome archers have", gnomearcherhealth, "health left")
        print("You have", tempHp, "health left")
        playerinp = int(input("Press 1 to attack or press 2 to heal\n:"))
        if playerinp == 1:
            gnomearcherhealth = gnomearcherhealth - atkPwr
        elif playerinp == 2:
            hpPotions = hpPotions - 1
            if tempHp <= 50:
                tempHp = tempHp + 30
            elif tempHp < 80:
                tempHp = 80
        else:
            print("You didn't put a 1 or a 2")
            continue

        reduced = gnomearcherdamage - defense
        tempHp = tempHp - reduced

    else:
        if tempHp == 0:
            playerDeath()
        elif gnomearcherhealth == 0:
            gnomearcherhealth = True
            print("The Gnome archers are DEAD!!!!")


def gnomeroguecombat():
    global maxHp
    global tempHp
    global atkPwr
    global defense
    global hpPotions
    gnomeroguehealth = 90
    gnomeroguedamage = 30
    while gnomeroguehealth > 0 and tempHp > 0:
        print("The gnome rogue has", gnomeroguehealth, "health left")
        print("You have", tempHp, "health left")
        playerinp = int(input("Press 1 to attack or press 2 to heal\n:"))
        if playerinp == 1:
            gnomeroguehealth = gnomeroguehealth - atkPwr
        elif playerinp == 2:
            hpPotions = hpPotions - 1
            if tempHp <= 50:
                tempHp = tempHp + 30
            elif tempHp < 80:
                tempHp = 80
        else:
            print("You didn't put a 1 or a 2")
            continue

        reduced = gnomeroguedamage - defense
        tempHp = tempHp - reduced

    else:
        if tempHp == 0:
            playerDeath()
        elif gnomeroguehealth == 0:
            gnomeroguehealth = True
            print("The Gnome rogue is DEAD!!!!")


def gnomebosscombat():
    global maxHp
    global tempHp
    global atkPwr
    global defense
    global hpPotions
    gnomebosshealth = 200
    gnomebossdamage = 50
    while gnomebosshealth > 0 and tempHp > 0:
        print("The gnome boss has", gnomebosshealth, "health left")
        print("You have", tempHp, "health left")
        playerinp = int(input("Press 1 to attack or press 2 to heal\n:"))
        if playerinp == 1:
            gnomebosshealth = gnomebosshealth - atkPwr
        elif playerinp == 2:
            hpPotions = hpPotions - 1
            if tempHp <= 50:
                tempHp = tempHp + 30
            elif tempHp < 80:
                tempHp = 80
        else:
            print("You didn't put a 1 or a 2")
            continue

        reduced = gnomebossdamage - defense
        tempHp = tempHp - reduced

    else:
        if tempHp == 0:
            playerDeath()
        elif gnomebosshealth == 0:
            gnomebosshealth = True
            print("The Gnome rogue is DEAD!!!!")


def room1():
    print("You have entered a gnome cave")
    inp2 = input("Press 1 to go straight and press 2 to go right")
    if inp2 == 1
        room2()
    elif inp2 == 2
        room4()
def room2()
    print("You have entered the room that was straight ahead")
    gnomeguardcombat()
def room3()
    print("You have entered the room past the gnome guards, and you see a shiny sword! You equip it and leave behind your copper spork")
    atkPwr = 35
    room6()
def room4()
    print("You have entered the room to the right of the entrance")
    gnomedogcombat()
def room5()
    print("You have entered the room past the gnome guards, and you see a shiny sword! You equip it and leave behind your copper spork")
    atkPwr = 35
def room6()
    print("You see a big gnome with a wizard hat")
    gnomewizardcombat()
def room7()
    print("You have entered the room to the left, and you see a gnome archer")
    gnomearchercombat()
def room8()
    print("You have entered the room to the right, when all of a sudden, a rogue gnome jumps out from the shadows behind you.")
def room9()
    print("You have entered the FINAL ROOM HAHAHAHAHAHAAHHAHAHA. There is one big gnome in the center of an arena")