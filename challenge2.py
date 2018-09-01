
# ===============
# challenge2.py
# ===============

# =================================
# List comprehension challenge 2
# =================================



# In case it's not obvious, a list comprehension produces a list, but
# it doesn't have to be given a list to iterate over.
#
# You can use a list comprehension with any iterable type, so we'll
# write a comprehension to convert dimensions from inches to centimetres.
#
# Our dimensions will be represented by a tuple, for the length, width and height.
#
# There are 2.54 centimetres to 1 inch.
 
inch_measurement = (3, 8, 20)
 
cm_measurement = [inch * 2.54 for inch in inch_measurement]
print("cm_measurement list = {}".format(cm_measurement))
 
# Once you've got the correct values, change the code to produce a tuple, rather than a list.

# This is converting above cm_measurement to a tuple:
cm_measurement = tuple(cm_measurement)
print("cm_measurement tuple1 = {}".format(cm_measurement))


# This is converting directly from the list comprehension:
cm_measurement = tuple([inch * 2.54 for inch in inch_measurement])
print("cm_measurement tuple2 = {}".format(cm_measurement))