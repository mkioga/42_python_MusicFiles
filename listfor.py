
# =================
# listfor.py
# =================

# ==============================
# List Comprehensions
# ==============================

# Python has comprehensions for lists, sets and Dicts (dictionaries)
# It also has generator expressions that are very similar to write.

# We will start with "list comprehensions" and then later show how "set and dict comprehensions" work in the same way.

# This is to print the complete file path so as to show you which program is running.
# Its result look like this. We know we are running listfor.py
# C:/Users/moe/Documents/Python/IdeaProjects/42_MusicFiles/listfor.py

print(__file__)

# Now we will make a program to print out the squares in a list (numbers)

numbers = [1, 2, 3, 4, 5, 6]  # list of numbers

# SQUARES SECTION
squares = []  # Initialize squares with empty list
for number in numbers:
    squares.append(number ** 2)   # append squares of the numbers in numbers list

print(squares)  # Print squares.

# Result for above code will be:

# C:/Users/moe/Documents/Python/IdeaProjects/42_MusicFiles/listfor.py
# [1, 4, 9, 16, 25, 36]

# ==================================================
# We can write above code using list comprehension
# We will do it in listcomp.py

# Note we can view the two programs at the same time using split screen on intellij
# Right Click listfor.py on this pane > Choose "Split Vertically"
# This will produce two screens which you can view at the same time

# So we will create a new file called listcomp.py
# NOTE: Make sure to click on listfor.py so that listcomp.py will be created on the left of the screen

