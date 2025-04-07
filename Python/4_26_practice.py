# warm up drills ---make sure i got it ----

# nums = [3, 7, 1, 9]
# count = 0
# for i in nums:
#    count += i
#    print(count)

# count = 1
# nums = [2, 4, 6]
# # Expected output: 48
# for i in nums:
#     count *= i
#     print(count)


# # # print only vowels
# text = "wake up and choose violence"
# # Expected output: a, e, u, a, o, o, e, i, e
# #i can't remebmber the syntax to pull out what i want......
# for i in text:
#     if i in "aeiou":
#         print("text has", i)

# text_1 = "this is my pracitce string"
# for i in text_1:
#     if i in "aeiou":
#         print("text 1 has:", i)

# text_3 = "I want to play some final fantasy"
# for i in text_3:
#     if i in "29daboe":
#         print("text 3 has", i)


# remember range(len(start, stop step))
    
# word = "python"
# # Expected output: n, o, h, t, y, p
# #i know i need a -1 but can't remember idk why
# for i in range(len(word)-1, -1, -1):
#     print(word[i])

# word_1 = "nascar"
# for i in range(len(word_1)-1, -1, -1):
#     print(word_1[i])

# so if 
# word = "python"
# len(word) = 6
    
#     so
# range(len(word), 0, -1)
#     becomes
# range(6, 0, 1)
#     that gives
# 6,5,4,3,2,1

# but that is wrong when looping through a list or str........
# because index 6 doesn't exist
# indexes are 0 - len(word) -1 - so 0-5

    


# word = "bananas"
# # Expected output: {'b': 1, 'a': 3, 'n': 2, 's': 1}
# letters_in_word = {}

# for letters in word:
#     letters_in_word[letters] = letters_in_word.get(letters, 0) + 1
# print(letters_in_word)

# nums = [1, 2, 2, 3, 3, 3]
# # Expected output: {1: 1, 2: 2, 3: 3}
# how_many_numbers = {}
# for num in nums:
#     how_many_numbers[num] = how_many_numbers.get(num, 0) + 1
# print(how_many_numbers)

# logs = [
#     ("Alice", "email"),
#     ("Bob", "login"),
#     ("Alice", "login"),
#     ("Bob", "email"),
#     ("Alice", "upload"),
# ]

# actions = {}

# for name, action in logs:
#     logged_actions = actions.get(name, {})
#     logged_actions[action] = logged_actions.get(action, 0) +1
#     actions[name] = logged_actions
# print(actions)

# for name, things in actions.items():
#     for thing, count in things.items():
#         print(name, thing, count)



#range refresh
# for i in range(0, 5):
#     print(i)

# for i in range(0, 10, 2):
#     print(i)

# for i in range(5, 0, -1):
#     print(i)

# for i in range(10, 0, -2):
#     print(i)

# word = "python"
# for i in range(len(word)-1, -1, -1):
#     print(i)

#for i in range(some_lists) -1, -1, -1):
    # print(some_list[i])

#     Prompt:

# You are given a list of purchase records from a store.
# Each record is a tuple: (customer_name, item_name)

# Your task:

# Write a function that builds a nested dictionary

# Then, write another function that:

# Prints each customer’s name

# Prints their total number of items purchased

# Prints the most frequently bought item (or one of them, if tied

# purchases = [
#     ("Alice", "apple"),
#     ("Bob", "banana"),
#     ("Alice", "banana"),
#     ("Alice", "apple"),
#     ("Bob", "banana"),
#     ("Bob", "banana"),
#     ("Derek", "apple"),
#     ("Derek", "apple"),
#     ("Derek", "banana")
# ]

# #declare a function
# def shopping_history(i):
#     #created an empty dict:
#     grocery_history = {}
#     #unpack and loop through the list:
#     for customer, purchase in i:
#         #created a holder for our nested dict
#         items = grocery_history.get(customer, {})
#         #populate our inner dict
#         items[purchase] = items.get(purchase, 0) + 1
#         #attach our outer dict
#         grocery_history[customer] = items
#     #return our dict
#     return grocery_history

# #print check and if works make a var
# shopper_history = shopping_history(purchases)
# #print to make sur we are good
# #print(shopper_history)

# def print_shopping_log(o):
#     for customer, items in o.items():
#         total = sum(items.values())
#         favorite = max(items, key=items.get)
#         print(f"{customer} bought {total} items. Favorite: {favorite}")


# print_shopping_log(shopper_history)

# sales = [
#     ("Dune", 5),
#     ("1984", 3),
#     ("Dune", 7),
#     ("Foundation", 4),
#     ("1984", 2),
#     ("Dune", 1)
# ]

# def book_sales(sales):
#     book_sold = {}
#     for title, qty in sales:
#         book_sold[title] = book_sold.get(title, 0) + qty
#     return book_sold

# def listed_book_sales(sales_dict):
#     total = sum(sales_dict.values())
#     best = max(sales_dict, key=sales_dict.get)
#     print(f"Total units sold: {total}")
#     print(f"Best seller: {best} ({sales_dict[best]} copies)")

# book_bought = book_sales(sales)
# listed_book_sales(book_bought)

# 💥

# 🧠 REAL ASSESSMENT-STYLE CHALLENGE: “Most Common Triplet”
# ❓ Prompt:
# You are given a list of strings representing user-submitted search queries.
# Each query is a single word. You must analyze all groups of 3 consecutive queries (triplets) and identify the most commonly occurring triplet.
# Your task:
# Write a function that scans through the list and tracks how often each triplet appears.
# Return the triplet that appeared most frequently, and how many times it appeared.

# words = ["apple", "banana", "carrot", "date", "elderberry"]

# for i in range(len(words) -1):
#     pair = (words[i], words[i+1])
#     print("PAIR", pair)

# for i in range(len(words) -2):
#     pair = (words[i], words[i+1])
#     print("PAIR :", pair)

# for in range(len(list) -2)
#     declare a var for the items i want to pul out





# # ("cat", "dog", "fish")  ➜ 3

# 💥 Requirements:
# Use .get() to track counts (no defaultdict, no Counter)
# Use range() smartly to avoid index errors
# Return the most common triplet and how many times it appeared
# Do not use fancy imports — built-in Python only


# queries = [
#     "cat", "dog", "fish",
#     "cat", "dog", "fish",
#     "dog", "cat", "fish",
#     "cat", "dog", "fish"
# ]

