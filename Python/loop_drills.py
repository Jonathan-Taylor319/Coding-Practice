# # -----------------🔁 FOR LOOP DRILLS----------------------
# # 🔧 1. Sum a list manually
# # Input: [5, 8, 12, 3]
# # Expected Output: 28
# num_list = [5, 8, 12, 3]
# # print(len(num_list))
# j = 0
# for i in num_list:
#     # print(i)
#     j = j+ i
# print(j)



# # 🔧 2. Multiply all numbers in a list
# # Input: [2, 4, 6]
# mult_list = [2, 4, 6]
# m = 1 #i know we are  multiplying so 1 works but is there another way or is this fine?
# for i in mult_list:
#     m = m * i
# print(m)
# # Expected Output: 48


# # 🔧 3. Print only vowels from a string
# # Input: "loop through this text"
# string_a = "loop through this text"
# for v in string_a:
#     #confirm it's printing letters = yes
#     #print(v)
#     if v == "a":
#         print(v)
#     elif v == "e":
#         print(v)
#     elif v == "i":
#         print(v)
#     elif v == "o":
#         print(v)
#     elif v == "u":
#         print(v)
# #--- better - much cleaner way -- i tried but couldn't figure it out
# for l in string_a:
#     #if letter is one of "" then print
#     if l in "aeiou":
#         print(l)

# #same output but not in same order ... could be better
# # Expected Output:
# # o  
# # o  
# # u  
# # o  
# # u  
# # i  
# # e  

# # 🔧 4. Reverse a string using a loop (no slicing)
# # Input: "python"
# r_string = "python"
# for l in range(len(r_string) -1, -1, -1):
#     print(r_string[l])
   
# # Expected Output: "nohtyp"

# # 🔧 5. Print all even numbers from a range
# # Input: range(1, 21)
# for i in range(1, 22):
#     if i % 2 == 0:
#         print(i)

# #alternative way....i need to get used to using range -
# #when using range(start, stop, step)
# #starts at 2, stops at 21, steps by 2 (even numbers only)
# for i in range(2, 21, 2):
#     print(i)

# Expected Output:
# 2  
# 4  
# 6  
# 8  
# 10  
# 12  
# 14  
# 16  
# 18  
# 20

#------------------------Getting there------------------------

# 🔄 WHILE LOOP DRILLS
# 🔧 6. Countdown timer from user input
# # Input: 5
# #make a var / this var asks for user input and makes sure to make it a int
# user_number = int(input("Enter a number: "))
# #we then take the number and simply loop while the number is greater than 0
# while user_number > 0:
#     #print the number
#     print(user_number)
#     #decrease the number by 1
#     user_number -= 1
# #once out of the loop print time is up
# print("Time's up!")

def personal_timer():

    x = int(input("enter a number: "))

    while x > 0:
        print(x)
        x -= 1
    print("TIME IS UP!")

#personal_timer()

# Expected Output:
# 5  
# 4  
# 3  
# 2  
# 1  
# Time's up!


# 🔧 7. Keep asking until "exit"
# Input (typed by user): hi, ok, no, exit

def simple_while_app():
    keep_running = True

    while keep_running == True:
        str_input = input("Enter hi, ok, no, or exit and see what happens.....:")
        if str_input == "hi":
            print("hey there......!")
        elif str_input == "ok":
            print("yessssssss, everything is going to be ok")
        elif str_input == "no":
            print("don't tell me no......")
        elif str_input == "exit":
            print("okay! bye")
            keep_running = False
        else:
            print("invalid input")

simple_while_app()

# Expected Output:
# You typed: hi  
# You typed: ok  
# You typed: no  
# Goodbye!


# 🔧 8. Sum user numbers until limit
# Input (typed): 5, 10, 15, 10
# Stop when total reaches or exceeds 30

num = 0

while num < 20:
    user_num = int(input("input a number "))
    num += user_num
    print(f" your total is: {num}")
    if num > 20:
        print("Limit Reached")
    

# Expected Output:
# Running total: 5  
# Running total: 15  
# Running total: 30  
# Limit reached!


# 🔧 9. Number guessing game (you set the number)
# User keeps guessing until correct
answer = 9
answer_guessed = False

while answer_guessed == False:
    user_guess = int(input("guess a number between 1 and 20: "))
    if user_guess == answer:
        print("you got the number right.... bye")
        answer_guessed = True
    elif user_guess > answer:
        print("too high")
    elif user_guess < answer:
        print("too low")

# Expected Output:
# Guess the number: 7  
# Too low  
# Guess the number: 11  
# Too high  
# Guess the number: 9  
# Correct!
# (Your target number is 9. Don’t be weird and change it.)
