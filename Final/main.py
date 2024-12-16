maxHp = 80
tempHp = 80
atkPwr = 20
defense = 15
hpPotions = 10
GnomeGuardsDead = False
GnomeDogsDead = False

def playerDeath():


def gnomeguardcombat():
    global maxHp
    global tempHp
    global atkPwr
    global defense
    global hpPotions
    global GnomeGuardsDead
    guardHealth = 50
    guardDamage = 10
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

        tempHp = tempHp - guardDamage
    else:
        if tempHp == 0:
            playerDeath()
        elif guardHealth == 0:
            GnomeGuardsDead = True
            print("The Gnome Guards are DEAD!!!!")
            
