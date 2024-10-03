#Matthew McKinley Secret Cipher

secret = list(input("What would you like to be converted?"))
length = len(secret) - 1
shift = 3
num = 0
secretWord = ""
while num <= length:
    currentChar = secret[num]
    currentChar = ord(currentChar)
    currentChar = currentChar + shift
    currentChar = chr(currentChar)
    secretWord += currentChar
    num += 1
print(secretWord)
