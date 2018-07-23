""" This is a collection of notes I've taken as i've learned python syntax for a cheat sheet reference """
# comments
    # for single line comment
        """ for multi
        line
        comments """
#Printing
    # Python 2
        print "Hello world!"
    # Python 3
        print ("Hellp world!")
    # adding variables
        product = "good"
        string_example = "THe product was " + str(product) #Spacing after "was" is important due to sentance structure
        print string_example
        # adding advanced variables - %s is replaces with variable at the end similar to powershell functions
            string1 = "Camelot"
            string2 = "place"
            print "Let's not go to %s. 'Tis a silly %s." % (string1, string2) # you must have the same number of &s and variables at the end or it will error
                # padding for integers - 0 is pad 2 is the number of digits to pad and d means to give signed integer
                    string1 = 6
                    print "03 - %s - 2019" % (string1)
                        # 03 - 6 - 2019
                    print "03 - %02d - 2019" % (string1)
                        # 03 - 06 - 2019
    # adding other strings
        print "Hello" + "World"
#Variables
    # creating a variable
        variable = "23" #gives a string
        variable = 23 #gives an int
    # updating a variable
        # Adding
            variable = 1
            variable += 5
            # adding more than one thing at a time
                variable = 1
                variable += 1 + 5 + 6
        # subtracting
            variable = 10
            variable -= 5

# Arithmetic - Follows order of operations simplified example =  1) exponents and roots 2) multiplication and division 3) addition and subtraction
    # Addition
        addition = 1 + 1
    # Multiplication
        multiplication = 1 * 2
    # Subtraction
        subtraction = 5 - 4
    # modulo (Shows remainder of division)
        modulo = 5 % 4 # returns as 1
    # exponent (to the power of)
        exponent = 2**2
    # division
        #int division
            division = 10 / 2
        #float division - all three are acceptable
            division = 5. / 2
            division = 5. / 2.
            division = 5 / 2.
                # use float method
                    division = float(5)/2
# Numbers
    #int - full numbers
        int1 = 1
    #float - a number with decimal places or scientific notation
        int1 = 1.1
        int2 = 1.5e2
#Booleans
    #True
        variable = True
    #False
        variable = False

#Strings
    # Example Strings
        variable = 'string 1'
        variable = "string 2"
        #error characters
             'This isn't flying, this is falling with style!'
                #notice the above? fixed with
                    'This isn\'t flying, this is falling with style!'
    # Accessing by index - 0 counts as first letter
        First_letter = "Daniel"[0]
        Second_letter = "Daniel"[1]
    # Methods
        # Length - gets length of string
            variable = "Daniel"
            print len(variable)
        # Lower - turns everything to lower case
            variable = "Daniel"
            print Daniel.lower()
        # Upper - sets everything to upper case
            variable = "Daniel"
            pring Daniel.upper()
        # str(object) - turns variable into a string
            variable = 55
            print str(variable)
# Date & time
    #importing
        from datetime import datetime
    # Current time
        datetime.now()
    # modifying the time variable - just like a powershell object
        from datetime import datetime
        now = datetime.now()
        print now.year
        print now.month
        print now.day
    # setting date as mm/dd/yyyy
        from datetime import datetime
        now = datetime.now()
        print '%02d/%02d/%04d' % (now.month, now.day, now.year)
# inputs
    # get input from user - is a string by default
        variable = raw_input("Enter something here: ")
    # get float input from user
        variable = float(raw_input("What's the number"))


    