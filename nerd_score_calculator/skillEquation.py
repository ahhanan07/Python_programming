# Author: ABDUL HANAN
# Start Date: 30th March 2019
# Last Modified Date: 11th April 2019

# Functionality: calculate the skill score by the equation
# This file is exported to menu_30340284.py
# fandom_score, hobbies_score, sports_played are inputs from menu_30340284.py
# calculateSkillEquation() method is used to calculate the nerd score


def calculateSkillEquation(fandom_score, hobbies_score, sports_played):
	skillScore = 0

	# Equation to calculate skill score
	skillScore = fandom_score * ((42*(hobbies_score**2))/(sports_played+1)) ** (1/2)

	return skillScore	
	
	
if __name__ == '__main__':

	FandomScore, HobbiesScore, SportsNum = 1, 4, 1 #the output should be 18.33030277982336

	try:
		print(calculateSkillEquation(FandomScore, HobbiesScore, SportsNum))
	
	except e:
		print(e)
		raise	
