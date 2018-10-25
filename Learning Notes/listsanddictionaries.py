"""" lists and dictionaries notes """
#Lists
    # similar to arrays in powershell
        zoo_animals = ["pangolin", "cassowary", "sloth", "dog" ];
    # access by index
        zoo_animals = ["pangolin", "cassowary", "sloth", "dog" ];
        print "The first animal at the zoo is the " + zoo_animals[0]
    # assign new value to list location
        zoo_animals = ["pangolin", "cassowary", "sloth", "tiger"]
        zoo_animals = [2] = hyena
    # removing something from a list
        zoo_animals = ["pangolin", "cassowary", "sloth", "tiger"]
        zoo_animals.remove("pangolin")
        #using pop to remove list and return it to you
            n = [1,3,5]
            n.pop(1)
            #returns 3 (the item at index 1)
            print n
            prints [1,5]
        #using del is like .pop but won't return the item to you
            del(n[1])
            #doesn't return anything
            print n
            #prints [3,5]

    # extending a list
        zoo_animals.append('cat')
    # get length of list
        print len(zoo_animals)
    # selecting specific values in the list
        suitcase = ["sunglasses", "hat", "passport", "laptop", "suit", "shoes"]
        middle = suitcase[2:4]
    # can slice with strings the same way
        animals = "catdogfrog"
        cat = animals[:3]
        dog = animals[3:6]
        frog = animals[6:]
    # place new values in a specific order
        animals = ["aardvark", "badger", "duck", "emu", "fennec fox"]
        duck_index = animals.index("duck")
        animals.insert(duck_index, "cobra")
    # sorting
        animals = ["aardvark", "badger", "duck", "emu", "fennec fox"]
        print animals.sort()
    # using range and lists
        range(6) # => [0, 1, 2, 3, 4, 5]
        range(1, 6) # => [1, 2, 3, 4, 5]
        range(1, 6, 3) # => [1, 4]
    # list slicing, start, end and "stride" of 2 would mean every 2nd 
        [start:end:stride]
        print l[2:9:2]
        # -1 can go backwards, e.g
            print l[::-1]

# Dictionaries
    # disctionaries are like list but hold two values, think of tag's in azure  name : value
        residents = {'Puffin' : 104, 'Sloth' : 105, 'Burmese Python' : 106}
        # printing a dictionary valie
            print residents['Puffin']
    # you can put lists inside dictionary pairs, empy dictionary is {} empty list is[]
    # New entries
        menu = {}
        menu['chicken'] = 10
        print menu
    # removing entries
        del menu['chicken']
    # replace current key entry
        menu['chicken'] = 15
    # all together example
        inventory = {
            'gold' : 500,
            'pouch' : ['flint', 'twine', 'gemstone'],
                'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
        }
    
        inventory['pocket'] = ['seashell', 'strange berry', 'lint']
        inventory['backpack'].sort()
        inventory['backpack'].remove('dagger')
        inventory['gold'] = inventory['gold'] + 50
    # getting values from dictionaries
        # items - gets both key and value
            my_dict.items()
        # keys - gets only keys
            my_dict.keys()
        # values - gets only values
            my_dict.values
    # running a loop through all keys
        for word in webster:
            print webster[word]
    