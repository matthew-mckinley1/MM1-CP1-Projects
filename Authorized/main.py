#Matthew McKinley Authorized proficiency test

admin = ["Matthew"]
user = ["Matthew", "Nathaniel", "Sawyer", "Luke", "Ethan", "Potato", "Tomato", "Ryan", "Nick", "Turtle"]

name = input("What is your name? (capitalize the first letter)")
if name in admin:
    print("You are THE ADMIN Greater Matthew (or you are lesser matthew which is fine)")
elif name in user:
    print("You have access and are authorized")
else:
    print("YOU ARE UGLY GET OUT OF MY PREMISIS IMMEDIATELY")