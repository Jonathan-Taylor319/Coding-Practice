# #looping in pairs triples etc.....

# numbers = [1, 2, 3, 4, 5]
# #we want pairs : [1,2], [2,3], [3,4], [4,5]
# #pairs need 2 elements, so stop at len(numbers) -1
# for i in range(len(numbers) - 1):
#     print("Pair:", numbers[i], numbers[i+1])

# numbers_1 = [4, 8, 1, 9, 0, 2, 4, 3]

# for i in range(len(numbers_1) - 1):
#     print("number 1 Pairs: ", numbers_1[i], numbers_1[i+1])
#     print(numbers_1[i] > numbers_1[i+1])

# number_list = [2, 4, 6, 7, 8, 2, 3, 5, 6, 1, 4]
# #again.....for value in the whole list always leave room for one
# for i in range(len(number_list) -1 ):
#     print(number_list[i], number_list[i +1])

# new_nums = [2, 3, 46, 80, 25, 16, 300, 425]

# for i in range(len(new_nums) -1):
#     print("new_nums pairs are....: ", new_nums[i], new_nums[i+1])
#     # i could only add new_nums_[i+2] if i save space for 2 at the end? 