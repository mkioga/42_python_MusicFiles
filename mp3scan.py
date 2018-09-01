
# =============
# mp3scan.py
# =============

# =======================
# Reading emp3 tags
# =======================

# One problem with the previous code was that relied on the files and directory names,
# is that you may not have such a neatly organized file structure.
# if you get your music from different sources, your filenames may not use the same pattern

# ===========
# Challenge:
# ===========

# In this code, we will read the ID3 tags from the emp3 files in the disk
# To do that, we will need a generator that will return the full path and name of each emp3 file

# So we need to create a generator that will return the complete filename of all emp3 files
# The generator should start at a specified directory, and the start will be provided as an argument to the generator function
# The filenames should include the full path from the specified start directory.
# So it will return a relative path

# We should make our generator function more generic so that it can handle files with any extension (not just emp3)
# So we will need to pass the extension as a second parameter to the function.

# We could also make the paths absolute. So they specify the filename from the root of the drive or volume.
# Check out the documentation of OS module for more info on absolute paths.

# we will use the music directory we have here and search for emp3 files


# =====================================
# Solution: - Getting relative path:
# =====================================

# We will use the os.walk generator to walk the directories from "start" provided
# Then we will filter the files that match the extension.

# LINE_3: We filter using '*.{}' and pass it extension (emp3 in this case)
# so it grabs every file with extension emp3

# This code returns all emp3 filenames starting from the start point (music) hence gives relative path starting from music.
# If we want absolute paths, we will use os.path.abs path function. See next section

import os
import fnmatch

def find_music(start, extension):
    for path, directories, files in os.walk(start):
        for file in fnmatch.filter(files, '*.{}'.format(extension)):  # LINE_3
            yield os.path.join(path, file)

for f in find_music('music', 'emp3'):
    print(f)

# When you run above command, you get results showing relative path from start point, music:

# music\music\1000 Maniacs\Our Time in Eden\1 - Candy Everybody Wants.emp3
# music\music\1000 Maniacs\Our Time in Eden\10 - Noah's Dove.emp3
# music\music\1000 Maniacs\Our Time in Eden\11 - Stockton Gala Days.emp3
# music\music\1000 Maniacs\Our Time in Eden\12 - These Are Days.emp3
# << ====== truncated =====>>




# =====================================
# Solution: - Getting absolute path:
# =====================================

# If we want absolute paths, we will use os.path.abs path function on LINE_4 below.
# Then on LINE_5, we will use absolute_path instead of path.
# The results after running this code will produce absolute path

import os
import fnmatch

def find_music(start, extension):
    for path, directories, files in os.walk(start):
        for file in fnmatch.filter(files, '*.{}'.format(extension)):  # LINE_3
            absolute_path = os.path.abspath(path)   # LINE_4: Creating absolute path
            # yield os.path.join(path, file)
            yield os.path.join(absolute_path, file)  # LINE_5: We use absolute_path in yielded values instead of path

for f in find_music('music2', 'mp3'):
    print(f)

# NOTE: In above for loop looped through the function.
# Another way to do it is

my_music_files = find_music('music', 'emp3')

for f in my_music_files:
    print(f)




# When you run above command, you get results with absolute path:

# C:\Users\moe\Documents\Python\IdeaProjects\42_MusicFiles\music\music\1000 Maniacs\Our Time in Eden\1 - Candy Everybody Wants.emp3
# C:\Users\moe\Documents\Python\IdeaProjects\42_MusicFiles\music\music\1000 Maniacs\Our Time in Eden\10 - Noah's Dove.emp3
# C:\Users\moe\Documents\Python\IdeaProjects\42_MusicFiles\music\music\1000 Maniacs\Our Time in Eden\11 - Stockton Gala Days.emp3
# C:\Users\moe\Documents\Python\IdeaProjects\42_MusicFiles\music\music\1000 Maniacs\Our Time in Eden\12 - These Are Days.emp3
# <<============== truncated =============>>



# =========================
# Tags and music files
# =========================

# tags in music files are how music players are able to display a song title or even an image of the album cover.
# There is a standard detail of the id3 tags used in mp3 files. See this link
# http://id3.org/

# This website contains everything you need if you want to write your own tags.

# =============
# Binary data
# =============

# We will not dwell a lot into binary format of mmp3 files,
# but we need to know why we need to read and write binary data in python.

# Reading the id3 tags from the music files is one example where we need to read binary data
# If any of your music files are missing some tags such as artist or subtitle, then we could use the earlier
# technique and attempt to work out the correct values from the file names.
# your program could then write the tags back to the files with the correct files added.

# Working with binary file format with only three tags is difficult, but Ned Batchelder has created a python2 module
# That does a good job of reading most common tags
# https://nedbatchelder.com/
# https://nedbatchelder.com/code/modules/id3reader.html

# There are other python libraries and most will let you write and read tags
# for Neds tag, we only read mp3 file tags hence there is no chance of writing into and destroying them.
# if you are using python2.7, you can download  id3reader.py file from this page and copy it into your project directory.
# https://nedbatchelder.com/code/modules/id3reader.html

# unfortunately, this  id3reader.py does not work with python 3
# so Trainer has produced a python3 version from Ned's original code.
# Its named: id3reader_p3.py and you can download it from the resources section of this video

# =================
# Using id3reader_p3
# =================

# Using the id3reader module is easy, you just need to create a new object and provide it with a path to an mp3 file.
# we have to import id3reader_p3 module first

# We will create a new object and provide it with a path to mp3 file
# Here the generator takes care of getting the file names for us and then we can focus on using the id3reader
# module to read the tag information

# NOTE: we will get an error when we run this code because we are pointing it to "emp3" file instead of "mp3" file
# "emp3 files we are using here are just text and don't contain any tag information which the id3 reader is looking for.
# Error message: OSError: [Errno 22] Invalid argument

# We will see how to fix that in the next section

import os
import fnmatch

import id3reader_p3 as id3reader   # CHANGE_1: import id3reader


def find_music(start, extension):
    for path, directories, files in os.walk(start):
        for file in fnmatch.filter(files, '*.{}'.format(extension)):  # LINE_3
            absolute_path = os.path.abspath(path)   # LINE_4: Creating absolute path
            # yield os.path.join(path, file)
            yield os.path.join(absolute_path, file)  # LINE_5: We use absolute_path in yielded values instead of path

# CHANGE_2: We make changes to print here to use id3reader

my_music_files = find_music('music', 'emp3')

for f in my_music_files:
    id3r = id3reader.Reader(f)
    print("Artist: {}, Album: {}, Track: {}, Song: {}".format(
        id3r.get_value('performer'),
        id3r.get_value('album'),
        id3r.get_value('track'),
        id3r.get_value('title')
    ))




# ======================================
# How to handle above error gracefully
# ======================================

# NOTE: we will get an error when we run this code because we are pointing it to "emp3" file instead of "mp3" file
# "emp3 files we are using here are just text and don't contain any tag information which the id3 reader is looking for.
# Error message: OSError: [Errno 22] Invalid argument

# We will see how to handle the error gracefully if we get an invalid argument in the list
# We will modify the program to handle any exceptions raised by the id3reader module
# If an exception is found, record the filename in the list and move to the next file.
# Once the loop finishes, print out all the files that caused an error.

# We handle the errors starting with CHANGE_1

import os
import fnmatch

import id3reader_p3 as id3reader   # CHANGE_1: import id3reader


def find_music(start, extension):
    for path, directories, files in os.walk(start):
        for file in fnmatch.filter(files, '*.{}'.format(extension)):  # LINE_3
            absolute_path = os.path.abspath(path)   # LINE_4: Creating absolute path
            # yield os.path.join(path, file)
            yield os.path.join(absolute_path, file)  # LINE_5: We use absolute_path in yielded values instead of path


my_music_files = find_music('music', 'emp3')

# CHANGE_1: Create empty list to store any problem files that we try to process

error_list = []

for f in my_music_files:
    try:  # CHANGE_2: Use try for check if this code runs without error
        id3r = id3reader.Reader(f)
        print("Artist: {}, Album: {}, Track: {}, Song: {}".format(
            id3r.get_value('performer'),
            id3r.get_value('album'),
            id3r.get_value('track'),
            id3r.get_value('title')
        ))
    except:
        error_list.append(f)  # CHANGE_3: Record all files that cause an exception

# CHANGE_4: Now we print files in error_list that caused exceptions

for error_file in error_list:
    print(error_file)

# When we run above program, it gives these results:

# First line: Shows one file returning None for the tags
# This is because if a file is large enough, the attempt to read the tag does not cause an error,
# but it just does not return a valid tag, hence we are getting None.

# Then following lines shows all the files (path and song) that caused an exception

# Artist: None, Album: None, Track: None, Song: None
# C:\Users\moe\Documents\Python\IdeaProjects\42_MusicFiles\music\music\1000 Maniacs\Our Time in Eden\1 - Candy Everybody Wants.emp3
# C:\Users\moe\Documents\Python\IdeaProjects\42_MusicFiles\music\music\1000 Maniacs\Our Time in Eden\10 - Noah's Dove.emp3
# C:\Users\moe\Documents\Python\IdeaProjects\42_MusicFiles\music\music\1000 Maniacs\Our Time in Eden\11 - Stockton Gala Days.emp3
# C:\Users\moe\Documents\Python\IdeaProjects\42_MusicFiles\music\music\1000 Maniacs\Our Time in Eden\12 - These Are Days.emp3
# C:\Users\moe\Documents\Python\IdeaProjects\42_MusicFiles\music\music\1000 Maniacs\Our Time in Eden\13 - Tolerance.emp3
# <<====== truncated ================>


# We will run above code to check a file with real mp3 files and see if it works


# ======================================
# Checking with real mp3 files
# ======================================

# I downloaded some real mp3 files and put them in music2 folder
# We will pass music2 folder and mp3 extension on LINE_6
#


import os
import fnmatch

import id3reader_p3 as id3reader   # CHANGE_1: import id3reader


def find_music(start, extension):
    for path, directories, files in os.walk(start):
        for file in fnmatch.filter(files, '*.{}'.format(extension)):  # LINE_3
            absolute_path = os.path.abspath(path)   # LINE_4: Creating absolute path
            # yield os.path.join(path, file)
            yield os.path.join(absolute_path, file)  # LINE_5: We use absolute_path in yielded values instead of path


# my_music_files = find_music('music2', 'mp3')   # LINE_6: pass music2 folder and mp3 extension
my_music_files = find_music('/Users/moe/Documents/Python/IdeaProjects/42_MusicFiles/music2', 'mp3')  # LINE_7: Using absolute path

# CHANGE_1: Create empty list to store any problem files that we try to process

error_list = []

for f in my_music_files:
    try:  # CHANGE_2: Use try for check if this code runs without error
        id3r = id3reader.Reader(f)
        print("Artist: {}, Album: {}, Track: {}, Song: {}".format(
            id3r.get_value('performer'),
            id3r.get_value('album'),
            id3r.get_value('track'),
            id3r.get_value('title')
        ))
    except:
        error_list.append(f)  # CHANGE_3: Record all files that cause an exception

# CHANGE_4: Now we print files in error_list that caused exceptions

for error_file in error_list:
    print(error_file)


# Results for above code:
# We should be alble to get good results but I am not getting any valid tags.

# Artist: None, Album: None, Track: None, Song: None
# Artist: None, Album: None, Track: None, Song: None
# Artist: None, Album: None, Track: None, Song: None

# When I ran music2 with the code for absolute path, I was able to get this.

# C:\Users\moe\Documents\Python\IdeaProjects\42_MusicFiles\music2\Dr. Dre - Still D.R.E. ft. Snoop Dogg.mp3
# C:\Users\moe\Documents\Python\IdeaProjects\42_MusicFiles\music2\Snoop Dogg - Gin & Juice.mp3
# C:\Users\moe\Documents\Python\IdeaProjects\42_MusicFiles\music2\Snoop Dogg - Who Am I (What's My Name)_.mp3

# Same thing when I put them in folders below

# C:\Users\moe\Documents\Python\IdeaProjects\42_MusicFiles\music2\music\snoop\with_dre\Dr. Dre - Still D.R.E. ft. Snoop Dogg.mp3
# C:\Users\moe\Documents\Python\IdeaProjects\42_MusicFiles\music2\music\snoop\with_dre\Snoop Dogg - Gin & Juice.mp3
# C:\Users\moe\Documents\Python\IdeaProjects\42_MusicFiles\music2\music\snoop\with_dre\Snoop Dogg - Who Am I (What's My Name)_.mp3



# ==============================
# Generators Summary
# ==============================

# So we have seen how to use generators in last few examples.
# Generators are a good way to deal with huge amounts of data without using up all your computers memory
