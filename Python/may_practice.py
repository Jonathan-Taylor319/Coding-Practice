# Write a function centered_average(nums) that returns the "centered" average of a list of integers — the mean average excluding the largest and smallest values.
# You ignore only one copy of the min and max each.
# The list will always have at least 3 numbers.

# centered_average([1, 2, 3, 4, 100]) → 3
# centered_average([1, 1, 5, 5, 10, 8, 7]) → 5
# centered_average([-10, -4, -2, -4, -2, 0]) → -3

# # create a function
# def centered_average(nums):
#     # sort our numbers using .sort() built in
#     nums.sort()
#     # need to find a way to remove first and last numbers/ using slicing....need to go back and practice learn get better with slicing
#     trimmed = nums[1:-1]
#     # add the rest  / use sum built in method sum()
#     total = sum(trimmed)
#     # divide the rest by the number of numbers in the list
#     return total // len(trimmed)

# nums = [10, 20, 30, 40, 50]
# just_mid = nums[1:-1]
# print(just_mid)

# nums = [11, 22, 33, 44, 55, 66]
# every_other = nums[::2]
# print(every_other)

#     5/15 ----------- INDEXING AND SLICING PRACTICE AND REMINDERS -------

# Simple index reminder --- “Positive moves forward, negative moves from the end.”

# SLICING -
#   a[start:stop:step]
#   returns a new list containing section of the original 
#   can use 1 - 3 parts
#   if you skip----
#   start defaults to 0
#   stop defaults to the end
#   step defaults to 1
# a = [5, 10, 15, 20, 25]

# #start at 1 stop before 4 increment by 1 since no 3rd value
# print(a[1:4]) # [10, 15, 20]

# #start at 0 stop at end increment by 2
# print(a[::2])

# #start at 0 end at end go backwards by 1
# print(a[::-1])

# #default to 0 / stop before 3 / default inc by 1
# print(a[:3])

# #start at 3 from the end / default going to end / default increment of 1
# print(a[-3:])

# nums = [11, 22, 33, 44, 55, 66, 77]

# #return the middle 3

# #so start at 2, stop before 5, default inc by 1
# print(nums[2:5:])

# nums[2:5]     ✅ Clean
# nums[2:5:]    ✅ Redundant, but still works
# nums[2:5:1]   ✅ Explicit

# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# # every 3rd number starting from the 2nd item (index 1)

# #so we want to start at 1 / default to end / increment by 3
# print(nums[1::3])

# letters = ["a", "b", "c", "d", "e", "f", "g", "h"]

# # Use slicing to return the list in reverse, but only every 2nd element, starting from the end.
# #start at end -1 / default to end / go back every 2
# # print(letters[-1::-2])

# # When slicing in reverse, your start must be after your stop, and your step must be negative.
# print(letters[::-2])

# nums = [100, 200, 300, 400, 500, 600, 700]
# # get 4th to last through 2nd to last elements in reverse order
# # ie [500, 400, 300]

# #start at end going to try leaving blank / stop at element 2 / reverse by 1
# print(nums[4:1:-1])

# so actually i have to say start at 4th index / stop before printing 1st / count down by 1

# data = ["x", "y", "a", "b", "c", "d", "e", "z"]
# # return middle 5 in reverse order

# # start at index 6 / stop before index 1 / go backwards by 1
# print(data[6:1:-1])

# letters = ["A", "B", "C", "D", "E", "F", "G"]
# # return all but first and last

# #start at 1 / stop at 6 / default to go by 1
# print(letters[1:6])

# nums = [10, 20, 30, 40, 50, 60, 70, 80, 90]
# # return middle 5 in reverse and skip every other one

# #start at 6 / stop before 20(1) / count every other backwords(-2)
# print(nums[6:1:-2])

# 🔁 1. Looping Logic: FizzBuzz with a Twist
# Print numbers from 1 to 50, but:

# For multiples of 3, print "Fizz"

# For multiples of 5, print "Buzz"

# For multiples of both 3 and 5, print "FizzBuzz"

# For prime numbers, print "Prime" instead

# 👉 Try writing this with a helper function to detect primes.

# # define a function
# def isprime(num):
#     # see if prime number
#     if num < 2:
#         return False
#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0:
#             return False
#     return True



# # define a function
# def fizz_buzz(num):
# #     count from 1 to 50
#     while num < 51:
# #     use helper function to check for prime
#         if isprime(num) == True:
#             print("Prime")
#             num += 1
# #     check for multiples of 3 and 5
#         elif num % 15 == 0:
#             print("FizzBuzz")
#             num += 1
# #     check for multiples of 5
#         elif num % 5 == 0:
#             print("Buzz")
#             num += 1
# #     check for multiples of 3
#         elif num % 3 == 0:
#             print("Fizz")
#             num += 1
#         else:
#             print(num)
#             num += 1

# fizz_buzz(1)

# Write a function word_frequency(text) that:
# Accepts a string
# Returns a dictionary with word counts (ignore case and punctuation)
# # Example:
# word_frequency("Hello hello! How are you, hello?")
# # Output: {'hello': 3, 'how': 1, 'are': 1, 'you': 1}

# def word_counter(sample):
#     counted_words = {}
#     for word in sample.split():
#         counted_words[word] = counted_words.get(word , 0) +1
#     return counted_words

# print(word_counter("this is my sample because this will fill this dictionary ?"))

# 🔄 Challenge 4: List Slicer
# Write a function reverse_chunks(lst, size) that:
# Splits the list into chunks of length size
# Reverses each chunk
# Returns a new list made up of those reversed chunks

# reverse_chunks([1, 2, 3, 4, 5, 6, 7, 8], 3)
# → [3, 2, 1, 6, 5, 4, 8, 7]

