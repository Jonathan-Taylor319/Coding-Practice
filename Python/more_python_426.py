
# Task:
# Given a list of numbers, return a list of the even numbers doubled.
x = [1, 2, 3, 4, 5]
# Expected Output: [4, 8]

# ✅ Brute first.
# ✅ Then 1-line list comprehension if you can.

# doubled_even = [for num in x and num * 2 if num % 2 == 0:]
#num * 2 - multiply the num by 2
#for num in x - loop through nums in x
#if num %2 == 0 -
# doubled_even = [num * 2 for num in x if num % 2 == 0]
# print(doubled_even)

# nums = [1, 2, 3, 4, 5]
# # 🔥 Expected: [2, 6, 10]
# double_odds = [num * 2 for num in nums if num % 2 != 0]
# print(double_odds)

# nums = [2, 3, 6, 7, 9, 12]
# #square num
# #for numbers in num
# #if num divisible by 3
# num_squared = [num * num for num in nums if num % 3 == 0]
# print(num_squared)

#don't forget exponent = num ** 2 or to whatever power

# words = ["a", "cat", "apple", "hi", "banana"]
# # # 🔥 Expected: ["apple", "banana"]
# # #each word
# # #in words list
# # #that is longer than length of 3
# longer_3 = [word.upper() for word in words if len(word) > 3]
# print(longer_3)

# words = ["hello", "world", "in", "a", "frame"]
# #word[::1] - reverse the word with slicing
# #for word in word - loop all words
# #if len(word) >=4 if length of word is euqal to or over 4
# backwords = [word[::-1] for word in words if len(word) >= 4]
# print(backwords)

# names = ["alice", "bob", "charlie", "derek", "eve"]
# #name.capialize() = capitalize the name
# #for name in names
# #that are longer than 3
# long_names = [name.capitalize() for name in names if len(name) > 3]
# #was going to slice and upper that slice not sure if i can?
# print(long_names)

# #some built in letter functions 
# text = "hello world"
# print(text.capitalize()) = Hello world
# print(text.upper()) = HELLO WORLD
# print(text.lower()) = hello world
# print(text.title()) = hello world

# cities = ["new york", "la", "chicago", "houston", "phx", "seattle"]

# # 🔥 Challenge:
# # 1. Only pick city names that are longer than 3 letters.
# # 2. Capitalize each selected city properly (first letter uppercase).

# # Example Output:
# # ['New york', 'Chicago', 'Houston', 'Seattle']
# #capitalize names
# #for cities in list of cities
# #that have a length longer than 3
# long_cities = [name.capitalize() for name in cities if len(name) > 3]
# print(long_cities)


# Given a string s, find the first non-repeating character in it and return its index.
# If it doesn't exist, return -1.

# x = "leetcode"
# # Output: 0  # 'l' is the first unique letter
# y = "loveleetcode"
# # Output: 2  # 'v' is the first unique letter
# z = "aabb"
# # Output: -1  # No unique characters

# # define a function first_unique(s)
# def first_unique(j):
#     #create an empty dict
#     letter_count = {}
#     #loop through the letters and count
#     for char in j:
#         #populate our dictionary
#         letter_count[char] = letter_count.get(char, 0) +1
#     #print our dict to see what we got?
#     # print(letter_count)
#     #now we loop again and enumerate and check for indexes 
#     for idx, char in enumerate(j):
#         #compare to see when there is only 1 count of a letter?
#         if letter_count[char] == 1:
#             #return the index of the enumeration?
#             return idx
#     return -1

# print(first_unique(x))
# print(first_unique(y))
# print(first_unique(z))

# Problem Type | What you do
# First unique character | Find the first letter with count == 1
# Duplicates | Check if any letter/number has count > 1
# Anagrams | Compare two hashmaps — if they match, it’s an anagram!
# Majority element | Find the element with count > n/2
# Frequency analysis | See what appears most often
# Grouping by count | Build lists of items with the same count