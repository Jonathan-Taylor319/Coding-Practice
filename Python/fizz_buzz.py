 
# The FizzBuzz Problem
# Problem Statement:
# Write a program that prints the numbers from 1 to 100. But for multiples of 3, print "Fizz" instead of the number, for multiples of 5, print "Buzz",
#  and for numbers which are multiples of both 3 and 5, print "FizzBuzz".

# Steps to consider:

# Looping:
# Use a loop to iterate through numbers 1 to 100.

# Conditionals:
# For each number:

# Check if it’s divisible by both 3 and 5.

# Else, check if it’s divisible by 3.

# Else, check if it’s divisible by 5.

# Otherwise, print the number.

# Output:
# Ensure each output is printed on a new line (or with a clear separation). 

# def Fizz_Buzz():
#     for i in range(1, 101):
#         if i % 15 == 0:
#             print("FizzBuzz")
#         elif i % 5 == 0:
#             print("Buzz")
#         elif i % 3 == 0:
#             print("Fizz")
#         else:
#             print(i)

# --------------Learning To Refractor---------------

# create a helper function
def get_fizz_buzz(i):
    if i % 15 == 0:
        return("FizzBuzz")
    elif i % 5 == 0:
        return("Buzz")
    elif i % 3 == 0:
        return("Fizz")
    else:
        return(i)

#call the helper function
def Fizz_Buzz():
    for i in range(1, 101):
        print(get_fizz_buzz(i))

Fizz_Buzz()
