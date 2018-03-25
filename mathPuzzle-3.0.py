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
import curses

# Just get a random sample of the numbers 1 through 10
# The sample is broken down thusly:
# Array items 0 through 3 are top most integers
# Array items 4 through 6 are top-middle integers
# Array items 7 through 8 are bottom-middle integers
# Array item 9 is the lowest placed integer

x = random.sample(range(1,11),4)

# Basic curses settings
stdscr = curses.initscr()
curses.noecho()
curses.cbreak()
stdscr.keypad(1)

stdscr.addstr(1, 5, "Program Running. Please wait...")
stdscr.refresh()

# Variables
solved = 0 # Change this if you'd like to quit after a certain number of events or findings
attempts = 0 # Incremented to track total number of events
solutions = [] # An Array to track all the solutions. Don't give credit multiple times for same finding.
solutions_str = ''
patterns = [] # An array implemented to track all the patterns, prevent duplicate evaluations

try:
	while len(solutions) != 8: # I am assuming that 8 solutions is the max
		if ((x in patterns) == False):
			patterns.append(x)

			y = [
				x[0], x[1], x[2], x[3],
				abs(x[0] - x[1]), abs(x[1] - x[2]), abs(x[2] - x[3]),
				abs(abs(x[0] - x[1]) - abs(x[1] - x[2])),
				abs(abs(x[2] - x[3]) - abs(x[1] - x[2])),
				abs(abs(abs(x[0] - x[1]) - abs(x[1] - x[2])) - abs(abs(x[2] - x[3]) - abs(x[1] - x[2])))
				]

			if (1 in y and 2 in y and 3 in y and
				4 in y and 5 in y and 6 in y and
				7 in y and 8 in y and 9 in y and 10 in y ):

				solutions.append(y)
				solutions_str += str(y) + '\n     '

			stdscr.addstr(2, 5, "Attempts: " + str(attempts))
			stdscr.addstr(3, 5, "Patterns: " + str(len(patterns)))
			stdscr.addstr(4, 5, "Solutions: " + str(len(solutions)))
			stdscr.addstr(5, 5, solutions_str)
			stdscr.refresh()

			attempts += 1 # Increment the attempt each round
		x = random.sample(range(1,11),4) # Get a new sample

	stdscr.addstr(1, 5, "Program complete. Hit any key to exit.")
	stdscr.refresh()
	stdscr.getch()
except:
	pass
# End the program
curses.nocbreak(); stdscr.keypad(0); curses.echo()
curses.endwin()
