# word = "gravity"
# # Expected Output: "ytivarg"

# # Build it using a loop and add each letter to a new string
# for i in range(len(word) -1, -1, -1):
#     print(word[i])
#     #if you want to be fancy and print it out sideways
#     #print(word[i], end=" ")

# nums = [10, 20, 30, 40, 50, 60]

# # Grab the middle 4 numbers using slicing.
# # Expected Output: [20, 30, 40, 50]

# for i in nums:
#     print(i)
#     middle_4 = i.slice(1,2,3,4)
#     print(middle_4)
    

# text = "lazy devs lose jobs"

# # Build a dictionary that counts how many times each letter appears.
# # Use .get() — no if-statements, no Counter.
# # Expected: {'l':1, 'a':1, 'z':1, ...}
# letter_dict = {}
# for b in text:
#     letter_dict[b] = letter_dict.get(b, 0) + 1
# print(letter_dict)

# nums = [12, 5, 8, 13, 10, 7]
# # # ✅ Expected: 30 (12 + 8 + 10)
# # # Write a one-liner using sum() and a generator or list comp.
# # #not right but trying to go off memory and not google syntax
# # even_sum = for i in nums if i % 2 == 0: sum(i)
# even_sum = sum(i for i in nums if i % 2 == 0)
# print(even_sum)

# words = ["banana", "apple", "watermelon", "kiwi"]
# # ✅ Expected: "watermelon"
# # Use max() and key= to find the longest word.
# for i in words:
#     print(i)
      #this is not right  
#     longest_word = max(i)
#     print(longest_word)

# sentence = "this is a very important sentence"
# # ✅ Expected: Total number of vowels (a, e, i, o, u)
# # Build a function that returns the count.
# counter = 0
# for j in sentence:
#     if j in "aeiou":
#         counter += 1
# print(counter)

# nums = [3, 3, 5, 1, 3, 5, 1, 1, 7]

# # ✅ Expected Output:
# # {3: 3, 5: 2, 1: 3, 7: 1}
# # Use a dictionary and .get() to count each number.
# number_count_dict = {}
# for m in nums:
#     number_count_dict[m] = number_count_dict.get(m, 0) +1
# print(number_count_dict)

# nums = [2, 5, 8, 11, 4, 7]
# #return a list of the even numbers squared -

# #for every number in nums list
# for i in nums:
#     #if that num is even 
#     if i % 2 == 0:
#         #square that number 
#         squared_even = i ** 2
#         print(squared_even)

# smart_squared = [i ** 2 for i in nums if i % 2 ==0]]

#learning Comprehension -
 # syntax = [expression for item in iterable] / 
 # same as 
 # result = []
#  for item in iterable:
#     result.append(expression)

#adding filters -
#[expression for item in iterable if condition]
#same as
#result = []
# for item in iterable:
#     if condition:
#         result.append(expression)

# -----examples---------

#     # multiply x by 2 for x that is in range of 0-5
# print([x * 2 for x in range(5)])
#     # list x for x in range(0-10) if it's even(modulus 2)
# print([x for x in range(10) if x % 2 == 0])
#     # square x from the list if x is more than 5
# print([x ** 2 for x in [3, 6, 9] if x > 5])

# #you are looping through / optionally filtering / transforming each as you go

# words = ["cat", "banana", "dog"]
# lengths = [len(w) for w in words]
# print(lengths)

# nums = [1, 3, 5, 8, 2, 10, 7]
# #return a list of each even number squared, only if it's greater than 20
# #brute it than use list comprehension to refractor

# #function
# def big_squared(x):
    #holder for our new list
    # test_output = []
#     #loop throgh our list
#     for i in x:
#         #if our squared number is greater than 20
#         if i ** 2 > 20:
#             #fill our list with squared numbers over 20
#             test_output.append(i ** 2)
#     #was asked to return and not print so we can use our data
#     return test_output
# #printed to test and it seems i got more than they expected?
# print(big_squared(nums))

# #now trying to list comp one line
# #new var = i squared in numbers if i squared = more than 20 - needed to look at notes to remeber structure
# over_20_squared = [i **2 for i in nums if i ** 2 > 20]
# print(over_20_squared)


# # #return a nested dictionary -
# # #the print the top item each customer bought
# orders = [
#     ("Alice", "apple", 2),
#     ("Bob", "banana", 5),
#     ("Alice", "banana", 3),
#     ("Bob", "apple", 1),
#     ("Alice", "apple", 4),
#     ("Bob", "banana", 2),
# ]

# # Same as always:
# # Write a function that builds the data
# # Write another that analyzes and prints it
# # No cheating with defaultdict or pandas, just raw Python brain
# # Drop your answers when ready, coding gladiator 🥊

# #make a function
# def fruit_picker(x):
#     #need an empty dict
#     fruit_dict = {}
#     #need to unpack our tuples and loop....idk why but forgot to add the 3rd var to unpack....we figured it out though
#     for customer, fruit, num in x:
#         #creat a var to hold our nested dictionary
#         quant_holder = fruit_dict.get(customer, {})
#         #need to count the fruit in our nested dict
#         quant_holder[fruit] = quant_holder.get(fruit, 0) + num
#         #need to put our nested dict in our outer
#         fruit_dict[customer] = quant_holder
#     return fruit_dict

# # print(fruit_picker(orders))
# fruit_data = fruit_picker(orders)
# # print(fruit_data)

# #new function -
# def list_orders(x):
#     #need to loop and unpack - i think it's key - value and make value plural 
#     for customers, fruits in x.items():
#         #unpack 2nd part
#         for fruit, num in fruits.items():
#             #return our vars so we can print?
#             listed_orders = (customers, fruit, num)

# nums = [4, 7, 1, 9, 6, 2, 3]
# # Return a list of only the odd numbers, squared
# # Use a list comprehension
# #googled how to check for odd number if divised by 2 it leaves a remainder of 1 so % 2 == 1

# #so create a var, = bracket[list comp], var squared in num if var % 2 == 1
# squared_odd = [i ** 2 in nums if i % 2 == 1:]
# print(squared_odd)

# orders = [
#     ("Maya", "peach", 3),
#     ("Liam", "plum", 1),
#     ("Maya", "peach", 2),
#     ("Liam", "peach", 5),
#     ("Nina", "plum", 4),
#     ("Nina", "peach", 1),
#     ("Liam", "plum", 2),
# ]

# #define a function
# def purchase_orders(x):
#     #declare our empty dict
#     customer_order = {}
#     #need to unpack our tuple:
#     for customer, fruit, num in x:
#         #create a holder for nested dict
#         fruit_basket = customer_order.get(customer, {})
#         #need to fill our basket with quantity of fruit
#         fruit_basket[fruit] = fruit_basket.get(fruit, 0) + num
#         # put our nested in our outer dict
#         customer_order[customer] = fruit_basket
#     return(customer_order)

# #make sure we filled our dict right
# #print(purchase_orders(orders))
# purchase_history = purchase_orders(orders)
# # print(purchase_history)

# def fruit_tracker(something):
#     for customer, fruit in something.items():
#         #checking to see if we unpacked enough
#         print(customer, fruit)
#         most_bought = max(customer, key=fruit)
# print(fruit_tracker(purchase_history))

# ------------ keys() accessing dict keys ---------
# #use .keys() to retrieve all the keys from a dictionary  -
# my_dict = {'a': 1, 'b': 2, 'c': 3}
# # print(my_dict.keys())

# # #use .values() to get all values
# # print(my_dict.values())

# # # use .items() to retrieve key-value pairs as tuples
# # print(my_dict.items())

# #practice round ..... 
# for key in my_dict.keys():
#     print(f"Key: {key}")
# # for values in my_dict.values():
# #     print(f"Value: {values}")
# # for key, value in my_dict.items():
# #     print(f"Key: {key}, Value: {value}")

# student_scores = {'Alice': 85, 'Bob': 90, 'Charlie': 78}
# #we have our filled dict.....we want to find the student with the highest score

# #declare our new var which = the max(highest score)out of student_scores.items() key = lambda function to find item 1?
# top_student = max(student_scores.items(), key=lambda item: item[1])
# #simple print statement with string interpulation - that pulls in the student name(key) and score(value pair)?
# print(f"Top student: {top_student[0]} with a score of {top_student[1]}")

# 🧙 lambda item: item[1] says: “Hey max(), compare by the score (index 1), not the name.”

# 💡 You could read it like:

# "Find the tuple where the second thing (the score) is the biggest."

#working on looping over key value pairs -----

data = {"apple": 3, "banana": 5, "cherry": 2}

# for fruit, count in data.items():
#     print(f"{fruit}: {count}")

# for key, value in dict.items():
#     print(stringinterpolation"{key} : {value}")

# for fruit, count in data.items():
#     print(f"{fruit}: {count}")
# for fruit, count in data.items():
#     fruit = f"{fruit}"
#     print(fruit)
#     count = f"{count}"
#     print(count)

# for i, b, in data.items():
#     print(i)
#     print(b)

# for fruit in data.keys():
#     print(fruit)
# for num in data.values():
#     print(num)

#highes value in a dict-----
# scores = {"Alice": 92, "Bob": 87, "Charlie": 78}

# top = max(scores.items(), key=lambda item: item[1])
# print(f"{top[0]} has the highest score: {top[1]}")
# #when we created our top var it made a tuple of just the highest based off item[1] 
# # still confused by the syntax of key=lambda item:[1] and would we change the item[1] to item[2] if there are multiple pairs 
# # and wanna rank by another value?
# print(f"{top}")

#score.items() turns the dict in to a bunch of tuples like ("alice", 92)
#lambda item: item[1] says grab the second thing in the tuple
#max(......, key=....) says find the bigges one based on the value from the lambda
#translated = get me the key-value pair in the dictionary where the value is the highest

# #regular string
# sentence = "hello there"
# #empty dict
# count = {}
# #loop through our str
# for char in sentence:
#     #don't include spaces/ only letters
#     if char != " ":
#         #count how many letters in the string
#         count[char] = count.get(char, 0) +1
# #create a new var that looks for the highest count, i think it makes tuples per key/value with the .items and the lamdbda compares them all according to the value[1]
# top_letter = max(count.items(), key=lambda item: item[1])
# print(f"Most common letter: {top_letter[0]} ({top_letter[1]} times)")

# #we want to find the most common fruit from a list
# fruits = ["apple", "banana", "apple", "orange", "banana", "apple"]

# #create an empty dictionary
# fruit_counts = {}

# #loop through the fruit:
# for fruit in fruits:
#     #fill our dictionary with the key fruit - and count how many 
#     fruit_counts[fruit] = fruit_counts.get(fruit, 0) +1

# # Use max() with .items() and lambda to find the fruit with the highest count (item[1])
# top_fruit = max(fruit_counts.items(), key=lambda item: item[1])
# print("most common is", top_fruit)

# #finding the most common nummber
# numbers = [3, 1, 4, 1, 5, 3, 1, 4, 4, 4]
 
# #create an empty dict
# number_count = {}

# #loop through our list
# for nums in numbers:
#     #need to count the numbers and track...using get to prevent errors
#     number_count[nums] = number_count.get(nums, 0) +1

# most_common = max(number_count.items(), key=lambda item: item[1])
# print(f"the most common number is {most_common[0]} and it showed {most_common[1]} times")

#memory typing 
# number_count.items(), = turns the dictionary into a list of tuples
# key=lambda item: item[1] this tells max - look at second part of tuple and pick the biggest one
#max(...) pick the biggest in this case 4,4
#most_common[0] = number (first part of tuple)
#most_common[1] = how many times it showed up

# sentence = "the dog and the cat and the mouse"
# #we want the most common word .........
# #create an empty dict
# word_counter = {}
# #loop through
# for word in sentence.split():
#     #count our words and place them in dictionary.....wonder if we need to skip spaces
#     word_counter[word] = word_counter.get(word, 0) +1

# max_word = max(word_counter.items(), key=lambda item: item[1])
# print(f"the most common word is '{max_word[0]}' it is said {max_word[1]} times")

# sentence = "run rabbit run rabbit run run run"
# # Expected output:
# # Most common word: run (4 times)
# #empty dictionary 
# word_count = {}

# #need to loop through the str
# for i in sentence.split():
#     word_count[i] = word_count.get(i, 0) +1

# most_used_word = max(word_count.items(), key=lambda item: item[1])
# print(f"the most used word = {most_used_word[0]} and it was used {most_used_word[1]} times")

# sentence = "Dog dog DOG cat Cat cAt doG DOG"
# # Expected output: Dog (5 times)
# # Make it case-insensitive!
# #empty dictionary 
# word_tracker = {}
# #loop through - need to make it all same and split the words
# for word in sentence.lower().split():
#     #count our words
#     word_tracker[word] = word_tracker.get(word, 0) +1

# common_word = max(word_tracker.items(), key=lambda item: item[1])
# print(f"the most common word used is {common_word[0]}, and it was used {common_word[1]} times")

# string = "My brain is melting from trying to learn all this python. I should take a break soon. I am pretty tired"

# word_count = {}

# # for i in string.lower().split():
# #     word_count[i] = word_count.get(i, 0) +1
# # print(word_count)
# # most_used = max(word_count.items(), key=lambda item: item[1])
# # print(f"the most used word is {most_used[0]}")

# for char in string.lower():
#     if char.isalpha():
#         word_count[char] = word_count.get(char, 0) +1

# most_used_letter = max(word_count.items(), key=lambda item: item[1])
# print(f"the most used letter is {most_used_letter[0]} and it was used {most_used_letter[1]} times")

# # -----sorted() and key ----------
# sorted(iterable)

# returns a new sorted list from any iterable (list, tuple, etc)
# sorted([5, 3, 9, 1]) -> [1, 3, 5, 9]

# key= lets you control how things are sorted

# words = ["banana", "fig", "watermelon", "apple"]
# sorted(words, key=len)
# -> ["fig", "apple", "banana", "watermelon"]

# scored = [("Alice", 85), ("Bob", 90), ("Charlie", 78)]
# #here we are sorting the scores by the 2nd item in the tuple .....
# #so it's always var, key = lambda and then var: var[1]
# sorted(scores, key=lambda x: x[1])

# students = [("Zoe", 92), ("Amy", 99), ("Jake", 85), ("Leo", 91)]
# #sort by ascending
# by_score = sorted(students, key=lambda x: x[1])
# print("By score:", by_score)

# #sort by name
# by_name = sorted(students, key=lambda x: x[0])
# print("by name:", by_name)

# #sort by score (descending)
# by_top_score = sorted(students, key=lambda x: x[1], reverse=True)
# print(f"from highest to lowest score...{by_top_score}")

# students = [
#     ("Zoe", 92),
#     ("Amy", 99),
#     ("Jake", 85),
#     ("Leo", 91),
#     ("Maya", 78),
#     ("Ella", 88)
# ]

# #we want to print out a top 3 score list

# #we want top 3 so sort by score and reverse = true?
# high_score = sorted(students, key=lambda x: x[1], reverse=True)
# print(high_score)

# coins = [
#     ("Mario", 45),
#     ("Luigi", 30),
#     ("Peach", 50),
#     ("Toad", 40),
# ]
# #so normal is sorted, to sort diff use sorted and then key and value for key...this works for tuples / lists

# sorted_coins = sorted(coins, key=lambda x: x[1], reverse=True)
# print(sorted_coins)

# nums = [12, 20, 30, 40, 50, 60]
# # [start:stop(notincluded)]
# print(nums[2:4]) 

# text = "gravity"
# #start at beginning and stop at index 3(not included)
# print(text[0:3])
# #it goes backwards and looks like our start stop step but im sure not the same
# print(text[::-1])

# text = "abcdef"
# print(text[::])
# print(text[::1])


