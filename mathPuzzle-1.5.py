#!/usr/bin/python

##########################
# This was a simple program built to determine all possible outcomes for a math game
# Rules of the game are:
# Using the numbers 1 through 10 once, fill an inverted pyramid
#
# _   _   _   _
#   _   _   _
#     _   _
#       _
#
# The final solution(s) must work together mathematically. Each triangle
# must be such that the top two numbers subtract into the integer of the space below.
#
# ie. 
#
# 3   2   _   _
#   1   _   _
#     _   _
#       _
#
# In this game, the order of subtraction does not matter. The output should be the absolute value.
#
# The reason I created this game is that I've always figured there were multiple solutions.
# I had worked out other solutions with the assistance of friends, but it was difficult to go through
# all possible permutations. Using the random number generator, I can let the computer try as often as
# it wants. Enjoy, and see if you can find a way to optimize the solution finding to get quicker results!
################

# Modules
import random

# Just get a random sample of the numbers 1 through 10
# The sample is broken down thusly:
# Array items 0 through 3 are top most integers
# Array items 4 through 6 are top-middle integers
# Array items 7 through 8 are bottom-middle integers
# Array item 9 is the lowest placed integer

x = random.sample(range(1,11),10)



# Variables
solved = 0 # Change this if you'd like to quit after a certain number of events or findings 
attempts = 0 # Incremented to track total number of events
solutions = [] # An Array to track all the solutions. Don't give credit multiple times for same finding.

while solved == 0: # this program is designed to run forever - I don't know how many solutions exist
	if (        abs(x[0] - x[1]) == x[4] 
		and abs(x[1] - x[2]) == x[5] 
		and abs(x[2] - x[3]) == x[6] 
		and abs(x[4] - x[5]) == x[7] 
		and abs(x[5] - x[6]) == x[8] 
		and abs(x[7] - x[8]) == x[9] ): # This logic makes the pyramid
		
		unique = True # We start with the assumption that the new solution is unique 

		for s in solutions: # Verify that the solution really is unique
			if (x == s):
				unique = False
		
		if (unique): # If the solution really is unique				
			solutions.append(x) # append the solution to the solutions array 
			print("Unique Solution Found!") # Document the solution on the screen for the user
			print("Attempts: " + str(attempts))
			print("Solutions: " + str(len(solutions)))
			print(x[:4])
			print(x[4:7])
			print(x[7:9])
			print(x[9])

	attempts += 1 # Increment the attempt each round
	x = random.sample(range(1,11),10) # Get a new sample 

