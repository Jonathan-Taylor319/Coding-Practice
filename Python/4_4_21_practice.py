# trying to put together muscle memory of ----
        # 🔁 range(), len(), loop logic ✅ Then we’ll hit:

        # 📦 Dictionary basics

        # 🧵 List comprehension

        # 🔪 Slicing & indexing

#have been hammering syntax and basics.... will try to fully cement in to memory and then apply to coding challenges

# --------starting with loop and range drill - 
    #start with triples - groups of 3 - will help range(), len() / and indexing

# nums = [4, 7, 9, 2, 5, 8, 1]

#write a loop that:
    # iterated over the list
    # extracts and prints triples
    # adds a comment on why the loop stops and where it does
    # bonus : check to see if the middle value is the largest of the three


# loop - range(len(num)) means we will loop through the length of the whole list
# our -2 means when looping, leave room for 2 more values when interating
# for i in range(len(nums) -2):
#     #-----can be print either way for however we want to use data
#     #print our num's i values:
#     print([nums[i], nums[i+1], nums[i+2]])
#     #i want to see if i can print like this and not another list:
#     print(nums[i], nums[i+1], nums[i+2])
#     #going to add this in to see if i can make one number?
#     print(nums[i] + nums[i +1] + nums[i+2]) # this will sum the numbers
#     #bonus attempt - check to see if middle number is highest value
#     a = nums[i]
#     b = nums[i+1]
#     c = nums[i+2]
#     if b > c and b > a:
#         print(f"{b} is the king of the castle! woo wow wee wow!")
#     else:
#         print(f"{b} needs to eat more veggies and grow up!")


# possible_kings = [3, 7, 9, 1, 5, 3, 0, 1, 6, 3, 5, 6]
# #declare a function
# def triple_kings(x):
#     #need to create a var to track the kings
#     #this needed to before initial loop but also inside function
#     king_count = 0
#     #loop through the list in triples
#     # for the length of the input keep track of 3 values
#     # i initially wrote i backwards like a dummy
#     for stuff in range(len(x) - 2):
#         #need to create 3 vars to compare:
#         a = x[stuff]
#         b = x[stuff + 1]
#         c = x[stuff + 2]
#         #a king is if the middle var is the biggest  so.....
#         if b > a and b > c:
#             king_count += 1
#     return king_count

# (f"We found {king_count} in this list of danger")

# print(triple_kings(possible_kings))

# def triple_kings(x):
#     king_count = 0
#     for i in range(len(x) - 2):
#         a = x[i]
#         b = x[i + 1]
#         c = x[i + 2]
#         if b > a and b > c:
#             king_count += 1
#     return king_count

#-------loop logic drill ---- 
    #givin a list of integers
    #check each group of 4
    #print something if their sum is evenly divisibly by 4 ( x % 4) i think
        #if the sum is divisible by 4, print:
            #"Balanced group found at index X: [a, b, c, d]"
            #x is the index and the list is the group itself

# data = [5, 3, 6, 3, 2, 1, 7, 4, 4, 8, 0, 2, 2]

# #lets define a function
# def check_4(muffins):
#     #create a loop that can check groups of four.....3 off the end
#     for berry in range(len(muffins) -3):
#         #break it down and see what we get:
#         # print("this is the berry print :", (berry)) # = index
#         # print("this is the muffins[berry] print :", (muffins[berry])) # = value
#         #looked at previous code was stuck for awhile trying to pull mutiple at once .....may need to create 4 vars to hold and then sum them up and then check %4 == 0
#         a = muffins[berry]
#         b = muffins[berry + 1]
#         c = muffins[berry + 2]
#         d = muffins[berry + 3]
#         total_berry = a + b + c + d
#         # print(total_berry)
#         if total_berry % 4 == 0:
#             print(f"balanced group found at index {berry}: {a} {b} {c} {d}")
        
# check_4(data)

# given alist of binary values: 0 and 1
# the list represents a motion sensor log

# 1 = movement

# 0 = no movement

# identify if there are three 1's in a row

# if  there are three in a row print"Intrusion detected at index X

# only if 3, no more, no less

# log = [0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0]

# #define our function
# def loop_drill(m):
#     #we want to check if it's only 3 in a row...meaning we need a group of 4 
#     for i in range(len(m) - 3):
#         #need to hold the 4 values as a group, but first grab them
#         a = m[i]
#         b = m[i + 1]
#         c = m[i + 2]
#         d = m[i + 3]
#         move_set = [a, b, c, d]
#         #new counter to track if we go over
#         total_moves = 0
#         #checking to see if groupped propperly it
#         # print(move_set)
#         #need to see if only 3 i's in a row...i can't blindly count...
#         #loop through new list - not sure if needed trying to think as i go
#         #may add a counter and make conditionals?
#         # for j in move_set:
#         #     if total_moves == 4:
#         #         break
#         #     elif move_set[j] == 0:
#         #what if i just make a conditional statement?
#             #did not work
#         # if move_set == [1, 1, 1, 0] or [0, 1, 1, 1]:
#         #     print(f"Intrusion detected at index {i}")
#         for j in move_set:
#             # print(j)
#             if total_moves == 4:
#                 break
#             elif total_moves == 3:
#                 print("Intrusion detected at index ", i)
#             elif j == 1:
#                 total_moves += 1
#             elif j == 0:
#                 total_moves = 0

# loop_drill(log)


# -----------------back to dictionaries-----------------
# a dict in python is like a locker
#     -put stuff in usina label(key)
#     -you retrieve it using the label
#     -and if you lose the key you'r locked out forever

# example of a basic dictionary
# book = {"title": "Dune", "author": "Frank Herbert"}
# print(book["title"]) prints just the title
# print(book) - prints the whole dict


#-------MUST-KNOW Methods-----------
#1
#.get(key, default)
#returns the value for key, or the default if it doesn't exist

# .get does not
#     create new keys
#     mutuate the dictionary

# it only prevents errors if the key does not exist

# inventory = {"sword":2} 
# print(inventory.get("shield", 0)) #returns 0 instead of crashing
# print(inventory.get("hammer", 1))
# # print(inventory)

# 2
# .items()
# returns all key - value pairs as tuples(jump in to tuples below) great for looping
#     for item, count in inventory.items():
#     print(item, count)

# 3
# .keys() and .values ()
# .keys() = all keys
# .values() = all values
# (Useful for checking existence, sorting, etc.)

#-------TUPLE------
#a tuple is an immutable sequence in python, like a list but it can't be changed

# my_tuple = (1,2,3)
# ✅ Ordered

# ✅ Indexable

# ✅ Iterable

# ❌ Cannot add/remove/change elements

# ---- tuples can be any size and even empty

# return multiple values from a function
#     the default return type when you return more than one thing

#     def get_name():
#     return ("Ada", "Lovelace")

#     first, last = get_name()

#     dictionary .items() gives tuples

#     d = {"a": 1, "b": 2}
#     for key, value in d.items():
#         print((key, value))  # ('a', 1), ('b', 2)

#     immutability = saftey
#         - you want a collectection of values to stay fixed
#         - you're using the data as a dictionary key

#         coords = (5, 9)
#         positions[coords] = "enemy spotted"

#         ✋ How Are They Different From Lists?
# Feature	List ([])	Tuple (())
# Mutable?	✅ Yes	❌ No
# Indexable?	✅ Yes	✅ Yes
# Iterable?	✅ Yes	✅ Yes
# Can change?	✅ Yes	❌ Locked forever
# Good for?	Changing data	||    Fixed, safe data
# Used in?	Loops, stacking	||    Coordinates, returns

# first dictionary drill ---

# write a function called count_names(lst)
#     it should take a list of names as strings
#     return a  dict
#         each unique name as a key
#         how many times it appears as a value

# names = ["Ada", "Bob", "Ada", "Eve", "Bob", "Ada", "Carl"]


# # 🧠 Required:
# # Use .get() to avoid KeyError tantrums

# # No if name in dict: checking

# # No collections.Counter cheat codes

# # Keep it caveman-level logic

# name_thing = {}
# def count_names(lst):
#     for i in names:
#         name_thing[i] = name_thing.get(i, 0) + 1
#     return name_thing

# print(count_names(names))


#-------practice drill 2-------

# votes = ["Alice", "Bob", "Alice", "Derek", "Bob", "Alice", "Alice", "Derek"]

# # created a function that is a list of votes / each vote is a name / count votes for candidates/ use .get()
# vote_count = {}

# def count_votes(votes):
#     for h in votes:
#         vote_count[h] = vote_count.get(h, 0) + 1
#     return vote_count
    
# print(count_votes(votes))
