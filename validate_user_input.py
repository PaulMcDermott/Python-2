#!/usr/bin/env python


# CHECK USER INPUT TO MAKE SURE IT'S AN INTEGER AND RETURN ZERO IF IT ISN'T
def input_validation(user_input):
  try:
    return int(user_input)
  except ValueError:
    print "You did not enter an integer"; return 0
	

number = input_validation(raw_input("Enter a number:")) 
print "number is:", number
