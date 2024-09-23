#Matthew McKinley Palindrome
print("This is the palindrome checker!")
word = input("What would you like to test?")
checks = word[::-1]

if checks == word:
    print("This is a palindrome!")
else:
    print("This word is not a palindrome")