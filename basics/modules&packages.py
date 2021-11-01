# a module --
    #  -- is a piece of software that has a specific functioanlity
    #  -- each is a different file which can be edited separately



# example 
mygame/
    mygame/game.py
    mygame/draw.py



# game.py will implement the game
# import the draw module 
import draw

def play_game():
    ...

def main():
    result = play_game()
    # must specify which module the function is coming from here
    draw.draw_game(result)

# this means that if this script is executed, then main() will be executed
if _name_ == '_main_':
    main()



# draw.py

def draw_game():
    ...

def clear_screen(screen):
    ...



# we may also import functions directly into the main script's namespace by using the 'from' command

# game.py
# import the draw module
from draw import draw_game

def main():
    result = play_game()
    # no need to specify module here because of import command
    draw_game(result)

# note -- a namespace cannot have two objects with the same name, so the 'import' command could replace an existing object in the namespace



# importing all objects from a module
from draw import *



# custom import name

# game.py
# import the draw module
if visual_mode:
    # in visual mode, we draw using graphics
    import draw_visual as draw
else:
    # in textual mode, we print out text
    import draw_textual as draw

def main():
    result = play_game()
    # this can either be visual or textual depending on visual_mode
    draw.draw_game(result)



# module initialization: even if a module is imported more than once, it will only be initialized once 

# draw.py

def draw_game():
    # when clearing the screen we can use the main screen object initialized in this module
    clear_screen(main_screen)
    ...

def clear_screen(screen):
    ...

class Screen():
    ...

# initialize main_screen as a singleton
main_screen = Screen()



# extending module load path

# using the environment variable PYTHONPATH --
    #  -- this will execute game.py
    #  -- this will enable the script to load modules from the foo directory
    #  -- this will enable the script to load modules from the local directory
PYTHONPATH=/foo python game.py

# this will add the foo directory to the list of paths to look for modules in
# may be executed before running an import command
sys.path.append('/foo')



# built-in modules

# importing the urllib, which allows us to create read data from URLs
import urllib

urllib.urlopen(...)

# we can look for which functions are implemented in each module with the dir function
import urllib
dir(urllib)

# when we find what we want, we can read more about it --
help(urllib.urlopen)



# packages --
    #  -- are directories which contain multiple packages and modules themselves
    #  -- must contain a special file called '__init__.py'
    #  -- the file can be empty
    #  -- the file is indicative of the Python package, so it can be imported the same way a module can be imported

foo/
    __init__.py
    bar

# using the module bar
import foo.bar
# OR
from foo import bar

# the '__init__.py' file can decide which modules to export and which to keep by overriding the '__all__' variable
__init__.py:

__all__ = ['bar']



# exercise -- print an alphabetically sorted list of all functions in the re module which contain the word 'find'
import re

find_members = []
for member in dir(re):
    if 'find' in member:
        find_members.append(member)

print(sorted(find_members))