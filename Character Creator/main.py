#Matthew McKinley Character Creator

name = input("What do you want to name your character?")

classy = input("What class do you want your character to be? (Barbarian, Cleric, Fighter, Paladin, Ranger, Rogue, Wizard)")
classes = ["Barbarian", "Cleric", "Fighter", "Paladin", "Ranger", "Rogue", "Wizard"]

race = input("What race do you want your character to be? (Dragonborn, Dwarf, Elf, Halfling, Human, Goblin, Orc)")
races = ["Dragonborn", "Dwarf", "Elf", "Halfling", "Human", "Goblin", "Orc"]



if classy == "Barbarian":
    print("You have 12 HP, 3 Strength, 0 Dexterity, and -1 Intelligence")
elif classy == "Cleric":
    print("You have 9 HP, 1 Strength, 2 Dexterity, and 2 Intelligence")
elif classy == "Fighter":
    print("You have 11 HP, 2 Strength, 1 Dexterity, and 0 Intelligence")
elif classy == "Paladin":
    print("You have 11 HP, 3 Strength, 0 Dexterity, and -1 Intelligence")
elif classy == "Ranger":
    print("You have 8 HP, 1 Strength, 3 Dexterity, and 1 Intelligence")
elif classy == "Rogue":
    print("You have 9 HP, 2 Strength, 2 Dexterity, and 1 Intelligence")
elif classy == "Wizard":
    print("You have 9 HP, 0 Strength, 1 Dexterity, and 3 Intelligence")
else:
    print("Your chosen class is not in the provided list! Try a different one")

if race == "Dragonborn":
    print("You have more Strength and Charisma")
elif race == "Dwarf":
    print("You have more Strength and Wisdom")
elif race == "Elf":
    print("You have Magical capabilities")
elif race == "Halfling":
    print("You have less Strength but have more Dexterity")
elif race == "Human":
    print("You are average.")
elif race == "Goblin":
    print("You have less Strength but more Dexterity")
elif race == "Orc":
    print("You have more Strength and are more Hostile")
else:
    print("Your chosen race is not in the provided list! Try a different one")


if classy in classes:
    print("Your character is named "+name)
    print("Your character is a "+classy)
else:
    print("Your chosen class is not in the provided list! Try a different one")

if race in races:
    print("Your character is a "+race)
else:
    print("Your chosen race is not in the provided list! Try a different one")