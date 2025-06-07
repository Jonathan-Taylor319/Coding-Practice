# # word frequency word counter   

# text = "I love Python because I love solving problems with Python"

# # need a function
#     #create an empty dictionary
#     #we need to loop through the str.split()
#         #make sure to fill our dictionary
#     #return our dictionary

# def word_counter(text):
#     words_counted = {}
#     for word in text.split():
#         words_counted[word] = words_counted.get(word, 0) +1 
#     return words_counted

# print(word_counter(text))

# # find the most frequent number 

# nums = [3, 5, 2, 3, 8, 3, 2, 5, 2]

# def top_num_counter(num):
#     numbers_found = {}
#     for numbers in num:
#         numbers_found[numbers] = numbers_found.get(numbers, 0) +1
#     #new var to hold most common = highest(dictionary, key=[dictionary info we want].get)
#     most_common = max(numbers_found, key=numbers_found.get)
#     return most_common

# print(top_num_counter(nums))


# # reverse the sentence 

# sentence = "Python makes me feel powerful"

# def sent_reversed(words):
#     #forgot if i can slice or i can just split.reverse.join
#     word_list = words.split()
#     word_list.reverse()
#     return ' '.join(word_list)

# # print(sent_reversed(sentence))

# .filter()

# .filter() is used to selec only the items in a list that meets a condition.
# it doesn't modify the original list - it returns a new one. 
# filter(function, iterable)

# nums = [1, 2, 3, 4, 5]

# evens = list(filter(lambda num: num % 2 == 0, nums))

# lambda num: num % 2 == 0 
# This is an anonymous function (a Lambda function). it means:
#   - for each num in the list, check if its evenly divisible by 2

# filter(....)
# a function (lambda num: num % 2 ==0)
# an iterable (nums)

# list(.....)
# wrap the whole filter() call in list() to turn the result in a proper list to use or print

# print(evens)

# | Part           | Meaning                                 |
# | -------------- | --------------------------------------- |
# | `lambda num:`  | anonymous function that takes `num`     |
# | `num % 2 == 0` | returns `True` if `num` is even         |
# | `filter(...)`  | applies function to each item in `nums` |
# | `list(...)`    | converts the result to a list           |

# copy drill

# numbers = [4, 7, 10, 13, 16, 19, 22]

#using filter with lambda
# even_numbers_filter = list(filter(lambda num: num % 2 == 0, numbers))
# print (even_numbers_filter)
# even_numbers_filter = list(filter(lambda num: num % 2 == 0, numbers))
# print(even_numbers_filter)
# even_numbers_filter = list(filter(lambda num: num % 2 == 0, numbers))
# print(even_numbers_filter)
# even_numbers_filter = list(filter(lambda num: num % 2 == 0, numbers))
# print(even_numbers_filter)
# even_numbers_filter = list(filter(lambda num: num % 2 == 0, numbers))
# print(even_numbers_filter)

# list comp way (refractered)
# even_numbers_comp = [x for x in numbers if x % 2 == 0]
# print("Even numbers (list comp):", even_numbers_comp)

# # return numbers divisible by 3
# numbers = [2, 3, 5, 6, 9, 11, 12, 14, 18]

# divis_by_3 = list(filter(lambda num: num % 3 == 0, numbers))
# print(divis_by_3)

# #new var = [var for loop in list if var % 3 == 0]
# divis_3 = [x for x in numbers if x % 3 ==0]
# print(divis_3)