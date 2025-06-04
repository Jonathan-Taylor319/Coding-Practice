# word frequency word counter   

text = "I love Python because I love solving problems with Python"

# need a function
    #create an empty dictionary
    #we need to loop through the str.split()
        #make sure to fill our dictionary
    #return our dictionary

def word_counter(text):
    words_counted = {}
    for word in text.split():
        words_counted[word] = words_counted.get(word, 0) +1 
    return words_counted

print(word_counter(text))

# find the most frequent number 

nums = [3, 5, 2, 3, 8, 3, 2, 5, 2]

def top_num_counter(num):
    numbers_found = {}
    for numbers in num:
        numbers_found[numbers] = numbers_found.get(numbers, 0) +1
    #new var to hold most common = highest(dictionary, key=[dictionary info we want].get)
    most_common = max(numbers_found, key=numbers_found.get)
    return most_common

print(top_num_counter(nums))


# reverse the sentence 

sentence = "Python makes me feel powerful"

def sent_reversed(words):
    #forgot if i can slice or i can just split.reverse.join
    word_list = words.split()
    word_list.reverse()
    return ' '.join(word_list)

print(sent_reversed(sentence))


    