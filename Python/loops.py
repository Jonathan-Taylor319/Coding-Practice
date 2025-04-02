# a place to smash loops in to my brain till i can loop in my sleep one handed

# words = ["hello", "world", "loop", "me"]
# for word in words:
#     print(word.upper())
    
#words = ["hello", "world", "loop", "me"]
# for i in words:
#     if "o" not in i.lower():
#         print(i)

#stuff = ["this", "is", "a", "new", "list"]

# for apples in stuff:
#     if "i" in apples.lower():
#         print(apples)

# words.sort()
# for x in words:
#     print()
#     print(len(x))

# same as above but fancier and works in python 3.6
# for i, word in enumerate(words, start=1):
#     print(f"this is the length of {i}: {len(word)}")
    
# cards = ["Diamonds", "Spades", "Hearts", "Clubs"]

# enumerate = built-in python function that adds a counter to any iterable and returns item as a pair (index, value)
# for i , card in enumerate(cards, start=1):
    #f"" = string interpulation - {the var in these will be the value of the var}
    #{i} = the iteration
    #{card} = the value from the list in each iteration
    #{len(card)} = the length of the str
    # print(f"{i}. {card} has {len(card)} letters.")

# cards.sort()

# for i, card in enumerate(cards, start=1):
#     print(i, card)

# print(cards)
# print(words)
# print(stuff)

# for foobar in cards:
#     if "he" in foobar.lower():
#         print("the answer below should be Hearts")
#         print(foobar)

# for i, word in enumerate(words, start=1):
#     print(i,":", word)

    #input  
# words = ["hello", "world", "python", "loop"]
    #emptyt dictionary
# letter_counts = []
    # want's me to loop through a list of strings
    #count how many times each letter appears across all of them
    # store it in our dictionary
    # print the count

    #Use .lower() so letters like 'H' and 'h' are treated the same 

    #Skip spaces and punctuation if any show up
# for a in words:
#     a.lower()
#     a.split()
#     letter_counts.append(a)
#     print(letter_counts) 

# Here's What You're Doing Wrong (Buckle Up):
# ❌ a.lower() — you did it, but you didn’t use it
# This method returns a new string. You didn’t assign it back.
# So this does absolutely nothing. It’s the no-op equivalent of a shrug.

# ❌ a.split() — why?? It’s already a string
# Are you trying to split the word into words? It’s already a word. You're holding a banana and trying to peel a pretzel.

# ❌ letter_counts.append(a) — you’re appending to a dict like it’s a list
# letter_counts is supposed to be a dictionary.
# .append() is for lists. You're trying to plug a USB cable into a potato.

# # list of strings as input
# words = ["hello", "world", "python", "loop"]
# # create an empty dictionary to hold our letters and counts
# letter_counts = {}
# #we are looping through each word in words list
# for word in words:
#     # make the word lowercase / have to re-asagin because str are immutable
#     word = word.lower()
#     # now we are looping through each letter in the word
#     for letter in word:
#         #the .isalpha() = makes sure we only count letters
#         if letter.isalpha():
#             # Update the count / 
#             # letter_counts[letter] means in letter counts if that letter exists replace the value, if not create it
#             #letter_counts(letter, 0) + 1 means does it exsit - if yes give the value, if not give me 0 / then w add 1 because of +1 (we are counting)
#             #those put together count safely without having to check
#             letter_counts[letter] = letter_counts.get(letter, 0) + 1
# print(letter_counts)

# initial impression soooooo we have to nest a loop inside a loop to get the letters? weird concept ----

# Each word is a string, and in Python, a string is already iterable—meaning you can loop through each character like it’s a list of tiny problems.

# for word in words:
#     for letter in word:
        # You're here. Inside the letter dimension now.

# It may feel weird because:

# You’re used to looping through lists.

# But now you’re looping through each character in a string.

# Strings are sequences too. They just hide it better.

# So yes: two loops.

# Outer loop: each word in the list

# Inner loop: each letter in the word

# Get comfy. Nested loops are like onions—layered and make people cry.

# TL;DR Cheat Sheet
# ✅ Nested loop → break each word into letters.

# ✅ letter_counts[letter] → access/update count for one specific letter.

# ✅ .get(letter, 0) → avoids errors if letter doesn't exist yet.

# numbers = [123, 456, 789, 123, 111]
# #create an empty dict
# digit_counts = {}
# #need to convert the int to str
# for number in numbers:
#     for digit in str(number):
#         digit_counts[digit] = digit_counts.get(digit, 0) + 1
# print(digit_counts)

# ✏️ Take This Mental Note:
# str(numbers) → BAD → turns list into weird string like "[123, 456]"

# str(number) inside the loop → GOOD → converts each int to string individually

# Never use your variable name (digit_counts) as a loop variable. That’s like naming your kid int.

# numbers = [101, 202, 303, 404, 505, 606, 707, 808, 909, 1001]

# digi_count = {}

# for num in numbers:
#     for digi in str(num):
#         digi_count[digi] = digi_count.get(digi, 0) +1
# print(digi_count)

#  .items() gives (key, value) pair from dict
#  max(..., key=lambda item: item[1]) finds the pair with the highs val
#  the min(...) skips anything that's zero
 
# most_common = max(digi_count.items(), key=lambda item: item[1])
# least_common = min((item for item in digi_count.items() if item[1] > 0), key=lambda item: item[1])

# print(f"\nMost common digit: {most_common[0]} appeared {most_common[1]} times")
# print(f"\nLeast common digit: {least_common[0]} apeared {least_common[1]} times")

#--------- counting practice using a dictionary -------
#counting letters first 
# text = "banana"
# letter_count = {}
# for letter in text:
#     letter_count[letter] = letter_count.get(letter, 0) + 1
# print(text)
# print(letter_count)

# state = "mississippi"
# for stuff in state:
#     letter_count[stuff] = letter_count.get(stuff, 0) + 1
# print(state)
# print(letter_count)

# foo = "lets see if we can bring the count down"
# for i in foo.lower():
#     #ensure only letters get counted / skips spaces and punctuation
#     if i.isalpha():    
#         letter_count[i] = letter_count.get(i, 0) -1
# print(foo)
# print(letter_count)

# word = "babaaabaaarrrrrraaaaaaan"
# beach_boy = {}
# for something in word:
#     beach_boy[something] = beach_boy.get(something, 0) +1
# print(word)
# print(beach_boy)
        
# stapler = "staaaaapppppppllllllleeeeessssszzzzeeeessszzzzzz"
# how_many = {}
# for s in stapler:
#     how_many[s] = how_many.get(s, 0) + 1
# print(stapler)
# print(how_many)

# e = "simple"
# a = {}
# for v in e:
#     a[v] = a.get(v, 0) +1
# print(e)
# print(a)

#-------some more counting letters -------

go = "grEen light"
stop = "red liGht"
yellow = "smAsh tHe gas"
blue = "WHAT"

big_letter = {}
little_letter = {}

colors = [go, stop, yellow, blue]
print(f"my colors are, {colors}")

#first attempt is to get count of only uppercase / change to get upper and lower
for color in colors:
    for char in color:
        if char.isupper():
            big_letter[char] = big_letter.get(char, 0) +1
        elif char.islower():
            little_letter[char] = little_letter.get(char, 0) +1

print(big_letter)
print(little_letter)

# -- end of this practice ---- going back and pracitincing even more loops in another file