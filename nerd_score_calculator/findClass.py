# Author: ABDUL HANAN
# Start Date: 30th March 2019
# Last Modified Date: 11th April 2019

# This file is exported to menu.py
# studentScore_list is input from menu.py
# countStudentClass() method is used to determine the nerd class


def countStudentClass(studentScore_list):
	if len(studentScore_list) < 1:
		print("Please add at least 1 item into the list")    # prints and returns 0 if studentScore_list is empty
		return 0

	nerdCount_list = [0] * 7

	# initialise for loop to check the range of each element in studentScore_list
	for i in range(0, len(studentScore_list)):
		if float(studentScore_list[i]) == 0:
			nerdCount_list[0] += 1
		if float(studentScore_list[i]) in range(1, 10):
			nerdCount_list[1] += 1
		if float(studentScore_list[i]) in range(10, 100):
			nerdCount_list[2] += 1
		if float(studentScore_list[i]) in range(100, 500):
			nerdCount_list[3] += 1
		if float(studentScore_list[i]) in range(500, 1000):
			nerdCount_list[4] += 1
		if float(studentScore_list[i]) in range(1000, 2000):
			nerdCount_list[5] += 1
		if float(studentScore_list[i]) >= 2000:
			nerdCount_list[6] += 1

	return nerdCount_list

	
if __name__ == '__main__':

	#test cases
	#studentScore_list = []  #
	studentScore_list = [23, 76, 1300, 600]   #output should be [0, 0, 2, 0, 1, 1, 0]

	try:
		print(countStudentClass(studentScore_list))
	
	except e:
		print(e)
		raise	
