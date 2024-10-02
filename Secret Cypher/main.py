#Matthew McKinley Secret Cipher

secret = input("What would you like to be converted?")
shift = 1
changedSecret = ""

def changy(shift, secret, changedSecret):
    for c in secret.lower():
        c2 = ord(c) + shift
        changedSecret += c2
        