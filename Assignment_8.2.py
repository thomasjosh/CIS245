# This is a header for the application
# You should read this header and insert your name and your date below as part of the peer review
# This is a typical part of any program
# Author: Joshua Thomas
# Creation Date: 9/27/2020
# Below is a simple program with 10 issues (some are syntax errors and some are logic errors.  You need to identify the issues and correct them.

import random
import time

def displayIntro():
	print('''You are in a land full of dragons. In front of you,
	you see two caves. In one cave, the dragon is friendly
	and will share his treasure with you. The other dragon
	is greedy and hungry, and will eat you on sight.''')
	print()

def chooseCave():
	cave = ''
    #while cave != '1' and cave != '2':
	while cave != 1 and cave != 2:
	#had too many tabs and did not need quotes.
		print('Which cave will you go into? (1 or 2)')
		cave = input()
	#return caves
		break
	#does not need to be a return function, but instead a break. Return makes it run a forever loop.

def checkCave(chosenCave):
	print('You approach the cave...')
	#sleep for 2 seconds
	time.sleep(2)
	print('It is dark and spooky...')
	#sleep for 2 seconds
	#time.sleep(3)
	time.sleep(2)
	#not consistent with other sleep times.
	print('A large dragon jumps out in front of you! He opens his jaws and...')
	print()
	#sleep for 2 seconds
	time.sleep(2)
	friendlyCave = random.randint(1, 2)

	if chosenCave == str(friendlyCave):
		print('Gives you his treasure!')
	else:
		#print 'Gobbles you down in one bite!'
		print ('Gobbles you down in one bite!')
		#missing parentheses.

playAgain = 'yes'
#while playAgain = 'yes' or playAgain = 'y':
while playAgain == 'yes' or playAgain == 'y':
#needed another eqaul sign since 'playAgain' was already defined
	displayIntro()
	#caveNumber = choosecave()
	caveNumber = chooseCave()
	#should have been "chooseCave" instead of "choosecave"
	checkCave(caveNumber)
    
	print('Do you want to play again? (yes or no)')
	playAgain = input()
	if playAgain == "no":
		#print("Thanks for planing")
		print("Thanks for playing")
		#playing was mispelled

