#RAID: Anagram Creator Matthew McKinley

import random

word = input("What word would you like to have scrambled?")
wordList = list(word.lower())
random.shuffle(wordList)
complete = "".join(wordList).title()
print(complete)





#use .title when you're printing to have it capitalized good ig