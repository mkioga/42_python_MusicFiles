
# =======================
# listcomp2.py
# =======================

# ============================================================================
# List comprehensions and side effects (Fixed using for list comprehension)
# ============================================================================

# Using comprehensions in listcomp2.py produces the expected results.
# When you enter a number, it gives you the index position and squares it as expected

# =============
# explanation
# =============

# list comprehension treats the "number" just like a loop control variable in languages like C or Java
# There is no side effect and the value of any existing variable with the same name is not modified

# So this is a good reason to use a list comprehension rather than a for loop
# list comprehension give more precise code and gives more protections from bugs like this one in for loop (listfor2.py)

# NOTE: that python2 does leak the loop control variable and it is available in the outer scope
# and would replace the value of any variable with the same name.
# This was fixed in python3 (as you can see here) and you can see that in Guido Van Rossum's comments (python creator) here:
# http://python-history.blogspot.com/2010/06/from-list-comprehensions-to-generator.html




print(__file__)

numbers = [2, 3, 4, 5, 6, 7]

number = int(input("Please Enter a Number: "))
print("="*20)

squares = [number ** 2 for number in numbers]

index_position = numbers.index(number)
print("Final Index Position = {}".format(index_position))
print("Final Squares List = {}".format(squares))
print("Square of Final Index Position = {}".format(squares[index_position]))

# Result for above code.

# C:/Users/moe/Documents/Python/IdeaProjects/42_MusicFiles/listcomp2.py
# Please Enter a Number: 2
# ====================
# Final Index Position = 0
# Final Squares List = [4, 9, 16, 25, 36, 49]
# Square of Final Index Position = 4

# C:/Users/moe/Documents/Python/IdeaProjects/42_MusicFiles/listcomp2.py
# Please Enter a Number: 3
# ====================
# Final Index Position = 1
# Final Squares List = [4, 9, 16, 25, 36, 49]
# Square of Final Index Position = 9


# C:/Users/moe/Documents/Python/IdeaProjects/42_MusicFiles/listcomp2.py
# Please Enter a Number: 4
# ====================
# Final Index Position = 2
# Final Squares List = [4, 9, 16, 25, 36, 49]
# Square of Final Index Position = 16
