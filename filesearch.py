
# ===============
# filesearch.py
# ===============

# ===========================
# Searching the file system
# ===========================

# In the last section, we saw how to use the os.walk generator to work
# with files and directories in the local file system.

# Here we will use os.walk in generators of our own to give a lot of flexibility in working with files.


import os
import fnmatch

# Generator find_albums is similar to the previous ones.
# it uses os.walk to walk through the directories.  # LINE_2:
# For each one, it joins a path to the directory name, and then walks that tree to pick up the albums

# In the outer level (LINE_5), we are not interested in the list of files returned,
# and that is why we use underscore _ as a name
# underscore _ is a python convention to show that you are not using a value.

# In this example, we return a tuple containing the album_name and the path to the songs.
# Just like the os.path.split function was used to split the path up, we use os.path.join to recreate the path in the album directories

# NOTE: instead of adding root initialization here, we will pass it as a parameter to find_albums function
# root = "music"

def find_albums(root, artist_name):  # instead of
    for path, directories, files in os.walk(root): # LINE_2: path\directories\files = music\music\1000 Maniacs

        _=input("Print path, directories & files:")
        print("path = {}".format(path))  # Result = music
        print("directory = {}".format(directories))  # Result = ['music']
        print("files = {}".format(files))  # Result = []
        print("="*20)

        for artist in directories: # directories is the second part of the path. artist here is an instance of directories

            _=input("Print directories instance (named artist here):")
            print("directories instance (artist) = {}".format(artist))   # Result  = music
            print("="*20)

            subdir = os.path.join(path, artist)  # LINE_4: joins the path (music) and directory instance (artist) which is also (music)

            _=input("Print subdir, which is path & directory instance (artist) joined:")
            print("Path join directory instance = {}".format(subdir))  # Results = music\music (path and directory instance joined)
            print("="*20)

            for album_path, albums, _ in os.walk(subdir):  # LINE_5: Walks through the subdir (music\music)

                _=input("Print album_path, albums and _ :")
                print("album_path = {}".format(album_path))  # Result = music\music
                print("albums = {}".format(albums))   # Result = ['1000 Maniacs', 'Axel Rudi Pell'. etc ]
                print("_ = {}".format(_))  # Prints nothing. underscore is python convention of not using any value.
                print("="*20)

                # This code will iterate through albums, then join album_path and album into path
                # Then add a separate instance of album.

                for album in albums:

                    _=input("Print album_path and album:")
                    print("album_path = {}".format(album_path))
                    print("album = {}".format(album))
                    # print("="*20)
                    yield os.path.join(album_path, album), album  # yields album_path, album and album and passes it to PRINT CALL below
                    print("="*20)


# We pass the root (music) and artist name (Axel Rudi Pell) in this case
album_list = find_albums("music", "Axel Rudi Pell")


# PRINT CALL
# Now we do a for loop to go through the album_list
# This results in a series of tuples containing directory path and the album name

# for a in album_list:
#     print(a)

print(next(album_list))
print(next(album_list))
print(next(album_list))

# Here is sample results for this:

# ('music\\music\\1000 Maniacs', '1000 Maniacs')
# ('music\\music\\Axel Rudi Pell', 'Axel Rudi Pell')
# ('music\\music\\Bad Company', 'Bad Company')
# ('music\\music\\Beatles', 'Beatles')
# ('music\\music\\Bernie Torme', 'Bernie Torme')





# ===========================================
# Above Code without stops and explanations:
# ===========================================

import os
import fnmatch

def find_albums(root, artist_name):
    for path, directories, files in os.walk(root):
        for artist in directories:
            subdir = os.path.join(path, artist)
            for album_path, albums, _ in os.walk(subdir):
                for album in albums:
                    yield os.path.join(album_path, album), album


album_list = find_albums("music", "Axel Rudi Pell")

print(next(album_list))
print(next(album_list))
print(next(album_list))





# ===================
# Using fnmatch
# ===================

# In above code, you notice that we are not using imported FILE NAME MATCH "fnmatch"
# and we are also not using the passed Artist name "Axel Rudi Pell"

# " fnmatch " is used to match files whose name follow some sort of pattern
# So our find_albums generator will be more useful if it returns the albums for a single artist e.g. Axel Rudi Pell
# We can make it to do that using CHANGES_1 shown
# So we only get the albums from directories that exactly match Artist name passed. in this case, Axel Rudi Pell

# The generator returns a tuple containing the path to the directory and the name of the directory
# So you can only generate the album name if you like
# ('music\\music\\Axel Rudi Pell\\Between The Walls', 'Between The Walls')

# In this case, we are going to demonstrate how using generators can be used to simplify code.
# As an example, we will show a way to get the list of songs in the albums.
# See next code below.

import os
import fnmatch



def find_albums(root, artist_name):  # instead of
    for path, directories, files in os.walk(root): # LINE_2: path\directories\files = music\music\1000 Maniacs

        _=input("Print path, directories & files:")
        print("path = {}".format(path))  # Result = music
        print("directory = {}".format(directories))  # Result = ['music']
        print("files = {}".format(files))  # Result = []
        print("="*20)

        for artist in fnmatch.filter(directories, artist_name): # CHANGE_1: add fnmatch to filter by artist_name

            _=input("Print directories instance (named artist here):")
            print("directories instance (artist) = {}".format(artist))   # Result  = music
            print("="*20)

            subdir = os.path.join(path, artist)  # LINE_4: joins the path (music) and directory instance (artist) which is also (music)

            _=input("Print subdir, which is path & directory instance (artist) joined:")
            print("Path join directory instance = {}".format(subdir))  # Results = music\music (path and directory instance joined)
            print("="*20)

            for album_path, albums, _ in os.walk(subdir):  # LINE_5: Walks through the subdir (music\music)

                _=input("Print album_path, albums and _ :")
                print("album_path = {}".format(album_path))  # Result = music\music
                print("albums = {}".format(albums))   # Result = ['1000 Maniacs', 'Axel Rudi Pell'. etc ]
                print("_ = {}".format(_))  # Prints nothing. underscore is python convention of not using any value.
                print("="*20)

                # This code will iterate through albums, then join album_path and album into path
                # Then add a separate instance of album.

                for album in albums:

                    _=input("Print album_path and album:")
                    print("album_path = {}".format(album_path))
                    print("album = {}".format(album))
                    # print("="*20)
                    yield os.path.join(album_path, album), album  # yields album_path, album and album and passes it to PRINT CALL below
                    print("="*20)


# We pass the root (music) and artist name (Axel Rudi Pell) in this case
album_list = find_albums("music", "Axel Rudi Pell")


# PRINT CALL
# Now we do a for loop to go through the album_list
# This results in a series of tuples containing directory path and the album name

# for a in album_list:
#     print(a)

print(next(album_list))
print(next(album_list))
print(next(album_list))




# ===========================================
# Above Code without stops and explanations:
# ===========================================

import os
import fnmatch

def find_albums(root, artist_name):
    for path, directories, files in os.walk(root):
        for artist in fnmatch.filter(directories, artist_name):
            subdir = os.path.join(path, artist)
            for album_path, albums, _ in os.walk(subdir):
                for album in albums:
                    yield os.path.join(album_path, album), album


album_list = find_albums("music", "Axel Rudi Pell")

for a in album_list:
    print(a)



# ===========================================================
# Chaining Generator to another
# (Passing one generator as argument to another generator)
# ============================================================

# ===========================================
# Using generator to get list of songs.
# ===========================================

# In this case, we are going to demonstrate how using generators can be used to simplify code.
# As an example, we will show a way to get the list of songs in the albums.
# We will add the find_songs generator


import os
import fnmatch



def find_albums(root, artist_name):  # instead of
    for path, directories, files in os.walk(root): # LINE_2: path\directories\files = music\music\1000 Maniacs

        _=input("Print path, directories & files:")
        print("path = {}".format(path))  # Result = music
        print("directory = {}".format(directories))  # Result = ['music']
        print("files = {}".format(files))  # Result = []
        print("="*20)

        for artist in fnmatch.filter(directories, artist_name): # CHANGE_1: add fnmatch to filter by artist_name

            _=input("Print directories instance (named artist here):")
            print("directories instance (artist) = {}".format(artist))   # Result  = music
            print("="*20)

            subdir = os.path.join(path, artist)  # LINE_4: joins the path (music) and directory instance (artist) which is also (music)

            _=input("Print subdir, which is path & directory instance (artist) joined:")
            print("Path join directory instance = {}".format(subdir))  # Results = music\music (path and directory instance joined)
            print("="*20)

            for album_path, albums, _ in os.walk(subdir):  # LINE_5: Walks through the subdir (music\music)

                _=input("Print album_path, albums and _ :")
                print("album_path = {}".format(album_path))  # Result = music\music
                print("albums = {}".format(albums))   # Result = ['1000 Maniacs', 'Axel Rudi Pell'. etc ]
                print("_ = {}".format(_))  # Prints nothing. underscore is python convention of not using any value.
                print("="*20)

                # This code will iterate through albums, then join album_path and album into path
                # Then add a separate instance of album.

                for album in albums:

                    _=input("Print album_path and album:")
                    print("album_path = {}".format(album_path))
                    print("album = {}".format(album))
                    # print("="*20)
                    yield os.path.join(album_path, album), album  # yields album_path, album and album and passes it to PRINT CALL below
                    print("="*20)


# We find songs by passing it the albums we want the songs from.
# This time we know the directory we are looking at and are not expecting any subdirectories
# So there is no need to walk through the entire directory structure
# So we use os.listdir instead of os.walk
# NOTE: This may or may not be more efficient, but we will discuss that later.

def find_songs(albums):
    for album in albums:
        for song in os.listdir(album[0]):  # we want the path, not the name of the album
            yield song


# We pass the root (music) and artist name (Axel Rudi Pell) in this case
album_list = find_albums("music", "Axel Rudi Pell")

# Now we call find_songs generator, pass it album_list and assign it to song_list
song_list = find_songs(album_list)


# PRINT CALL
# Now we do a for loop to go through the album_list
# This results in a series of tuples containing directory path and the album name

# for a in album_list:
#     print(a)

# Print album_list
print(next(album_list))
print(next(album_list))
print(next(album_list))

# print song_list

for s in song_list:
    print("songs = {}".format(s))
    print("="*20)




# ===========================================
# Above Code without stops:
# ===========================================

# The interesting thing here is we have removed the generator of the data from the code that makes use of the data
# We could do that with ordinary functions, but they would be returning lists and they could be huge.
# And these huge lists would stay in memory until we explicitly clear them and this is something we would sometimes forget.

# So when using this approach, we can create a list of songs from any Artist with four lines of code and very little overhead
# Here we are chaining generators together by passing one generator on as the argument to the next.
# In this case, we are passing "find_albums" generator as argument to "find_songs" generator

# On LINE_1, when we loop through the albums, the generator returns the details for each item as we request them
# At no time does the complete list of albums exist in memory.
# Same thing with songs. We get each song as needed and the program does not create a list of songs as such.

# This however is not completely true because the os.walk function returns lists in its tuple
# If the lists are going to be so big and hence occupy lots of memory, then os.walk may not be suitable for your particular application

# we will look at "scandir" later on, and this can be useful if you want to avoid generating the lists that os.walk creates
# See "Generator summary info" below for more info.

import os
import fnmatch

def find_albums(root, artist_name):
    for path, directories, files in os.walk(root):
        for artist in fnmatch.filter(directories, artist_name):
            subdir = os.path.join(path, artist)
            for album_path, albums, _ in os.walk(subdir):
                for album in albums:
                    yield os.path.join(album_path, album), album


def find_songs(albums):
    for album in albums:  # LINE_1
        for song in os.listdir(album[0]):  # we want the path, not the name of the album
            yield song


album_list = find_albums("music", "Axel Rudi Pell")
song_list = find_songs(album_list)

# NOTE: Song_list will print if this album_list is commented out
# for a in album_list:
#     print(a)

for s in song_list:
    print(s)

# When you run above code, it produces these results of all the songs belonging to Axel Rudi Pell

# 1 - The Curse.emp3
# 10 - Desert Fire.emp3
# 2 - Talk Of The Guns.emp3
# 3 - Warrior.emp3
# 4 - Cry Of The Gypsy.emp3
# 5 - Casbah.emp3
# 6 - Outlaw.emp3
# 7 - Wishing Well.emp3
# 8 - Innocent Child.emp3
# <<===== truncated ==========>>




# ================================================================
# Generator Summary info:
# ================================================================

# Creating and destroying a lot of lists will affect performance, so python will have to
# take care of reclaiming memory for the previous album songlist each time we process a new album.

# Using generators like this can be very useful for interogating log files in a local server
# There could be thousands of lots e.g. apache logs and these can be a lot.

# But using a generator to return the name and full path of each file and then another generator to check each file
# for a particular matching string is a very memory efficient way to look for particular errors of find something else you want.
# So generators make python to be a great choice for working with huge datasets.

# There are more things you can do with generators.
# Since Python 3.5, it is also possible to send a value into a generator using a slightly different form of yield.


# ===============================================================
# Using wildcard ( * ) on "fnmatch" module's "filter" method :
# ===============================================================

# In above Filter method can take wildcards so it can process all the names that start with certain letters.
# For example, in this case, we can make filter use a wildcard to process all names that start with "Black"
# by adding asterix (*) ==> black*
# We do that in LINE_2 below.
# When you activate PRINT_ALBUM, you will see the artists are "Black Keys" and "Black Oak". all starting with Black
# Then deactivate PRINT_ALBUM and you will see all the songs for "Black Keys" and "Black Oaks"

# NOTE that the fnmatch filter is sort of case sensitive
# This is because the behavior depend on the operating system

# Linux files are case sensitive hence fnmatch is case sensitive in linux

# But windows NTFS is not case sensitive and so fnmatch is not case sensitive in Windows
# That is why I don't see any difference here between Black* and black*

# MAC uses HTFS file system which is "Not case sensitive" but is "Case preserving".
# With HTFS, you cannot create files with the same name using different case.
# But you can refer to a file using its name in either uppercase or lowercase
# When python reads the file, it returns the name of the original case that it was created with.
# This is why trainer changed case for black* and pulled nothing because he was using MAC

# To resolve the Case issue, you can use a generator expression to convert the directory names to uppercase
# We will see this in the next code


import os
import fnmatch

def find_albums(root, artist_name):
    for path, directories, files in os.walk(root):
        for artist in fnmatch.filter(directories, artist_name):
            subdir = os.path.join(path, artist)
            for album_path, albums, _ in os.walk(subdir):
                for album in albums:
                    yield os.path.join(album_path, album), album


def find_songs(albums):
    for album in albums:  # LINE_1
        for song in os.listdir(album[0]):  # we want the path, not the name of the album
            yield song


album_list = find_albums("music", "Black*")  # LINE_2: Search for artist whose name start with Black
song_list = find_songs(album_list)

# PRINT_ALBUM: Song_list will print if this album_list is commented out
# for a in album_list:
#     print(a)

# PRINT_SONG:
for s in song_list:
    print(s)




# ====================================================================
# Using " generator expression " to change directory names to uppercase
# ====================================================================


# To resolve the Case issue above (for MAC and LINUX),
# you can use a generator expression to convert the directory names to uppercase

# " Generator expressions " will make more sense when we learn about " list comprehensions " later
# So don't worry if you don't understand code below for using generator expression to convert to uppercase
# we will make changes CHANGE_1 and CHANGE_2
# This will now work for MAC, and it still works for Windows.

# NOTE that this will still not work for case-sensitive file systems like Linux
# For case sensitive file systems, its best to use regular expressions

# We can also use a more complicated generator function which will work in Linux.
# We will look at it in the next code.


import os
import fnmatch

def find_albums(root, artist_name):
    caps_name = artist_name.upper()   # CHANGE_1: create caps_name and assign it artist_name in uppercase
    for path, directories, files in os.walk(root):
        # for artist in fnmatch.filter(directories, artist_name):  # CHANGE_2: comment this out and replace with one below
        for artist in fnmatch.filter((d.upper() for d in directories), caps_name):  # CHANGE_2
            subdir = os.path.join(path, artist)
            for album_path, albums, _ in os.walk(subdir):
                for album in albums:
                    yield os.path.join(album_path, album), album


def find_songs(albums):
    for album in albums:  # LINE_1
        for song in os.listdir(album[0]):  # we want the path, not the name of the album
            yield song


album_list = find_albums("music", "Black*")  # LINE_2: Search for artist whose name start with Black
song_list = find_songs(album_list)

# PRINT_ALBUM: Song_list will print if this album_list is commented out
# for a in album_list:
#     print(a)

# PRINT_SONG:
for s in song_list:
    print(s)





# ====================================================================
# Using a more complex " generator expression "
# ====================================================================

# We can also use a more complicated generator function which will work in Linux, but its not as good as using filters.
# But we will look at it here.

# We will comment out CHANGE_2 and add a complex expression under CHANGE_3
# This should work on all operating systems (Windows, MAC and Linux)


import os
import fnmatch

def find_albums(root, artist_name):
    caps_name = artist_name.upper()   # CHANGE_1: create caps_name and assign it artist_name in uppercase
    for path, directories, files in os.walk(root):
        # for artist in fnmatch.filter(directories, artist_name):  # CHANGE_2: comment this out and replace with one below
        # for artist in fnmatch.filter((d.upper() for d in directories), caps_name):  # CHANGE_2
        for artist in (d for d in directories if fnmatch.fnmatch(d.upper(), caps_name)):  # CHANGE_3
            subdir = os.path.join(path, artist)
            for album_path, albums, _ in os.walk(subdir):
                for album in albums:
                    yield os.path.join(album_path, album), album


def find_songs(albums):
    for album in albums:  # LINE_1
        for song in os.listdir(album[0]):  # we want the path, not the name of the album
            yield song


album_list = find_albums("music", "Black*")  # LINE_2: Search for artist whose name start with Black
song_list = find_songs(album_list)

# PRINT_ALBUM: Song_list will print if this album_list is commented out
# for a in album_list:
#     print(a)

# PRINT_SONG:
for s in song_list:
    print(s)


