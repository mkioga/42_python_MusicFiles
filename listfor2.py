
# ===============
# listfor2.py
# ===============

# =======================================================
# List comprehensions and side effects (using for loop)
# =======================================================

# NOTE: This is for python3 only. Will not work with python2

# ================================================
# Differences between comprehensions and for loop
# ================================================
# One difference is that comprehensions don't have the same side effect that you can have with a for loop.


# ================================
# Side Effect of bug in for loop
# ===============================

# In this program, we have a list of numbers. LINE_1
# we are trying to input a Number (LINE_2) and then use that number to check if it exist in LINE_1
# Then get its number from its index
# Then square that number and display it.

# From the results below, we realize that the number we input in LINE_2,
# even if its being stored in a variable named "number", is actually not being used to loop through the numbers (LINE_1)
# The loop is starting from the beginning to the end and eventually gives final index position as 5 (last one, beginning from 0)

# The reason for this bug or side effect is because the variable number is also used as the loop control variable
# That is "number" in LINE_1 and "number" in LINE_3
# So when the for loop terminates, "number" has the value of the last item in numbers i.e. 7

# This side effect does not happen if you use "list comprehensions" (See listcomp2.py)


print(__file__)

numbers = [2, 3, 4, 5, 6, 7]   # LINE_1

number = int(input("Please Enter a Number: "))   # LINE_2
print("="*20)

squares = []
for number in numbers:   # LINE_3
    print("Initial squares List = {}".format(squares))
    print("Number = {}".format(number))
    print("Numbers Index Position = {}".format(numbers.index(number)))
    squares.append(number ** 2)
    print("New Squares List = {}".format(squares))
    print("="*20)


index_position = numbers.index(number)
print("Final Index Position = {}".format(index_position))
print("Final Squares List = {}".format(squares))
print("Square of Final Index Position = {}".format(squares[index_position]))

# Results from code above:

# C:/Users/moe/Documents/Python/IdeaProjects/42_MusicFiles/listfor2.py
# Please Enter a Number: 4
# ====================
# Initial squares List = []
# Number = 2
# Numbers Index Position = 0
# New Squares List = [4]
# ====================
# Initial squares List = [4]
# Number = 3
# Numbers Index Position = 1
# New Squares List = [4, 9]
# ====================
# Initial squares List = [4, 9]
# Number = 4
# Numbers Index Position = 2
# New Squares List = [4, 9, 16]
# ====================
# Initial squares List = [4, 9, 16]
# Number = 5
# Numbers Index Position = 3
# New Squares List = [4, 9, 16, 25]
# ====================
# Initial squares List = [4, 9, 16, 25]
# Number = 6
# Numbers Index Position = 4
# New Squares List = [4, 9, 16, 25, 36]
# ====================
# Initial squares List = [4, 9, 16, 25, 36]
# Number = 7
# Numbers Index Position = 5
# New Squares List = [4, 9, 16, 25, 36, 49]
# ====================
# Final Index Position = 5
# Final Squares List = [4, 9, 16, 25, 36, 49]
# Square of Final Index Position = 49
