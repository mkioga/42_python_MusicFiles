
# ===============
# challenge1.py
# ===============

# ========================================
# Converting a for loop to Comprehension:
# ========================================


# Rewrite the following code to use a list comprehension, instead of a for loop.
#
# Add your solution below the loop, so that the resulting list is printed out
# below output - that makes it easier to check that it's producing exactly
# the same list (and avoids entering the input text twice).

text = input("Please enter your text: ")

# Original solution to get word length using "for loop":

output = []
for x in text.split():
    output.append(len(x))
print("Length using For loop = {}".format(output))
print("="*20)

# New Solution to get word length using list comprehension:
# NOTE that "split" is able to split words if they are separated by a space

answer = [len(x) for x in text.split()]
print("Length using Comprehension = {}".format(answer))
print("="*20)

# It could be useful to store the original words in the list, as well.
# The for loop would look like this (note the extra parentheses, so
# that we get tuples in the list):

# Original solution to get word and word length using "for loop":

output = []
for x in text.split():
    output.append((x, len(x)))
print("Word & Lenth using for loop = {}".format(output))
print("="*20)

# New Solution to get word and word length using "list comprehension":

answer = [(x, len(x)) for x in text.split()]
print("Word & Length using comprehension = {}".format(answer))
print("="*20)


# Here is the result:

# C:\Users\moe\AppData\Local\Programs\Python\Python36-32\python.exe C:/Users/moe/Documents/Python/IdeaProjects/42_MusicFiles/challenge1.py
# Please enter your text: Input text contains text and integers and another text
# Length using For loop = [5, 4, 8, 4, 3, 8, 3, 7, 4]
# ====================
# Length using Comprehension = [5, 4, 8, 4, 3, 8, 3, 7, 4]
# ====================
# Word & Lenth using for loop = [('Input', 5), ('text', 4), ('contains', 8), ('text', 4), ('and', 3), ('integers', 8), ('and', 3), ('another', 7), ('text', 4)]
# ====================
# Word & Length using comprehension = [('Input', 5), ('text', 4), ('contains', 8), ('text', 4), ('and', 3), ('integers', 8), ('and', 3), ('another', 7), ('text', 4)]
# ====================




# ================================================================
# Converting for loop to "set comprehension" to avoid duplicates:
# ================================================================

# In above code, our input text had the word "text" three times and word "and" two times. And they were all counted.
# If you want to show unique words e.g. you only want to show word "text" only once even if it appears three times
# We will need to use "set comprehensions" ( enclosed in { } ) instead of "list comprehensions" (enclosed in [ ] )
# We changed the code on LINE_1 and LINE_2


text = input("Please enter your text: ")

# Original solution to get word length using "for loop":

output = []
for x in text.split():
    output.append(len(x))
print("Length using For loop = {}".format(output))
print("="*20)

# New Solution to get word length using list comprehension:

answer = { len(x) for x in text.split() }  # LINE_1: Replaced [] with {} to make it a set comprehension instead of list comprehension
print("Length using Comprehension = {}".format(answer))
print("="*20)

# ===============================================================
# Original solution to get word and word length using "for loop":

output = []
for x in text.split():
    output.append((x, len(x)))
print("Word & Lenth using for loop = {}".format(output))
print("="*20)

# New Solution to get word and word length using list comprehension:

answer = { (x, len(x)) for x in text.split() }   # LINE_1: Replaced [] with {} to make it a set comprehension instead of list comprehension
print("Word & Length using comprehension = {}".format(answer))
print("="*20)


# Here is the result:
# In this case, the "set comprehension" results are not in order.
# And they also count the repeating words (text & and) only once each.


# C:\Users\moe\AppData\Local\Programs\Python\Python36-32\python.exe C:/Users/moe/Documents/Python/IdeaProjects/42_MusicFiles/challenge1.py
# Please enter your text: input text contains text and integers and another text
# Length using For loop = [5, 4, 8, 4, 3, 8, 3, 7, 4]
# ====================
# Length using Comprehension = {3, 4, 5, 7, 8}
# ====================
# Word & Lenth using for loop = [('input', 5), ('text', 4), ('contains', 8), ('text', 4), ('and', 3), ('integers', 8), ('and', 3), ('another', 7), ('text', 4)]
# ====================
# Word & Length using comprehension = {('text', 4), ('integers', 8), ('input', 5), ('contains', 8), ('and', 3), ('another', 7)}
# ====================




# ===========================================
# Using "Nested comprehensions"
# ===========================================

# If we run above code and input text:  mike, is not, good
# it will work, but will give length of word "mike" to be 5 (instead of 4) and word "not" to be length 4 (instead of 3)
# This is because "split" works only when splitting words that are separated by a space.

# We will resolve this later when we look at "nesting comprehensions" later on.

text = input("Please enter your text: ")

# Original solution to get word length using "for loop":

output = []
for x in text.split():
    output.append(len(x))
print("Length using For loop = {}".format(output))
print("="*20)

# New Solution to get word length using list comprehension:

answer = { len(x) for x in text.split() }  # LINE_1: Replaced [] with {} to make it a set comprehension instead of list comprehension
print("Length using Comprehension = {}".format(answer))
print("="*20)

# ===============================================================
# Original solution to get word and word length using "for loop":

output = []
for x in text.split():
    output.append((x, len(x)))
print("Word & Lenth using for loop = {}".format(output))
print("="*20)

# New Solution to get word and word length using list comprehension:

answer = { (x, len(x)) for x in text.split() }   # LINE_1: Replaced [] with {} to make it a set comprehension instead of list comprehension
print("Word & Length using comprehension = {}".format(answer))
print("="*20)


# Here is the result:

# Please enter your text: mike, is not, good
# Length using For loop = [5, 2, 4, 4]
# ====================
# Length using Comprehension = {2, 4, 5}
# ====================
# Word & Lenth using for loop = [('mike,', 5), ('is', 2), ('not,', 4), ('good', 4)]
# ====================
# Word & Length using comprehension = {('good', 4), ('is', 2), ('not,', 4), ('mike,', 5)}
# ====================
