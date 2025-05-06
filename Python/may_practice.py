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

nums = [11, 22, 33, 44, 55, 66]
every_other = nums[::2]
print(every_other)