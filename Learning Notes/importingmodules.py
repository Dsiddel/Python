""" Importing modules notes"""
#Installing - must be done before importing
    # install a module - installs ppring
        python -m pip install pprint
# Importing
    # import whole module
        import pprint
    # import function
        from module import function
#Using modules
    # math module example if imported whole module
        import math
        print math.sqrt(25) # the function or value .sqrt is in the math module therefore you need to call it first.
    # example if only importing function
        from math import sqrt
        print sqrt(25)
    # Universal import - imports all things from module andnot make you type module. before everything
        from math import *
        print sqrt(25)