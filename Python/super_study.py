# 📅 7-DAY STUDY BLUEPRINT: "One Week to Become a Python Weapon"

# Day	Focus	Topics	Tools / Practice
# 1️⃣	Data Structures Deep Dive	Lists, Sets, Dicts, Tuples, Stacks, Queues, basic ops, use cases	Copy drills, .get(), .items(), collections, flashcards
# 2️⃣	Big O + Built-ins	Time complexity, .sort(), sum(), max() w/ key, lambda, slicing	Write Big O for each drill, analyze brute vs optimized
# 3️⃣	Algorithms Day 1: Patterns	Two pointers, Sliding Window, Frequency Counter, Hashmap tricks	Leetcode Easy: [Two Sum], [Longest Substring], etc
# 4️⃣	Algorithms Day 2: Logic Boost	Sorting, Prefix Sums, Greedy, Problem Breakdown	Leetcode Medium + our custom logic drills
# 5️⃣	Interview Core + Python Pro Tips	Practice whiteboard problems, talk-throughs, advanced list comp, enumerate, zip, map, filter	Mock with me, dry-run problems
# 6️⃣	Pinterest Brain Day	Engineering blog deep dive, project highlights, thoughtful questions	Read + prep 2-3 insights to mention. Be “Pinterest-aware”
# 7️⃣	Full Simulation + Brain Bath	Simulate 45-min interview, final review, behavioral Qs, confidence boost	You VS You mode. I play bad cop. Or worse, recruiter cop.


# day one - 
# 🎓 Today’s Kickoff: Day 1 – Data Structures + Built-ins
# ✅ Lists
# ✅ Dicts
# ✅ Sets
# ✅ Tuples
# ✅ Built-in Functions (sum, max, sorted, slicing, enumerate)
# ✅ Copy drills and cheat-proof warmups
# ✅ When to use what (with Big O)
# ✅ Then: Intro to Classes (if we have gas left)


# ✅ Big O to keep track of and understand as we go -----
# 🧠 Big O for Beginners (The “Do I Need to Care?” Guide)
# Imagine you're at the store, scanning items:


# Code Type	Big O	Real-Life Metaphor
# O(1) (Constant time)	1 step	Grab one item off the shelf. Always 1 step, no matter what.
# O(n) (Linear time)	grows w/ n	Scan every item in the cart. More items? More time.
# O(n²) (Quadratic)	double loop	For every shirt, try every pair of pants. Fashion hell.
# O(log n) (Logarithmic)	shrink fast	Cut a phone book in half each time. Binary search.
# You’re Mostly Dealing With:
# ✅ O(1) — access item in list or dict by index/key
# ✅ O(n) — loop through list/dict/string
# 🚩 O(n²) — nested loops (like comparing every pair of things)

# So yeah — everything you’ve written so far is O(n). And that’s fine. For now.

# Do You Need to Know Big O Yet?
# Not deeply. But...

# You should notice when you're doing something like double looping — that's the start of Big O awareness.

# You don’t need to calculate exact Big O on every line right now.

# You’ll absorb it over time, especially when we hit sorting, searching, recursion, etc.

# You focus on building and understanding, and I’ll sprinkle in Big O when it matters. Like when you're about to write a nested loop with tears in your eyes.


# 🛠️ DRILL LIST: The Monkey Forge
# 🟩 LISTS
# Create a list of numbers and sum() it manually.
# nums = [1, 4, 7, 9, 25, 14, 10]

# def num_add(x):
#     #need to keep this before the loop to keep constant tally
#     total = 0
#     #loop through whole list
#     for i in nums:
#         #add current num to our current "total"
#         total += i
#     #return outside the loop to make sure it updates
#     return total
# print(num_add(nums))

# 🔍 Big O: O(n) - Linear time - grows with the lists - more items more time...
# Why? You're looping through each number once.
# n = length of the list.
# When it matters: With huge lists (millions+), this grows linearly with size.
# Can you improve it? Only by using sum() which is optimized internally in C, but still O(n) in time.

# Use sum() to do the same.
#was a guess(the syntax) but it worked ---- easy
# total_nums = sum(nums)
# print(total_nums)
# 🔍 Big O: O(n) - linear time - more items - more time
# Why? Under the hood, Python still loops through the list. It just hides the loop from you.

# Use list comprehension to square each even number.

#shit.....did i get that right on the first try?
# squared_evens = [i ** 2 for i in nums if i % 2 == 0]
# print(squared_evens)

# 🔍 Big O: O(n) - linear time - grows with /n
# You loop once through the whole list (n elements).
# For each item, you're doing:
# A modulus check i % 2 → constant time
# A squaring operation i ** 2 → constant time
# So total = O(n) operations.

# Use slicing to grab every other item.
#start - stop - increment?

#shit, did i get that one too? i still don't know everything about slicing though....just knew enoough to get this
# every_other_num = nums[::2]
# print(every_other_num)

# 🔍 Big O: O(n) 0 Linear time -
# Technically O(n) because Python still has to build a new list, even if you're skipping items.
# You get half the elements, but still loop through the index range.
# Optimization: This is the cleanest way to do it, and it’s fast, concise, readable. So don't cry over the asymptotics here.

#more slicing drills--

# letters = ["a", "b", "c", "d", "e", "f", "g"]
# # 🔧 Expected Output: ['b', 'c', 'd']
# #looks like it wants index 123
# #start / stop (does not include what you want/increment)
# letters_3 = letters[1:4:1]
# print(letters_3)

#🧪 Big O: O(k), where k is the number of items in the slice. So in this case: O(3).
#so the Big O is still - linear - depends on how much you slice

# nums = [10, 20, 30, 40, 50, 60]
# # 🔧 Expected Output: [30, 40, 50]
# #start/stop/inc
# nums_3 = nums[2:5:1]
# print(nums_3)

#big O - O(k) - Linear for how much is sliced

# text = "spaceship"
# # 🔧 Expected Output: "ship"
# #start/stop/inc
# new_text = text[5:9:1]
# print(new_text)
# big O = O(k) - linear for how many slices

# emojis = ["😀", "😎", "🤖", "👽", "👾", "💀"]
# # 🔧 Expected Output: Every second emoji starting with the first one
# # ['😀', '🤖', '👾']
# #start/stop/inc
# new_emoji = emojis[0:5:2]
# print(new_emoji)

# big O = O(k) - linear k for how many slices

# grid = [
#     ["a", "b", "c", "d"],
#     ["e", "f", "g", "h"],
#     ["i", "j", "k", "l"],
#     ["m", "n", "o", "p"]
# ]

# #[['f', 'g'], ['j', 'k']]

# #this is wrong
# # mid_grid = grid[2[1:3:1],3[1:3:1]]
# mid_grid = [row[1:3] for row in grid[1:3]]
# print(mid_grid)

# 🔪 First Cut: grid[1:3]
# You’re saying: "Give me rows 1 and 2"
# That’s this chunk:

# 🧠 Then this part: row[1:3]
# Now, loop through those two rows, and in each one, give me columns 1 and 2.
# So:
# In ["e", "f", "g", "h"], you get ["f", "g"]
# In ["i", "j", "k", "l"], you get ["j", "k"]
# It’s like a surgeon delicately removing a section of cells from a spreadsheet while blindfolded.

# so the grid[1:3] slices the grid by start at row index 1 and stopping at 3 (2 not included)
# the looping of row[1:3] for row in grid..... means out of the grid slice get me start at index 1 and stop at index 3(not included) so it returns only the 2 
# so if it said grid[1:4] the return would even inlude ["n", "o"]??

# is row and grid in this reserved or just common practice to use those?
# can be replaced with foo and bar just like any other loop?


# ChatGPT said:
# Yes. 💯 Everything you just said is exactly correct—which is suspicious and terrifying, honestly. Are you sure you didn’t download a Python chip directly into your brain overnight?

# Let’s break down your questions:

# ✅ grid[1:3]
# You nailed it:

# Starts at row index 1: ["e", "f", "g", "h"]

# Stops at index 3 (exclusive), so you get up to index 2, which is: ["i", "j", "k", "l"]

# If you did grid[1:4], then yeah:

# [
#   ["e", "f", "g", "h"],  # index 1
#   ["i", "j", "k", "l"],  # index 2
#   ["m", "n", "o", "p"]   # index 3 ← this gets added
# ]
# And yes, that would include the row with "n" and "o".

# 🤖 row and grid – Reserved?
# Nope. Not reserved.

# grid is just the variable name you used for your 2D list.

# row is just the name you gave the loop variable. Could you write:
# [mid[1:3] for mid in grid[1:3]]
# Yes.

# [bar[1:3] for bar in foo[1:3]]
# Yes again.

# You can use pickle, gremlin, banana, anything your sad heart desires. These are just variables.

# But:

# Using readable names like row, col, grid is just convention.

# It makes your code readable, like it wasn’t written by a random internet raccoon with a keyboard.

# matrix = [
#     [11, 12, 13, 14, 15],
#     [21, 22, 23, 24, 25],
#     [31, 32, 33, 34, 35],
#     [41, 42, 43, 44, 45],
#     [51, 52, 53, 54, 55]
# ]

# matrix[1:4] → Grabbed rows 1, 2, 3
# row[1:4] → Grabbed columns 1, 2, 3 in each of those
# new_matrix = [row[1:4] for row in matrix[1:4]]
# print(new_matrix)


# 🔥 Big O Brain Bonus:
# This is still O(n) technically, where n is the number of rows you're iterating over. But since you're working with fixed-size sub-slices, it’s tight, efficient, and very readable. Which is the holy trinity of Pythonic elegance.


# 🟧 SETS
# what is a set?
# - unordered - no indexes
# - unchangeable - no terms of item positions
# - no duplicates allowed -
# - fast for membership(if it exists) checks....like is 'banana' in this set

# used when :
#     - remove duplicates -
#     - compare groups - 
#     - check membership(if it exists in group) -
#     - you don't care about order -

# “Membership” just means: "Is this thing in that group?"

# Like:
# Is a user in a list of banned users?
# Is a word in a sentence?
# Is a key in a dictionary?
# Is a letter in a word?
# Is your name in the cool kids set? (spoiler: not with that syntax error, it’s not.)

# items = ["apple", "banana", "apple", "cherry"]
# unique_items = set(items)
# print(unique_items)

# colors = {"red", "blue", "green"}
# print("red" in colors)
# print("yellow" in colors)

# a={"apple", "banana", "cherry"}
# b = {"banana", "cherry", "date"}
# #what do both have
# print(a & b)
# # print all unique values
# print(a | b)
# # what is different
# print(a - b)
# #does not work
# # print(a + b)

# # set() is a built in function - 
# # converts an iterable in to set
# # removes duplicates

# numbers = [1, 2, 2, 3, 4, 4, 5]
# #creates a set that removes the duplicates
# unique = set(numbers)
# print(unique)

# letters = set("banana")
# #prints letters in word only once ---- no duplicates
# print(letters)

# use set() when you have an existing thing
# use {} when you already know the elements

# nums = [1, 2, 2, 3, 4, 4, 5]
# # ❓ Use a set to print only the unique numbers in this list
# # ✅ Expected Output (order doesn't matter): 1 2 3 4 5
# single_nums = set(nums)
# print(single_nums)

# a = "developer"
# b = "clever"
# # ❓ Use sets to print the letters that appear in both words
# # ✅ Expected Output (order doesn't matter): e, l, v, etc.
# set_a = set(a)
# set_b = set(b)
# print(set_a & set_b)

# invited = {"Alice", "Bob", "Charlie", "Derek"}
# attended = {"Alice", "Charlie"}
# # ❓ Use a set operation to figure out who didn't attend
# # ✅ Expected Output: Bob, Derek
# did_not_show = (invited - attended)
# print(did_not_show)

# data = [1, 2, 2, 3, 4, 4, 5]
# # ❓ Convert this to a set to remove duplicates, then back to a list
# # ✅ Expected Output: A list of unique values: [1, 2, 3, 4, 5]
# data_set = set(data)
# print(data_set)

# #my silly way of brute -
# def new_i(x):
#     new_data = []
#     for i in x:
#         new_data.append(i)
#     return new_data

# print(new_i(data_set))

# unique_list = list(set(data))
# print(unique_list)

# 🟪 TUPLES
# like a list but ........
    #you can't modify(immutable)
    #you use () instead of []
    #still indexable/iterable
    #you often use them when you want data that shouldn't change
# coordinates = (5, 10)
# print(coordinates[0])

# person =("alice", 25)
# for item in person:
#     print(item)

# Given this list of tuples, print each person's name and age.
# people = [("Zoe", 19), ("Sam", 22), ("Alex", 30)]

# # 🔧 Expected Output:
# # Zoe is 19 years old.
# # Sam is 22 years old.
# # Alex is 30 years old.

# # Write a loop. Unpack the tuple. Print in a sentence.

# # Then write a version using enumerate() and print their number in the list too:
# # 1. Zoe is 19 years old.
# # 2. Sam is 22 years old.
# # ...

# for name, age in people:
#     print(f"{name} is {age} years old")

# for index, (name, age) in enumerate(people, start=1):
#     print(f"{index}. {name} is {age} years old.")

#enumerate(people) gives you both the index and the value
#start=1 is so list will start at 1
#(name, age) unpaackes the tuple inside the list
   
# scores = [
#     ("Maya", 88),
#     ("Liam", 94),
#     ("Zoe", 91),
#     ("Leo", 78),
#     ("Ava", 85)
# ]

# def student_scores(x):
#     for name, score in x:
#         #print(f"{name} scored {score} points.")
#         if score > 90:
#             print(f"{name} - {score}")
#             honor_roll = enumerate(scores)

# print(student_scores(scores))

# def student_scores(x):
#     print("All Scores:")
#     for name, score in x:
#         print(f"{name}, scored {score} points")
    
#     print("\nAbove 90:")
#     for name, score in x:
#         if score > 90:
#             print(f"{name} - {score}")

#     print("\nTop Performers:")
      #forgotten sorted syntax ....
#     sorted_scores = sorted(x, key=lambda i: i[1], reverse=True)
      # so for the enumaeration we loop and combine name and score
      # does that mean when we use enumerate it is automatticaly a loop?  
#     for j, (name, score) in enumerate(sorted_scores, 1):
#         print(f"{j}. {name} - {score}")
    
# student_scores(scores)

# scores = [
#     ("Noah", 82),
#     ("Olivia", 95),
#     ("Ethan", 88),
#     ("Emma", 91),
#     ("Mason", 79),
#     ("Ava", 97)
# ]
# #return a list from high to low - numbered

# def unpack_scores(x):
#     sorted_scores = sorted(x, key=lambda i: i[1], reverse=True)
#     for m, (name, score) in enumerate(sorted_scores, 1):
#         print(f"{m}. {name} - {score}")

# unpack_scores(scores)

# exam_data = [
#     ("Alice", 92, "Biology", "A"),
#     ("Bob", 78, "Math", "C"),
#     ("Zoe", 88, "History", "B"),
#     ("Leo", 95, "Physics", "A+"),
#     ("Maya", 83, "Chemistry", "B+"),
# ]


# for i, (name, score, subject, grade) in enumerate(exam_data, 1):
#     print(i, name, score, subject, grade)

# # drill 1 - 
# people = [("zoe", 88), ("liam", 95), ("Amy", 91)]
# #sort by score 
# sorted_people = sorted(people, key=lambda i: i[1], reverse=True)
# #need to list with enumerate
# for i, (name, score) in enumerate(sorted_people, 1):
#       print(f"{i}. {name} scored {score}")

# sorted_names = sorted(people, key=lambda j: j[0])
# for i, (name, score) in enumerate(sorted_names, 1):
#       print(f"{i}. {name} - {score}")

# books = [
#     ("Dune", 9.2),
#     ("1984", 9.5),
#     ("Foundation", 8.9),
#     ("Neuromancer", 9.0),
# ]

# sorted_books = sorted(books, key=lambda i: i[1], reverse=True)
# for i, (name, score) in enumerate(sorted_books, 1):
#       print(f"{i}. book: {name} - score: {score} ")

# students = [
#     ("Alice", 95, 300),
#     ("Bob", 92, 250),
#     ("Charlie", 95, 280),
#     ("Derek", 90, 310),
#     ("Eve", 95, 270)
# ]

# #-1[1] go backwords sorting / i[2] ascend by time
# sorted_score = sorted(students, key=lambda i: (-i[1], i[2]))
# # print(sorted_score)
# for i, (name, score, time) in enumerate(sorted_score, 1):
#       print(f"{i}, {name} - {score}")
      
# students = [
#     ("Alice", 92),
#     ("Bob", 85),
#     ("Charlie", 95),
#     ("Derek", 88),
#     ("Eve", 91),
# ]

# for name, score in students:
#       if score > 90:
#             print(name, score)

# high_scores = [(name, score) for name, score in students if score > 90]
# print(high_scores)

# runners = [
#     ("Zoe", 320),
#     ("Liam", 290),
#     ("Amy", 310),
#     ("Jake", 275),
#     ("Nina", 340),
#     ("Tom", 299)
# ]

# for name, time in runners:
#       if time < 300:
#             print(name, time)

# under_3 = [(name, time) for name, time in runners if time < 300]
# print(under_3)
# for name, time in under_3:
#       print(f"{name} ran the course in {time}")

# agents = [
#     ("Alice", "ShadowFox", 5),
#     ("Bob", "NightOwl", 2),
#     ("Charlie", "RedWolf", 4),
#     ("Derek", "GhostTiger", 3),
#     ("Eve", "SteelFalcon", 5),
# ]
# #filter agents with a clearance of level 4 or higher, return a list of their codenames
# #print in Codename authorized: [CODENAME]

# for name, code_name, level in agents:
#       if level >= 4:
#             print(f"Codename authorized: [{code_name}]")

# # or ----
# authorized_agents = [(name, code_name, level) for name, code_name, level in agents if level >= 4]
# for a, b, c in authorized_agents:
#       print(f"Codename authorized: [{b}]")

# # nums = [1, 1, 1, 2, 2, 3]
# # k = 2
# # ✅ Expected: [1, 2]
# nums = [4, 1, 1, 2, 2, 3, 3, 3]
# # k = 1
# # ✅ Expected: [3]

# #create a function
# def num_counter(x):
#       #empty dict to hold the count of each number found
#       num_counter = {}
#       #need to fill our dict....almost forgot to loop :P
#       for i in nums:
#             num_counter[i] = num_counter.get(i, 0) +1
#       #did not work lol
#       #sorted_num = sorted(num_counter, key=lambda i: -i[1])
#       print(sorted_num)
#       for num, count in num_counter.items():
            

# nums = [4, 1, 1, 2, 2, 3, 3, 3]
# # ✅ Expected Output: [3]

# # nums = [4, 1, 1, 2, 2, 3, 3]
# # # ✅ Expected Output: [1, 2, 3]

# # return a list of number/numbers that appear most frequently if there's a tie have them ascending
# #input will be int
# #will need to sort if they are worried about ascending

# #create a function
# def dupe_tracker(x):
#       #we could create a dict and track how many of each
#       num_count = {}
#       #we need to loop
#       for i in x:
#             #we would then havet sort our results
#             num_count[i] = num_count.get(i, 0) +1
#             #return our results
#       print(num_count)
#       for number, count in num_count.items():
#             counted_number = [number, count]
#             print(counted_number)
#             for count in range(len(counted_number), -2):
#                   print("this is the count", count)

# dupe_tracker(nums)

# words = ["apple", "banana", "apple", "orange", "banana", "apple"]

# # 🧠 Task: Count the words and print the one used most often.
# # ✅ Expected Output: "apple"

# #create a function
# def word_counter(x):
#       #create an empty dict to hold our word count
#       words_used = {}
#       #loop through and count our words
#       for i in x:
#             #count the words
#             words_used[i] = words_used.get(i, 0) +1
#       #print to see our dict
#       #print(words_used)
#       #unpack
#       for name, count in words_used.items():
#             #not sure if apple comes first because of count or name being apple will sort by count
#             words_used = sorted(count, key=lambda i: i[1], reverse=True)
#       print(words_used)

# word_counter(words)

# You are given a list of integers. 
# Return the k most frequent elements in descending frequency order. 
# If there’s a tie, return the smaller number first.

# expected output:
# [3, 1]
# 3 appears 3 times
# 1 and 2 both appear 2 times → pick 1 because it's smaller

# nums = [4, 1, 1, 2, 2, 3, 3, 3]
# k = 2

# #creating a function
# def num_counter(x, y):
#       #create a empty dict to hold our count
#       num_count = {}
#       #need to loop and count
#       for i in x:
#             #fill our dict
#             num_count[i] = num_count.get(i, 0) +1
#       #check our dict
#       #print(num_count)
#       #sort the dict by highest to lowest 
#       sorted_count = sorted(num_count.items(), key=lambda i: -i[1])
#       #check we are sorted
#       #print(sorted_count)
#       #need to return by k - i messed this part up will break it down and practice and keep learning
#       top_k = [num for num, count in sorted_count[:y]]
#       return top_k
# result = num_counter(nums, k)
# print(result)

      #so in the created top_k var 
      #sorted_count[:y] 
      # - slices the y item from the sorted_count list meaning the 3, the 1, 2, 4
      #if i were to use y=2, i would take the the first two most frequent, but we are using are passed in arg for the value
      #for num, count in ......
      #each element in sorted_count is a tuple....this merley unpacks the tuple
      #[num for.......]
      #you're created a new list containg just the num part of each [num, count] pair
      #not keeping the counts. just the top k- numbers

# Given an array of integers, 
# return True if the number of occurrences of each value is unique. 
# Otherwise, return False.

# unique_occurrences([1, 2, 2, 1, 1, 3])
# # ✅ Output: True
# # Explanation: 1 occurs 3 times, 2 occurs 2 times, 3 occurs 1 time → [3,2,1] → unique

# unique_occurrences([1, 2])
# # ✅ Output: False
# # Explanation: 1 occurs 1 time, 2 occurs 1 time → [1,1] → not unique

# unique_occurences = ([1, 3, 4, 2, 1, 3, 3, 4, 4, 4])
# unique_occurences_1 = ([1, 2, 3, 4, 5, 6, 6, 7])

# #need to create a function
# def unique_or_not(x):
#       #need to create an empty dict to hold our count
#       num_tracker = {}
#       #need to loop
#       for i in x:
#             #need to fill our dict while looping
#             num_tracker[i] = num_tracker.get(i, 0) +1
#       #print to check our dict
#       #print(num_tracker)
#       #need to sort the dict by using sorted(dict.items())
#       sorted_by_count = sorted(num_tracker.items(), key=lambda i: i[1])
#       #print and check our sorted list - 
#       # print(sorted_by_count)
#       #do some kind of logic check/conditional if duplicates in values = return false if no dupes = return true
#       # for num, count in sorted_by_count:
#       #       if count[0] == count[1]:
#       #             return False
#       #       else:
#       #             return True
#       #get all the counts and check if their lengths match
#       #looks like we create a new var - built in list function and we use just our values from our dict hench the .values()
#       values = list(num_tracker.values())
#       #here we check the len of values and the leng of set values? will return a true or false
#       return len(values) == len(set(values))

# print(unique_or_not(unique_occurences))
# print(unique_or_not(unique_occurences_1))

#-------------    brain burn in for built in functions    ------
# list() = converts anything in to a list, list() = converts anything in to a list
# list() = converts anything in to a list, list() = converts anything in to a list
# list() = converts anything in to a list, list() = converts anything in to a list
# list() = converts anything in to a list, list() = converts anything in to a list
# list() = converts anything in to a list, list() = converts anything in to a list

# set() = removes duplicates and makes un-ordered unique collection
# set() = removes duplicates and makes un-ordered unique collection
# set() = removes duplicates and makes un-ordered unique collection
# set() = removes duplicates and makes un-ordered unique collection
# set() = removes duplicates and makes un-ordered unique collection

# sorted() = returns a sorted version, sorted() = returns a sorted version
# sorted() = returns a sorted version, sorted() = returns a sorted version
# sorted() = returns a sorted version, sorted() = returns a sorted version
# sorted() = returns a sorted version, sorted() = returns a sorted version
# sorted() = returns a sorted version, sorted() = returns a sorted version

# dict() = builds a dict - have not used yet
# dict() = builds a dict - have not used yet
# dict() = builds a dict - have not used yet
# dict() = builds a dict - have not used yet
# dict() = build a dict - have not used yet

# str()/int() type conversion - str()/int() type conversion
# str()/int() type conversion - str()/int() type conversion
# str()/int() type conversion - str()/int() type conversion
# str()/int() type conversion - str()/int() type conversion
# str()/int() type conversion - str()/int() type conversion

# list() ----------------------
# range(5)          ➡️  list(range(5))  ➡️  [0, 1, 2, 3, 4]
# dict.keys()       ➡️  list(dict.keys())  ➡️  ["key1", "key2"]
# set("hello")      ➡️  list(set("hello"))  ➡️  ['h', 'e', 'l', 'o']


# set() ---------------------
# set_a & set_b  # intersection
# set_a | set_b  # union
# set_a - set_b  # difference

# if x in some_set:  # way faster than in a list

# sorted() --------------------
# sorted(x)           # returns a new list, original is untouched
# sorted(x, reverse=True)  # descending
# ✅ You can sort tuples and dict .items() by value with key= tricks.

# dict()----------------------------
# dict([("a", 1), ("b", 2)])  # {'a': 1, 'b': 2}
# tracker = {}
# tracker[key] = tracker.get(key, 0) + 1

# str()/int()---------------------------------
# str(42)     # "42"
# int("42")   # 42
# But int("4.5") will explode 🔥 because it’s not a clean int.

# logs = [
#     ("Alice", "upload"),
#     ("Bob", "comment"),
#     ("Alice", "upload"),
#     ("Bob", "upload"),
#     ("Charlie", "like"),
#     ("Alice", "upload"),
#     ("Charlie", "upload"),
#     ("Alice", "comment"),
#     ("Charlie", "upload"),
#     ("Charlie", "make Chocolate"),
# ]
# # 🧠 Your Mission:
# # Count how many total actions each user performed.
# # Output: {"Alice": 4, "Bob": 2, "Charlie": 2}
# # Find the user(s) with the most actions.
# # Output: ["Alice"]
# # If there's a tie, return all users who tied.
# # (e.g., if Bob and Charlie both had 4 actions)
# # 🚫 Rules:
# # No collections.Counter
# # Yes to .get() and .items()
# # Try to write it in a function
# # Bonus: Print the top user(s) in a friendly way:
# # "Most active user(s): Alice"

# #create a function
# def user_actions(x):
#       #create a dict to count name / actions
#       action_count = {}
#       #loop
#       #had to put name, action in x if i just had name it would separate each action - good to know
#       for name, action in x:
#             #fill our dict
#             action_count[name] = action_count.get(name, 0) +1
#       #print(action_count)
#       #sort our dict info as tuples
#       # user_action_count = sorted(action_count.items(), key=lambda i: -i[1])
#       #return our new sorted info
#       return action_count

# def most_active_users(y):
#       #step 1 - get max action count - max(dict.values())
#       most_actions = max(y.values())
#       # step 2: collect everyone who has that count
#       top_users = []
#       for user, count in y.items():
#             if count == most_actions:
#                   top_users.append(user)
            

#       #top_users = [user for user, count in y.items() if count == most_actions]
#       return top_users

# action_count = user_actions(logs)
# winners = most_active_users(action_count)
# print(f"Most active user(s):", ", ".join(winners))
      
#top_users = [user for user, count in y.items() if count == most_actions]
#means loop through y.items() - the .items() gives user/count as tuples - for each pair only grab user if their count == most_actions
#it's list comprehension but a loop in disguise 

# votes = [
#     ("Alice", "banana"),
#     ("Bob", "apple"),
#     ("Alice", "banana"),
#     ("Charlie", "banana"),
#     ("Alice", "apple"),
#     ("Bob", "banana"),
#     ("Charlie", "apple"),
#     ("Charlie", "banana"),
# ]

# def fruit_count(x):
#       fruit_votes = {}
#       for name, fruit in x:
#             fruit_votes[fruit] = fruit_votes.get(fruit, 0) + 1
#       return fruit_votes

# counted_votes = fruit_count(votes)
# #print(counted_votes)
# def vote_results(y):
#       for name and count in y.items():
#             top_voted = max(y.values(), count[0])
#       return top_voted

# top_fruit = vote_results(counted_votes)
# print(f"Top fruit: {fruit}")

# word = "abracadabra"
# # Count how many times each letter appears.
# # ✅ Expected: {'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1}

# letter_count = {}

# for letter in word:
#       letter_count[letter] = letter_count.get(letter, 0) +1
# print(letter_count)

# scores = [("Alice", 88), ("Bob", 94), ("Zoe", 91)]
# # Print the name of the person with the highest score.
# # ✅ Expected: Bob
# #all we needed to do was take scores - use built in max - and then print top[0]
# top = max(scores, key=lambda x:x[1])
# print(top[0])

# nums = [1, 2, 2, 3, 4, 4, 5]
# # Convert to a list of unique values (any order is fine).
# # ✅ Expected: [1, 2, 3, 4, 5]
# removed_dupes = set(nums)
# print(removed_dupes)
# #if we want to make it a list as well
# print(list(set(nums)))

# letters = ["a", "b", "c", "d", "e", "f", "g"]
# # Grab the middle 3 letters.
# # ✅ Expected: ['c', 'd', 'e']
# new_letters = letters[2:5]
# print(new_letters)

# students = [("Amy", 92), ("Liam", 85), ("Zoe", 95)]
# # Sort by score, descending.
# # ✅ Expected: Zoe, Amy, Liam
# sorted_students = sorted(students, key=lambda i: -i[1])
# for name, score in sorted_students:
#       print(name)

# nums = [1, 2, 2, 3, 4, 4, 5]
# # 👉 Expected: [1, 2, 3, 4, 5] (order doesn't matter)
# unique = list(set(nums))
# print(unique)

# word = "abracadabra"
# # 👉 Expected: {'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1}
# letter_count = {}
# for char in word:
#     letter_count[char] = letter_count.get(char, 0) +1
# print(letter_count)

# students = [("Amy", 92), ("Liam", 85), ("Zoe", 95)]
# # 👉 Expected: ("Zoe", 95)
# top_student = sorted(students, key=lambda i:-i[1])
# print(top_student[0])

# scores = [("Alice", 88), ("Bob", 94), ("Zoe", 91)]
# # 👉 Expected: Bob, Zoe, Alice
# sorted_scores = sorted(scores, key=lambda i: -i[1])
# print(sorted_scores)

# letters = ["a", "b", "c", "d", "e", "f", "g"]
# # 👉 Expected: ['c', 'd', 'e']
# middle = letters[2:5]
# print(middle)

# logs = [
#     ("Alice", "upload"),
#     ("Bob", "comment"),
#     ("Alice", "upload"),
#     ("Bob", "upload"),
#     ("Charlie", "like"),
#     ("Alice", "upload"),
#     ("Charlie", "upload"),
#     ("Alice", "comment"),
#     ("Charlie", "upload"),
#     ("Charlie", "upload"),
# ]

# # #create a function
# # def log_tracker(x):
# #       #create an empty dict
# #       user_action = {}
# #       #then we need to loop
# #       for name, action in x:
# #             #need to populate our dict
# #             user_action[name] = user_action.get(name, 0) +1
# #             #return our dict
# #       return user_action

# # action_count = log_tracker(logs)

# # def most_used(action_count):
# #       most = max(action_count.values())
# #       top_users = [user for user, count in action_count.items() if count == most]
# #       return top_users

# # winners = most_used(action_count)
# # print("most acitve user(s):", ", ".join(winners))

# counts = {'Alice': 4, 'Bob': 2, 'Charlie': 5, 'Derek': 5}

# # Your job:
# # 1. Get the highest value
# # 2. Return all names with that value

# def top_performers(d):
#     top_users = max(counts.values())
#     winners = [name for name, count in d.items() if count == top_users]
#     return winners

# print(top_performers(counts))  # ✅ Should return ['Charlie', 'Derek']

# words = ["apple", "banana", "apple", "orange", "banana", "apple"]

# # Step 1: Count occurrences
# count = {}
# for word in words:
#     count[word] = count.get(word, 0) + 1

# # Step 2: Find the most common
# top_count = max(count.values())
# most_common = [w for w, c in count.items() if c == top_count]
# print("Most common:", most_common)

# votes = ["Alice", "Bob", "Alice", "Derek", "Alice", "Bob", "Derek", "Derek", "Bob", "Alice"]

# vote_count = {} 
# for name in votes:
#       vote_count[name] = vote_count.get(name, 0) +1

# top_votes = max(vote_count.values())
# most_votes = [name for name, count in vote_count.items() if count == top_votes]
# print(most_votes)

# nums = [4, 1, 2, 1, 2]
# # ✅ Expected Output: 4
# #write a function called find_single(nums)
# def find_single(nums):
#       num_count = {}
#       for i in nums:
#             num_count[i] = num_count.get(i, 0) +1
#       for num, count in num_count.items():
#             if count == 1:
#                   return num
# print(find_single(nums))

# ❓ Prompt:
# Given a string, return the index of the first character that is unique (appears only once).
# If there is no unique character, return -1.

# ✅ Example:
# Input: "leetcode"
# Output: 0  (because 'l' is the first unique character)

# Input: "loveleetcode"
# Output: 2  (because 'v' is the first unique character)

# Input: "aabb"
# Output: -1

# def first_unique(s):
#     char_count = {}
#     for char in s:
#         char_count[char] = char_count.get(char, 0) + 1

#     for idx, char in enumerate(s):
#         if char_count[char] == 1:
#             return idx
#     return -1

# nums1 = [1, 2, 2, 1]
# nums2 = [2, 2]

#return a list of unique elements 

# def in_both(x, y):
#       set1 = set(x)
#       set2 = set(y)
#       return list(set1 & set2)

# print(in_both(nums1, nums2))
# # Given a list of integers, return True if any value appears at least twice.

# nums1 = [1, 2, 3, 4]        # Expected: False
# nums2 = [1, 2, 3, 1]        # Expected: True

# def has_duplicates(nums):
#     # Your magic goes here
#     for digit in nums:
#       if digit[0] == digit[1]:
#             return true
      

votes = ["Alice", "Bob", "Alice", "Derek", "Alice", "Bob", "Derek", "Derek", "Bob", "Alice"]

# ✅ Expected: "Alice"
vote_count = {} 
for name in votes:
      vote_count[name] = vote_count.get(name, 0) +1
top_votes = max(vote_count.items(), key=lambda i: -i[1])
winner = [name for name, votes in vote_count.items() == top_votes]

print(winner)
