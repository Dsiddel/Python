""" Notes from learning functions in python"""
# functions act the same as in powershell with slightly different syntax
    # example function with no variables
    def spam(egg):
        """Print's eggs to console"""
        print egg
    # calling above function
    spam()
    # calling function with string - can also be done with other variables
    spam(green)
    # all together example
        def power(base, exponent):  # sets parameters to use
            result = base ** exponent
            print "%d to the power of %d is %d." % (base, exponent, result)

            power(37, 4)  # sets value of parameters
    # functions can call other functions
        def one_good_turn(n):
            return n + 1
    
        def deserves_another(n):
            return one_good_turn(n) + 2
# function arguments
    # max() - takes a number or arguments and shows the largest one
        maximum = max(1,2,3)
        print maximum # will show 3
    # min() - takes a number or arguments and shows the smallest one
        minimum = min(1,2,3)
        print minimum # will show 1
    # abs() - takes a number and shows it's "absolute" number which is always positive, eg -5 will be 5 etc - only taks a single number
        absolute = abs(-3)
        print absolute # will show 3
    # type() - takes a value and shows the type of variable in it
        print type(42) # = int
        print type(5.5) # = float
        print type("asd") # = str
# lambda's - a quick function
    # syntax - this takes variable x, sets conditional as if it = pythin and runs through a list called "languages"
    print filter(lambda x: x == "Python", languages)
    #


