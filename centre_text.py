
# ===================
# centre_text.py
# ===================

# ===============================
# list comprehension - continued
# ===============================

# We are now going to see when list comprehensions can be preferable to a for loop
# Back in section 11, we created a function to center text on a display
# We have pasted the code here.
# When we run this program, it centers the text. See results below.

# In this program, we are concantenating strings inside a for loop (LINE_3 and LINE_4)
# This is not a good idea if it can be avoided and it also has an effect that we don't want.
# See next section for the undesirable effect

def centre_text(*args):
    text = ""
    for arg in args:            # LINE_3
        text += str(arg) + " "  # LINE_4
    left_margin = (80 - len(text)) // 2
    print(" " * left_margin, text)


# call the function
centre_text("spam and eggs")
centre_text("spam, spam and eggs")
centre_text(12)
centre_text("spam, spam, spam and spam")

centre_text("first", "second", 3, 4, "spam")

# Results for above program shows all centered:

#                   spam and eggs
#                spam, spam and eggs
#                        12
#             spam, spam, spam and spam
#               first second 3 4 spam




# ===========================================


# ===============================
# list comprehension - continued
# ===============================

# We can demonstrate the undesirable effect by adding a "-" instead of " " on LINE_4
# From the result below, we see that the - is added at the end of the string, not just between the items in the list
# An example of where this is a disadvantage is if you are searching for strings ending with "spam",
# you will not find any because the strings will end with "spam " (spam and space) if we remained with " "

# We can fix this by using "join" rather than a "for loop"
# We will do this in next section


def centre_text(*args):
    text = ""
    for arg in args:            # LINE_3
        text += str(arg) + "-"  # LINE_4
    left_margin = (80 - len(text)) // 2
    print(" " * left_margin, text)


# call the function
centre_text("spam and eggs")
centre_text("spam, spam and eggs")
centre_text(12)
centre_text("spam, spam, spam and spam")

centre_text("first", "second", 3, 4, "spam")

# Results for above program shows all centered:

#                   spam and eggs-
#                spam, spam and eggs-
#                        12-
#             spam, spam, spam and spam-
#               first-second-3-4-spam-





# =====================================================
# list comprehension - using join instead of for loop
# =====================================================

# We can fix above issue by using "join" rather than a "for loop"


def centre_text(*args):
    # We comment these lines out:
    # text = ""
    # for arg in args:            # LINE_3
    #     text += str(arg) + "-"  # LINE_4

    text = "-".join(args)    # Joins the arguments given (ones separated by "argument") and separates them by -
    left_margin = (80 - len(text)) // 2
    print(" " * left_margin, text)

# call the function
centre_text("spam and eggs")
centre_text("spam, spam and eggs")
# centre_text(12)  # comment this out because you cannot join int to strings
centre_text("spam, spam, spam and spam")

# centre_text("first", "second", 3, 4, "spam")  # Comment this out because it has 3, 4 ints. Cannot join ints to strings

# Results for above program shows all centered and with no - :
# This is because all these three lines have one argument, under one set of " ", hence not being joined to anything.

#                   spam and eggs
#                spam, spam and eggs
#             spam, spam, spam and spam


# ==================================================================
# using list comprehension to accomodate both strings and integers
# ==================================================================

# Now we will modify the join to be able to join with the integers
# LINE_1: To accomodate both strings and integers, we use a list comprehension to:
# First: Loop through every arg in args
# Second: convert that arg to string
# Third: use that string to join to the next with - as a separator


def centre_text(*args):
    text = "-".join([str(arg) for arg in args])    # LINE_1
    left_margin = (80 - len(text)) // 2
    print(" " * left_margin, text)

# call the function
centre_text("spam and eggs")
centre_text("spam, spam and eggs")
centre_text(12)  # int
centre_text("spam, spam, spam and spam")
centre_text("first", "second", 3, 4, "spam")  # Has strings and ints

# We get results below which accomodates both strings and integers
# It also gets every argument passed (between " ") with and separates it with a -

#               spam and eggs
#            spam, spam and eggs
#                    12
#         spam, spam, spam and spam
#           first-second-3-4-spam



# ====================================
# Generator Expression (introduction)
# ====================================

# If you remove the [ ] in LINE_1, you get the same results as one above for list comprehension
# But this (without [ ] ) is not a list comprehension, it is a "Generator Expression"
# We will learn more above Generator Expressions later.


def centre_text(*args):
    text = "-".join(str(arg) for arg in args)    # LINE_1
    left_margin = (80 - len(text)) // 2
    print(" " * left_margin, text)

# call the function
centre_text("spam and eggs")
centre_text("spam, spam and eggs")
centre_text(12)  # int
centre_text("spam, spam, spam and spam")
centre_text("first", "second", 3, 4, "spam")  # Has strings and ints

# We get results below which accomodates both strings and integers
# It also gets every argument passed (between " ") with and separates it with a -

#               spam and eggs
#            spam, spam and eggs
#                    12
#         spam, spam, spam and spam
#           first-second-3-4-spam

