
# ===============
# filegen.py
# ===============

# ===============================================
# The OS.Walk Generator
# ===============================================

# We will continue our discussion of Generators.
# There is another way of using generators, called "Generator Expressions"
# But we will come back to that after seeing what "List Comprehensions" are

# ===============================================
# We are going to use the music database which contains 440 albums, by 203 artists and with over 5000 songs.
# We had python type all this information into the database and we will see how we did it.

# The source of this data was mp3 disk with the database
# We will look at how to work with the computer file system
# We download music.zip file provided and unzipped it into our 42_MusicFiles folder.

# NOTE that these are not real mp3 files because of copyright issues and they would be too large.
# Also NOTE that we have used extension "emp3" for the songs so that if your music player automatically picks
# up all mp3 files from the hard disk, it will not pick these ones up and mess up your music collection



# # ===============================
# # OS.Walk function
# # ===============================
#
# # So now we will look at how we can access computer files in a harddisk
# # We know that OS.walk function can be used to recursively retrieve the contents of a directory and subdirectories
# # We initially used OS.walk function to explain recursion
#
# # But we should know that OS.walk function is also a generator
# # so it does not build a huge list of all the files and directories in the harddrive, it just returns them as needed.
#
# # We will see how this works.
#
# # First we import OS module
#
# import os
#
# # We define the root level folder "music"
# # this is the relative path because we have the folder under 42_MusicFiles and we are running filegen.py from same folder 42_MusicFiles
# # NOTE: if music folder is stored somewhere else, you will have to provide an exact path to where they are.
#
# root = "music"
#
# # os.walk recursively visits every directory from the root, and for every one of them, it returns a tuple.
# # LINE_1:
# # path: - The first item of LINE_1 is a string containing the name of the "current directory" which we are unpacking into "path" in our code
# # directories: - next is a list of all directories in the current directory
# # files: - Then we have a list containing the names of all the files.
#
#
# for path, directories, files in os.walk(root, topdown=True):  # LINE_1
#     print("Path = {}".format(path))  # initial path is music, second interation is music\music, third is music\music\1000 Maniacs etc
#     print("Directories = {}".format(directories))  # initial directory is 'music', second is all under music\music etc
#     print("Files = {}".format(files))  # No files until 4th directory (e.g. Our Time in Eden, which has files)
#     print("="*20)
#
#     input("Press Enter:")  # Use this input to get output line by line
#
#     # Then we iterate through the files.
#     # NOTE: we can comment this out for testing
#     # for f in files:
#     #    print("\t{}".format(f))
#

# ======================

# Above code produces results like this for all Artists and albums.
# NOTE the songs are in alphabetical order but it considers the first number first. So 10 comes before 2
# NOTE that when it reaches the files and there are no more directories under that section, it backtracks one level up
# to go to the next directory and then loop through all of them like that


# Path = music
# Directories = ['music']
# Files = []
# ====================
# Path = music\music
# Directories = ['1000 Maniacs', 'Axel Rudi Pell', 'Bad Company', <<== truncated ==>, 'ZZ Top']
# Files = []
# ====================
# Path = music\music\1000 Maniacs
# Directories = ['Our Time in Eden']
# Files = []
# ====================
# Path = music\music\1000 Maniacs\Our Time in Eden
# Directories = []
# Files = ['1 - Candy Everybody Wants.emp3', "10 - Noah's Dove.emp3", '11 - Stockton Gala Days.emp3', '12 - These Are Days.emp3', '13 - # Tolerance.emp3', '2 - Circle Dream.emp3', '3 - Eden.emp3', '4 - Few And Far Between.emp3', '5 - Gold Rush Brides.emp3', "6 - How You've # Grown.emp3", '7 - If You Intend.emp3', "8 - I'm Not The Man.emp3", '9 - Jezebel.emp3']
# ====================
# 	1 - Candy Everybody Wants.emp3
# 	10 - Noah's Dove.emp3
# 	11 - Stockton Gala Days.emp3
# 	12 - These Are Days.emp3
# 	13 - Tolerance.emp3
# 	2 - Circle Dream.emp3
# 	3 - Eden.emp3
# 	4 - Few And Far Between.emp3
# 	5 - Gold Rush Brides.emp3
# 	6 - How You've Grown.emp3
# 	7 - If You Intend.emp3
# 	8 - I'm Not The Man.emp3
# 	9 - Jezebel.emp3
# Path = music\music\Axel Rudi Pell
# Directories = ['Between The Walls', 'Black Moon Pyramid', 'Diamonds Unlocked', 'Eternal Prisoner', 'Kings and Queens', 'Magic', 'Mystica', # 'Nasty Reputation', 'Oceans of time', 'Shadow Zone', 'Tales of the Crown', 'The Ballads IV', 'The Crest', 'The Masquerade Ball', 'Wild # Obsession']
# Files = []
# ====================
# Path = music\music\Axel Rudi Pell\Between The Walls
# Directories = []
# Files = ['1 - The Curse.emp3', '10 - Desert Fire.emp3', '2 - Talk Of The Guns.emp3', '3 - Warrior.emp3', '4 - Cry Of The Gypsy.emp3', '5 - # Casbah.emp3', '6 - Outlaw.emp3', '7 - Wishing Well.emp3', '8 - Innocent Child.emp3', '9 - Between The Walls.emp3']
# ====================
# 	1 - The Curse.emp3
# 	10 - Desert Fire.emp3
# 	2 - Talk Of The Guns.emp3
# 	3 - Warrior.emp3
# 	4 - Cry Of The Gypsy.emp3
# 	5 - Casbah.emp3
# 	6 - Outlaw.emp3
# 	7 - Wishing Well.emp3
# 	8 - Innocent Child.emp3
# 	9 - Between The Walls.emp3

# <<============ Truncated ============>



# # =====================================================
# # Here is above code without all the comments
# # =====================================================
#
# import os
#
# root = "music"
#
# for path, directories, files in os.walk(root, topdown=True):
#     print(path)
#     for f in files:
#         print("\t{}".format(f))







# =================================================================
# Using OS.Walk function to extract files and populate a database:
# =================================================================

# ========================
# Separating the album
# ========================

# As we saw above, the OS.walk function goes through the files and folders and yields the directories and files in them
# NOTE that when we reach a folder that has music files, it is able to extract them as files.
# And we can extract these files to populate a database

# The code for extacting the files is simple,
# but when dealing with file paths, don't be tempted to split the string at the slashes.
# This is because the OS module has a path module that knows about file names and can correctly parse them for us.


# import os
#
# root = "music"
#
# for path, directories, files in os.walk(root, topdown=True):
#     if files:
#         print("Path = {}".format(path))
#         # LINE_1 below shows os.path.split separates the last directory "Our Time in Eden" from the path
#         # "Our Time in Eden" is the last directory in the path. And first in the path to have files.
#         first_split = os.path.split(path)  # LINE_1:  Result ==> ('music\\music\\1000 Maniacs', 'Our Time in Eden')
#         print("first_split = {}".format(first_split))
#     else:
#         print("No files in: {}".format(path))
#         print("="*40)
#
#     input("Press Enter:")  # Use this input to get output line by line


# =====================================================================

# SPLIT_1 below separated the last directory from the path. This last directory is the album.
# Hence above code separated the Album ('Our Time in Eden') for us from the path.

# =========================
# Getting Artist name
# =========================

# SPLIT_2: If we repeat os.path.split(path) on the first element of the tuple, we can get access to the artist name.
# In the first iteration, we pass first object from first_split tuple ('music\\music\\1000 Maniacs') to second_split
# Second_split then splits it and separates artist 1000 Maniacs from the path as shown: ('music\\music', '1000 Maniacs')

import os

root = "music"

for path, directories, files in os.walk(root, topdown=True):
    if files:
        print("Path = {}".format(path))
        # SPLIT_1 below shows os.path.split separates the last directory "Our Time in Eden" from the path
        # "Our Time in Eden" is the last directory in the path. And first in the path to have files.
        first_split = os.path.split(path)  # LINE_1:  Result is tuple ==> ('music\\music\\1000 Maniacs', 'Our Time in Eden')
        print("first_split = {}".format(first_split))

        # SPLIT_2: Second_split is passed the first object of first_split, and then it splits it as shown
        second_split = os.path.split(first_split[0])  # Pass first object ('music\\music\\1000 Maniacs') which will then be split to separate 1000 Maniacs
        print("second_split = {}".format(second_split))  # Prints (('music\\music', '1000 Maniacs') => which separates 1000 Maniacs from path

        # SPLIT_3:
        # To get the list of songs, we can iterate over the files list
        # We already know that there are files in this directory because we checked using "if files" statement above.
        # So we can use normal string splitting to split the name from the song number.
        # For example, we have song "1 - Candy Everybody Wants.emp3" and we can split the songs name from the songs number 1
        # This code gives results: song_details = ['1', 'Candy Everybody Wants.emp3'],
        # It splits song number from Song name, but it includes file extension emp3. We will improve it below

        # for f in files:
        #     song_details = f.split(' - ')  # NOTE: we are splitting and removing this dash
        #     print("song_details = {}".format(song_details))

        # SPLIT_3 (improvement 1)
        # We also want to strip the file extension (emp3) using the "strip" keyword
        # So on line: f.strip('.emp3').split(' - '), we strip .emp3 and then split the result on the dash
        # First results ==> song_details = ['1', 'Candy Everybody Wants']
        # But also another result down the line ==> song_details = ['', 'Eden'], original was: song_details = ['3', 'Eden.emp3']
        # In this case, it removed the number 3

        # Reason for this is because "strip" works for a "sequence" and Not a "string"
        # So it does not actually remove the string (.emp3), but it checks the beginning and end of file name for any of the characters
        # in .emp3 and keeps removing them regardless of order until it cannot remove them anymore.
        # So if you look through the result, if any one starts or ends with any letters in .emp3, they will be removed.

        # for f in files:
        #     song_details = f.strip('.emp3').split(' - ')  # Removes any beginning/ending letter in .emp3: Results ==> song_details = ['', 'Eden']
        #     print("song_details = {}".format(song_details))



        # SPLIT_3 (improvement 2 (final improvement)
        # To deal with above issue, we can SLICE the string before SPLITTING it.
        # We want everything except the last five characters i.e. ".emp3"
        # f[:-5] is split where we don't give start point, hence it defaults from beginning of string
        # and then -5 means we remove the last 5 characters
        # The results here are what we expect. It removes the last 5 characters (.emp3)


        for f in files:
            song_details = f[:-5].split(' - ')  # Results ==> song_details = ['3', 'Eden']
            print("song_details = {}".format(song_details))
    else:
        print("No files in: {}".format(path))
        print("="*40)

    input("Press Enter:")  # Use this input to get output line by line

# =============================

# So the output above gives us all the data we need and we can use it in
# SQL Insert statements to write the data to a database.
# This is how the music.db was created. By pulling the information from a real CD, and then stripping the mp3 extension

# ============================
# OS.walk as a Generator
# ============================

# We can see that os.walk is a generator
# It does not try to read every single file at once into a huge list,
# but it only yields details for a single directory at a time.
# Hence we can process millions of albums like this without running out of memory.

# Generators can be more useful if we start using them to create other generators
# We will start working on that in the next section.