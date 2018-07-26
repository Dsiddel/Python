""" Set of notes about dealing with conditions and flow control in python"""
# comparitors
    # order of operations
        #Not --> and --> or
            True or not False and False
            True
    # Equal to ==
        2 == 2
        True
        2 == 5
        False
    # Not equal to !=
        2 != 5
        True
        2 != 2
        False
    # less than <
        2 < 5
        True
        2 < 1
        False
    # Less than or equal to <=
        2 <= 3
        True
        2 <= 1
        False
    # Greater than >
        2 > 1
        True
        2 > 5
        False
    # Greater than or equal to >=
        2 >= 1
        True
        2 >= 5
        False
    # and - both expressions must be true
        1 < 2 and 2 < 5
        True
        1 > 3 and 3 == 4
        False
    # or - at least one expression is true
        1 < 2 or 2 < 1
        True
        5 < 3 or 5 < 2
        False
    # not - returns true for false statements and false for true statements
        not 5 < 3
        True
        not 1 == 1
        False
# Conditional Statements
    # if - same as powershell stuff
        if 8 < 9:
            print "Eight is less than nine!"
    # else - same as powershell stuff
        if 8 < 9:
            print "this is true"
        else:
            print "this is false"
    # elif - same as powershell stuff
        if 8 > 9:
            print "I don't get printed!"
        elif 8 < 9:
            print "I get printed!"
        else:
            print "I also don't get printed!"
    # for - similar to powershell but with different syntax
        my_list = [1,9,3,8,5,7]
        for number in my_list:
            print number * 2
    