""" This is a dice game"""

from random import randint
from time import sleep

def get_user_guess():
  guess = int(raw_input("What is your guess? "))
  return guess

def roll_dice(number_of_sides):
  first_roll = randint(1, number_of_sides)
  second_roll = randint(1, number_of_sides)
  max_val = number_of_sides * 2
  print "The max value is %s" % max_val
  guess = get_user_guess()
  if guess > max_val:
    print "Invalid guess"
  else:
    print "Rolling..."
    sleep(2)
    print 'The first roll is %d' % first_roll
    sleep(1)
    print "The second roll is %d" % second_roll
    total_roll = first_roll + second_roll
    print "Result... %d" % total_roll
    sleep(1)
    if get_user_guess > total_roll:
      print "You win!"
    else:
    	print "You lose!"
  
roll_dice(6)
  