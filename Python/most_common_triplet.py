# 🧠 REAL ASSESSMENT-STYLE CHALLENGE: “Most Common Triplet”
# ❓ Prompt:
# You are given a list of strings representing user-submitted search queries.
# Each query is a single word. You must analyze all groups of 3 consecutive queries (triplets) and identify the most commonly occurring triplet.
# Your task:
# Write a function that scans through the list and tracks how often each triplet appears.
# Return the triplet that appeared most frequently, and how many times it appeared.

# # ("cat", "dog", "fish")  ➜ 3

# 💥 Requirements:
# Use .get() to track counts (no defaultdict, no Counter)
# Use range() smartly to avoid index errors
# Return the most common triplet and how many times it appeared
# Do not use fancy imports — built-in Python only


queries = [
    "cat", "dog", "fish",
    "cat", "dog", "fish",
    "dog", "cat", "fish",
    "cat", "dog", "fish"
]

def triple_chaser(i):
    #we want to unpack in groups of 3 to track each set.....and im assuimg we want a dict
    triple_sequence = {}
    #we need to polulate our dict, but in groups of 3.....
    for b in range(len(i) -2):
        pattern = (i[b], i[b+1], i[b+2])
        

triple_chaser(queries)


