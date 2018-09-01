
# =============
# listcomp.py
# =============

# Now we write code to do squares but using list comprehensions

print(__file__)

numbers = [1, 2, 3, 4, 5, 6]  # list of numbers

# Does same thing as SQUARES SECTION in listfor
# We can see that using list comprehensions takes less code than using for loop
# NOTE: We know this is a list comprehension because it is enclosed in [ ]

# Definition of list comprehensions:

# This list comprehension is in two parts.
# Part1: is the expression ( number ** 2 ) that we want to return.

# Part2: is an iteration over a sequence (for number in numbers).
# It is identical to the "for" part of our "for loop" except we don't need a colon at the end.

# NOTE: There is more to comprehensions and we will extend that definition later.

squares = [number **2 for number in numbers]  # Does same thing as SQUARES SECTION in listfor

print(squares)

# When you print this, it gives results:
# Notice it shows you we are running listcomp.py
# And it has same results for squares.

# C:/Users/moe/Documents/Python/IdeaProjects/42_MusicFiles/listcomp.py
# [1, 4, 9, 16, 25, 36]




# ============================================

# A list comprehension produces a list.
# It does that by evaluating the expression (Part1) for each item in the iterable (Part2)
# We can use anything that can be iterated over in the iterable (Part2) e.g. string, generator, range etc

print(__file__)

numbers = [1, 2, 3, 4, 5, 6]  # list of numbers

# squares = [number **2 for number in numbers]  # comment this out and replace iterable (Part2) with Range
squares = [number **2 for number in range(1, 7)]  # Using a range in iterable

print(squares)

# Result for this is:

# C:/Users/moe/Documents/Python/IdeaProjects/42_MusicFiles/listcomp.py
# [1, 4, 9, 16, 25, 36]


# =========================================
# Examples of list comprehensions
# =========================================

text = "what have the romans done for us"

# Using list comprehension to convert all characters in text to caps

capitals = [char.upper() for char in text]
print(capitals)

# This gives results:
# ['W', 'H', 'A', 'T', ' ', 'H', 'A', 'V', 'E', ' ', 'T', 'H', 'E', ' ', 'R', 'O', 'M', 'A', 'N', 'S', ' ', 'D', 'O', 'N', 'E', ' ', 'F', 'O', 'R', ' ', 'U', 'S']

# ====================================
# Using list comprehensions to convert all words in text to caps

words = [word.upper() for word in text.split(' ')]  # We split text by space to get the words
print(words)

# This gives results:
# ['WHAT', 'HAVE', 'THE', 'ROMANS', 'DONE', 'FOR', 'US']

# ==========================================
# Using list comprehension to print words in text unchanged (in lower case)

lc_words = [word for word in text.split(' ')]  # We just pull the iterable (part2) but have no expression(part1) because we are not changing anything
print(lc_words)

# This gives results:
# ['what', 'have', 'the', 'romans', 'done', 'for', 'us']

# NOTE: that above (lc_words) is not a good use of list comprehension because there is easier way of writing the words in lower case
# As shown below.

lc_words2 = text.split(' ')
print(lc_words2)

# This gives result:
# ['what', 'have', 'the', 'romans', 'done', 'for', 'us']


# ============================================================================
# We will see when list comprehensions are sometimes preferable to for loops
# we will do this in centre_text.py
# ============================================================================




# ========================
# Set Comprehension (brief example)
# ========================

# If we change the [ ] in squares and replace it with { }, we get results of a set.
# List comprehensions produce a list, while set comprehension produces a set.

print(__file__)

numbers = [1, 2, 3, 4, 5, 6]  # list of numbers

squares = { number **2 for number in numbers }  # Enclose in { } to produce a set comprehension ==> {1, 4, 36, 9, 16, 25}

print(squares)


# Gives result:

# C:/Users/moe/Documents/Python/IdeaProjects/42_MusicFiles/listcomp.py
# {1, 4, 36, 9, 16, 25}




