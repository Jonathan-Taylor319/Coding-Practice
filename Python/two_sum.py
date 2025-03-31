# Problem 1: Two Sum
# Description: Given an array of integers and a target value, return the indices of the two numbers that add up to the target.

# Example:

# Input: nums = [2, 7, 11, 15], target = 9

# Output: [0, 1] (because nums[0] + nums[1] = 2 + 7 = 9)

# Hint: Use a hash map (or dictionary) to store elements and check for the complement value.

                                
# def two_sum(arr, total):
    # need to return the indices of numbers that equal the output
    # for num in arr:
        #need to loop and try to see if numbers = target
        # if num[i] + num[i+1] == total
        # return num.index[i] and num.index[i+1]
    


#learning notes / thoughts / etc

# for i in range(len(arr)):
# len(arr) - this returns the number of elements in the list arr
# range(len(arr)) - this created an iterable sequence of numbers starting at 0 if (if array has 5 numbers will show 4 indecies......starts with 0)
# for i in range(len(arr)) - the loop iterates over this sequence, assigning each number to the var i one by one - i represents current index
# access elements = you can access the element at index at index i by using arr[i]

#------EXAMPLE---------
# arr = [10, 20, 30, 40, 50]
# for i in range(len(arr)):
#     print("Index:", i, "Value:", arr[i])

#prints 
# Index: 0 Value: 10
# Index: 1 Value: 20
# Index: 2 Value: 30
# Index: 3 Value: 40
# Index: 4 Value: 50


# def two_sum(arr, total):
#     #this will associate the index as key value pair and loop through
#     for i in range(len(arr)):
#         #for each elemen in an the array, check every other element to see if their sum = the total
#         #for now try nesting and looping inside to compare?
#         #we declar another var to check - and we add it to i
#         for j in range(i+1, len(arr)):
#             if i + j == total:
#                 #return the index of the items in their array?
#                 return index(arr[i], Arr[j])

def two_sums(arr, total):
    #make a key value pair index/value / loop through
    for i in range(len(arr)):
        #loop through and add if elements equal the total
        for j in range(i+1, len(arr)):
            #compare the value of said elements
            if arr[i] + arr[j] == total:
                #return the indice of the 2 that make up the total
                return (i, j)

print(two_sums([1,4,6,8], 10))
print(two_sums([15, 3, 0, 6, 4, 1, 15], 30))


# refactored code using a hash map

def two_sum(arr, total):
    # create an empty dictionary to store numbers we've seen as keys,
    #with their indices as values
    hash_map = {}

    #loop over each element in the array
    for i in range(len(arr)):
        #calculate the complement: the number i need to add to arr[i]
        complement = total - arr[i]

        #check if this complement exists in our dictionary(hashmap)
        if complement in hash_map:
            #if found, return the indices
            #stored and current index
            return (hash_map[complement], i)

        #if not found, add the current number and it's index to dictionary
        hash_map[arr[i]] = i

    #if no valide pair is found, return none
    return None

print(two_sum([1,4,6,8], 10))
print(two_sum([15, 3, 0, 6, 4, 1, 15], 30))

# top answer compared to lower answer 

# Efficiency:
# Instead of using two nested loops (which gives O(n²) time), this approach uses one loop and dictionary lookups, 
# which are O(1) on average. Overall, this makes the solution O(n).

# In Python, a dictionary is implemented as a hash map. In other words, they refer to the same underlying data structure:

# Dictionary: This is the built-in data type in Python that lets you store key-value pairs. You create one using curly braces (e.g., {}) or the dict() constructor.

# Hash Map: This term describes a data structure that uses a hash function to map keys to values for fast lookups. In Python, the dictionary is implemented as a hash map, so when you're using a dictionary, you're already using a hash map.

# So, when the code example uses a dictionary to store values and their indices, it's using a hash map. The terms are often used interchangeably in Python.

# Think of it this way:

# When you're creating a dictionary, you're setting up a hash map.

# When you store key-value pairs in it, you're populating the hash map.

# When you look up a key, you're taking advantage of the hash map's fast access properties.

# This means your two-sum solution that uses a dictionary is effectively using a hash map to optimize the lookup process.