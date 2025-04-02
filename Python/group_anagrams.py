# Group Anagrams
# Problem:
# Given an array of strings, group the anagrams together.
# Example: ["eat", "tea", "tan", "ate", "nat", "bat"] should group as [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]].

# Focus:
# String manipulation, sorting, and using dictionaries as hash maps.

# Hint:
# For each word, sort the characters to form a key and use this key to group words in a dictionary.

#create a function - takes in a list

x = ["eat", "tea", "tan", "ate", "nat", "bat"]

def group_anagrams(x):
    
    