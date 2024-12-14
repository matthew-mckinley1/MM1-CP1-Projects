maxHp = 80
tempHp = 80
atkPwr = 20
defense = 15
hpPotions = 5

def gnomeguardcombat():
    global maxHp
    global tempHp
    global atkPwr
    global defense
    global hpPotions
    guardHealth = 50
    guardDamage = 10
    while guardHealth > 0 and tempHp > 0:
        print("The gnome guards have ", guardHealth, "left")
        print("You have ", tempHp, "left")
        playerinp = input("Press 1 to attack or press 2 to heal")
        if playerinp == 1:
            guardHealth = guardHealth - atkPwr
        elif playerinp == 2:
            if tempHp <= 50:
                tempHp = tempHp + 30
            elif tempHp < 80:
                tempHp == 80
        else:
            print("You didn't put a 1 or a 2")
            continue
gnomeguardcombat()
"""
Take a random number from 1 or 2
If the number is 1, then remove 10 hp from player health
If the number is 2, then add 20 hp to guardhealth, can’t go over 50
"""