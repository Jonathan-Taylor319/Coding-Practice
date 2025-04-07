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

# 🧪 CHALLENGE: balance_check()
# 🔢 Input:
# data = [5, 3, 6, 2, 1, 7, 4, 4, 8, 0, 2, 2]
# ✅ Expected Output:
# Balanced group found at index 0: [5, 3, 6, 2]
# Balanced group found at index 4: [1, 7, 4, 4]
# Balanced group found at index 7: [4, 4, 8, 0]
# You figure out:

# A balanced group is a group of integers whose sum is evenly divisible by 4.

# How many numbers to group

# What check to perform

# What data structure or access method to use
# data = [5, 3, 6, 2, 1, 7, 4, 4, 8, 0, 2, 2]


# #define a function
# def b_4(mayo):
#     #loop through the length of the data but make groups of 4
#     for i in range(len(mayo) - 3):
#         #forgot to add vars to hold each var and the combine to make a set
#         a = mayo[i]
#         b = mayo[i + 1]
#         c = mayo[i + 2]
#         d = mayo[i + 3]
#         e = (a, b, c, d)
#         # print(a)
#         # print(e)
#         #once we loop through need to see if the group of 4 is moduls 0 by 4
#         if (a + b + c + d) % 4 == 0:
#         # #create a print statemunt or return stating the index and the group-
#             print (f"Balanced group found at index {i}: {e}")

# b_4(data)

# 🧪 DRILL: steady_rise()
# 🔢 Input:
nums = [1, 2, 3, 2, 4, 5, 1, 2, 3, 5, 6]
# ✅ Expected Output:
# Rising sequence found at index 0: (1, 2, 3)
# Rising sequence found at index 4: (4, 5, 1)
# Rising sequence found at index 7: (2, 3, 5)
# You figure out:

# What “rising” means

# How many numbers to group

# What to compare

# When to print

# You’re warmed up.
# Now go loop and conquer.

# def up_or_not(something):
#     for i in range(len(something) - 2):
#         a, b, c = something[i], something[i+1], something[i+2]
#         if a < b and b < c:
#             print(f"Rising sequence found at index {i}: ({a}, {b}, {c})")


# up_or_not(nums)

#----------back to get practice ----------

# genres = [
#     "sci-fi", "fantasy", "sci-fi", "romance", "fantasy",
#     "fantasy", "sci-fi", "non-fiction", "romance", "romance",
#     "sci-fi", "non-fiction"
# ]

# # 🔧 Your Task:
# # Build a function count_genres(lst)

# # Use .get() to count genre frequency

# # No if in dict allowed

# # No sorting, no list comprehension, no cheating

# #define a function
# def genre_counter(i):
#     #declare a dict
#     genre_count = {}
#     #loop through the input
#     for b in i:
#         #count the genre and increment inside our dict
#         genre_count[b] = genre_count.get(b, 0) + 1
#     #print or return the count
#     return genre_count

# print(genre_counter(genres))

# records = [
#     ("Alice", "math"),
#     ("Bob", "history"),
#     ("Alice", "science"),
#     ("Derek", "math"),
#     ("Alice", "math"),
#     ("Bob", "science"),
#     ("Eve", "history"),
#     ("Alice", "history"),
#     ("Derek", "science"),
#     ("Eve", "math"),
#     ("Eve", "science"),
#     ("Bob", "math")
# ]

# #create a function
# def student_tracker(i):
#     student_sched = {}
#     #loop through input and unpack tuple-----omg that is nice
#     for a, b in i:
#         #confirm it is unpacked --- it is...need to go back, create empty dict and get ready for nesting of the nested >.<
#         #print(a, b)
#         #need to create our student name with an empty dict and then go in to it and populate.....
#         student_sched[a] = student_sched.get(a, {})
#         student_class[b] = student_class.get(b, 0) + 1
#     return student_sched


# student_tracker(records)

#======favorite drinks=========
# drinks = [
#     ("Alice", "tea"),
#     ("Bob", "coffee"),
#     ("Alice", "coffee"),
#     ("Alice", "tea"),
#     ("Bob", "tea"),
#     ("Derek", "juice")
# ]

# def track_drinks(data):
#     drink_log = {}

#     for person, drink in data:
#         inner = drink_log.get(person, {})
#         inner[drink] = inner.get(drink, 0) + 1
#         drink_log[person] = inner 
    
#     return drink_log

# print(track_drinks(drinks))

# def track_drinks(data):
#     drink_log = {} 

#     for person, drink in data:
#         inner = drink_log.get(person, {})
#         inner[drink] = inner.get(drink, 0) + 1
#         drink_log[person] = inner
#     return drink_log
# print(track_drinks(drinks))

# def drink_tracker(hat):
#     person_drink = {}
#     for cap, bill in hat:
#         holder = person_drink.get(cap, {})
#         holder[bill] = holder.get(bill, 0) + 1
#         person_drink[cap] = holder
#     return person_drink
# print(drink_tracker(drinks))

#define the function
    #make an empty dict
    #unpack and loop
        #holder to declare an empty dict assinged to our key
        #holder[nested item we want] = holder.get[what we want to increment, 0] + 1
        #our dict[key] = [nested items]
    #return nested items
#printfunction(input))

#def my_nested_counter(data):
    #create an empty dictionary to hold results
    #result = {}

    #loop an empty dictionary to hold results
    #for key, nested_key in data:

        #holder: inner dictionary, defaults to {}
        #holder = result.get(key, {})

        #update the inner value using .ger()
        #holder[nested_key] = holder.get(nested_key, 0) + 1

        #assigned to the updated inner dict back to the outer key
        #result[key] = holder

    #Return the final nested dict
    #return result

# drinks = [
#     ("Alice", "tea"),
#     ("Bob", "coffee"),
#     ("Alice", "coffee"),
#     ("Alice", "tea"),
#     ("Bob", "tea"),
#     ("Derek", "juice")
# ]

# def drink_things(ummm):
#     yerp = {}
#     for a, b in ummm:
#         c = yerp.get(a, {})
#         c[b] = c.get(b, 0) + 1
#         yerp[a] = c
#     return yerp

# print(drink_things(drinks))

# #declare a function
# def track_drinks(i):
#     #create an empty dict
#     total_drinks = {}
#     #unpack and loop through the list
#     for name, drank in i:
#         #this is where we get funky / we need to make something to hold our drinks inside our key....
#         #random var = our dict.get(key, {actual holder})
#         hold_on = total_drinks.get(name, {})
#         #now we need to pass in our drinks like a flat dict to the empty
#         hold_on[drank] = hold_on.get(drank, 0) + 1
#         #now we throw our stuff inside the actual dict like normal/flat? no....by just bringing the 2 together as the value of our key'd dict
#         total_drinks[name] = hold_on
#     #return our dict
#     return total_drinks

# print(track_drinks(drinks))

# pet_data = [
#     ("Alice", "cat"),
#     ("Bob", "dog"),
#     ("Alice", "dog"),
#     ("Derek", "fish"),
#     ("Alice", "cat"),
#     ("Bob", "dog"),
#     ("Eve", "cat"),
#     ("Derek", "cat"),
#     ("Eve", "dog"),
#     ("Bob", "fish"),
# ]

# # 📋 Your Mission:
# # Define a function: track_pets(data)
# # Use two .get() calls (one nested)
# # Do not use if key in dict anywhere
# # No fancy libs, no defaultdict, just you and your loops

# #define a function
# def pet_tracker(i):
#     #created a empyt dict
#     owner_pet_list ={}
#     #unpack my tuple and loop
#     for owner, pet in i:
#         #create a holder that will sit in an empty dict
#         pet_list = owner_pet_list.get(owner, {})
#         #fill the holder like a normal dict using nested data
#         pet_list[pet] = pet_list.get(pet, 0) + 1
#         #call upon the orig dict with our key and then have it = the holder
#         owner_pet_list[owner] = pet_list
#     #return our dict
#     return owner_pet_list

# print(pet_tracker(pet_data))

# watch_data = [
#     ("Alice", "Inception"),
#     ("Bob", "The Matrix"),
#     ("Alice", "Inception"),
#     ("Derek", "Interstellar"),
#     ("Alice", "The Matrix"),
#     ("Bob", "Inception"),
#     ("Eve", "The Matrix"),
#     ("Derek", "Inception"),
#     ("Eve", "Inception"),
#     ("Bob", "The Matrix"),
# ]

# # 📋 Your Mission:
# # track_movies(data)
# # Two .get() calls — one outer, one inner
# # No if key in dict
# # Correctly re-assign the nested dict back into the outer one (DO NOT TACO BELL THIS TIME)

# #define a function
# def watched_movies(i):
#     #declare an empty dict
#     movie_dict = {}
#     #unpack my tuple and loop
#     for name, movie in i:
#         #create a var to hold my empty dict
#         movie_holder = movie_dict.get(name, {})
#         #fill the empty dict with get
#         movie_holder[movie] = movie_holder.get(movie, 0) + 1
#         #pull in the holder to my keyed dict
#         movie_dict[name] = movie_holder
#     #return the stuff
#     return movie_dict

# print(watched_movies(watch_data))

    # in a dict .items() gives you
    #     (key, value) pairs

    # so:
    
    # my_dict = {'a': 1, 'b':2}
    # for k, v in my_dict.items():
    #     print(k, v)

    # output = a 1
    # #          b 2

    # movie_data = {
    #     'alice': {'Inception': 2, 'The Matrix': 1},
    #     'Bob': {'The Matrix': 2, 'Inception': 1}
    # }

    # using .items() twice lets me .....

    # #for key/ value in dict
    # for person, movies in movie_data.items():
    #     #for value and value inside dict
    #     for movie, count in movies.items():
    #         #give me the key / value /value?
    #         print(person, movie, count)
# test_data = {
#     "Amy" : {"apple": 2, "banana": 1},
#     "Tom" : {"banana": 3, "pear": 1},
#     }

# for name, fruits in test_data.items():
#     for fruit, qty, in fruits.items():
#         print(f"{name} has {qty} {fruit}(s)")

# movie_data = {
#     'Alice': {'Inception': 2, 'The Matrix': 1},
#     'Bob': {'The Matrix': 2, 'Inception': 1}
# }

# for person, movies in movie_data.items():
#     for movie, count in movies.items():
#         print(person, movie, count)

# #loop key, first value in dict.item():
#     #loop first value, second value in 1st value.items()
#         #print(all values we pulled)

# 💪 WHAT YOU MUST DO:
# Build a nested dict
# Format: {user: {action: count}}
# Return the nested dict from a function
# No print inside that function. Return only.
# Write another function to take the nested dict and print a clean summary line-by-line

# logs = [
#     ("Alice", "email"),
#     ("Bob", "login"),
#     ("Alice", "login"),
#     ("Derek", "email"),
#     ("Alice", "upload"),
#     ("Bob", "email"),
#     ("Derek", "login"),
#     ("Alice", "login"),
#     ("Eve", "upload")
# ]

# #def a function
# def webpage_log(i):
#     #create and empty dict
#     user_logs = {}
#     #loop through the dict with a key value pair to unpack the tuple
#     for name, action in i:
#         #use a holder var with the key and the dict.get(key {}) to create the empty inner dict
#         logged = user_logs.get(name, {})
#         #populate our inner var[value] = var.get(value, 0)+1
#         logged[action] = logged.get(action, 0) + 1
#         #use ourdict[key] = holder var
#         user_logs[name] = logged
#     #return dict
#     return user_logs

# # print(webpage_log(logs))
# #create a var from these results
# user_actions = webpage_log(logs)

# def print_actions(o):
#     for name, actions in o.items():
#         for action, num in actions.items():
#             print(name, action, num)
#             if "login" in action and num > 1:
#                 print(f"{name} has logged in more than once....she may be hacked")

# print_actions(user_actions)

# 🎯 Your Goals (unchanged):
# Build a nested dict:
# {player: {game: count}}
# Return that dict from one function
# Use a second function to print line-by-line:
# BONUS: If they play a game 3+ times:
# Whoa Alice really loves Final Fantasy!

# game_logs = [
#     ("Alice", "Final Fantasy"),
#     ("Bob", "World of Warcraft"),
#     ("Alice", "Aion"),
#     ("Derek", "Final Fantasy"),
#     ("Bob", "Aion"),
#     ("Eve", "World of Warcraft"),
#     ("Alice", "Final Fantasy"),
#     ("Bob", "Final Fantasy"),
#     ("Derek", "Aion"),
#     ("Alice", "Final Fantasy"),
#     ("Bob", "World of Warcraft"),
#     ("Alice", "Aion"),
# ]

# #create a function
# def game_tracker(i):
#     #create an empty dict
#     player_log = {}
#     #loop through the dict and unpack tuple
#     for player, game in i:
#         #declare a holder for inner dict, game_logs(key, {})
#         how_many_times = player_log.get(player, {})
#         #holder[value] = holder.get(value, 0 ) + 1
#         how_many_times[game] = how_many_times.get(game, 0) + 1
#         #dict[key] = holder
#         player_log[player] = how_many_times
#     #return our dict
#     return player_log

# #check our 1st function
# #print(game_tracker(game_logs)) - works

# #create var to hold our return 
# tracked_dict = game_tracker(game_logs)
# print(tracked_dict)

# #define a new function
# def game_count(i):
#     #key, 1st val in var.item():
#     for name, games in i.items():
#         #1st val, 2nd val in 1st.item():
#         for game, count in games.items():
#             #print results
#             print(name, game, count)
#         #bonus if game is played more than 3 times interpolate that {player} really loves {game}
#             if count >= 3:
#                 print(f"Woah {name} really loves {game}")

# game_count(tracked_dict)

# tame_logs = [
#     ("Alice", "Slime"),
#     ("Bob", "Dragon"),
#     ("Alice", "Slime"),
#     ("Derek", "Goblin"),
#     ("Alice", "Dragon"),
#     ("Bob", "Slime"),
#     ("Derek", "Slime"),
#     ("Alice", "Slime"),
#     ("Bob", "Dragon"),
#     ("Eve", "Goblin")
# ]

# #define a function
# def monster_tamer(i):
#     #declare an empty dict
#     tamed = {}
#     #unpack nd loop through tuples
#     for tamer, monster in i:
#         #created holder = dict key empty dict
#         tamed_monster = tamed.get(tamer, {})
#         #holder val = holder.get(val 0) + 1
#         tamed_monster[monster] = tamed_monster.get(monster, 0) + 1
#         #dict[key] = holder
#         tamed[tamer] = tamed_monster
#     #return dict
#     return tamed

# #create car to hold function(input)
# who_got_what = monster_tamer(tame_logs)
# # print(who_got_what)

# #create another function to list/print
# def printed_monster_tally(i):
#     #for key, value in input.items()
#     for tamer, monsters in i.items():
#         #for value, value2 in values.items()
#         for monster, count in monsters.items():
#             #print (key, val1 , val2)
#             print(tamer, monster, count)
#             #bonus if count >= 2
#             if count >= 2:
#                 print(f"{tamer} really has it out for {monster}!")

# printed_monster_tally(who_got_what)

#forgot to call my print function to run and see results at first.....had it right initially lol....starting to get tired but there's no time left

# # 🧠 Coding Assessment-Style Question:
# # “Majority Element”
# # ❓ Prompt:
# # You are given a list of strings representing votes cast in an election.
# # Your job is to write a function that:
# # Returns a dictionary showing how many votes each candidate got
# # Prints the name of the candidate who received the most votes

# votes = [
#     "Alice", "Bob", "Alice", "Derek", "Alice", "Bob",
#     "Derek", "Derek", "Bob", "Alice", "Alice", "Derek", "Bob"
# ]

# #define a function
# def vote_counter(i):
#     #create a dict to hold our candidate and votes
#     vote_count = {}
#     #simple loop and count to track name and votes
#     for name in i:
#         vote_count[name] = vote_count.get(name, 0) + 1
#     #return our dict
#     return vote_count

# #we want a var to hold our dict
# apr_votes = vote_counter(votes)
# # print(apr_votes)

# #declare another funciton
# def vote_counter_printer(i):
#     #unpack and loop through our dict
#     for name, votes in i.items():
#         #not nested so no double loop:
#         print(name, votes)
#         #tried to print max(votes) and string interpolate the winner 
#         # winner = votes.max()
#         # print(f"{name} won with {votes} votes")
#         #won't try to get fancy

# vote_counter_printer(apr_votes)

#what is list comprehension -
    #a compact way to build a new list by looping through another one, applying logic as you go
    # basic form :
    #     [expression for item in iterable]
    # it's just a one liner for a "for" loop that returns a list

    # ex ----

# nums = [1,2,3,4]
# squares = [n**2 for n in nums] #n**2 is value to the 2nd power
# print(squares)

#same as above
# squares = []
# for n in nums:
#     squares.append(n**2)
    
# print(squares)

# #using with a condition
# evens = [n for n in nums if n % 2 ==0]
# print(evens)

#transform and filter
# doubled_odds = [n*2 for n in nums if n% 2 != 0]
# print(doubled_odds)

#burn in drills ------
#basic transformation

# nums = [1, 2, 3, 4, 5]
# squared = [n ** 2 for n in nums]
# print(squared)
#var = looped item ** 2 for item in nums list
# squared = [ n ** 2 for n in nums]
# print(squared)
# squared = [n ** 2 for n in nums]
# print(squared)
#create var to hold answer = [item ** 2 for item in nums list] - so why the brackets....going to be something to learn/think i what i can actually do inside these
# so broken down
#making a list - [] why it's in brackets
# n**2 - what we want in the list
#for n in nums - loop that feeds the values

#copy drill 2 transformation and condition
# names = ["ada", "bob", "alice", "eve"]
# short_names = [name.upper() for name in names if len(name) <=3]
# print(short_names)