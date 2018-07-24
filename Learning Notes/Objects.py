""" Set of notes about dealing with objects in python"""

#See attributes possible in python, similar to object | fl in powershell
    from datetime import datetime
    now = datetime.now()
    dir(now) # this is where it will spit out all the things
    # another way to do it
        import math # Imports the math module
        everything = dir(math) # Sets everything to a list of things from math
        print everything # Prints 'em all!