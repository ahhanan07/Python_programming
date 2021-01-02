# Author: ABDUL HANAN
# Start Date: 30th March 2019
# Last Modified Date: 11th April 2019

# Importing files to be used in menu() function
import skillEquation_30340284
import findClass_30340284


# define a function menu()
def menu():
    # Initializing Variables to store user input
    # Default values set to None
    fandom_number = None
    hobbies_score = None
    sports_played = None
    print("Welcome \n 1. Fandom Score \n 2. Hobbies Score \n "
          "3. Sports Played \n 4. Calculate Nerd Score \n "
          "5. Print Nerd rating of student\n 6. Restart the program \n 7. Exit program")

    # Input () method is used to get inputs from users
    # While loop is used to continuously ask the user to enter choices and inputs.
    # Try-except is used to check for value errors
    # Multiple if-else conditions are used to check for various limitations
    # Print () statement is used to interact with user at various occasions

    while True:
        try:
            choice = int(input("ENTER YOUR CHOICE\n"))

            if choice == 1:
                fandom_number = int(input("Enter fandom score\n"))
                if fandom_number < 0:
                    print("INVALID: Negative fandom score \n")
                    fandom_number = None

                if fandom_number == 0:
                    print("INVALID: Fandom score is zero")
                    fandom_number = None
                print("Welcome \n 1. Fandom Score   {} \n 2. Hobbies Score   {} \n "
                      "3. Sports Played   {}\n 4. Calculate Nerd Score \n "
                      "5. Print Nerd rating of student \n 6. Restart Program \n 7. Exit program".
                      format(fandom_number, hobbies_score, sports_played))

            elif choice == 2:
                hobbies_score = int(input("Enter hobbies score\n"))
                if hobbies_score < 0 or hobbies_score % 4 != 0:
                    print("INVALID : Enter zero or multiple of FOUR")
                    hobbies_score = None
                print("Welcome \n 1. Fandom Score    {} \n 2. Hobbies Score   {} \n "
                      "3. Sports Played   {}\n 4. Calculate Nerd Score \n "
                      "5. Print Nerd rating of student \n 6. Restart Program \n 7. Exit program".
                      format(fandom_number, hobbies_score, sports_played))

            elif choice == 3:
                sports_played = int(input("Enter number of sports played \n"))
                if sports_played < 0:
                    print("INVALID : Enter positive integer value")
                    sports_played = None
                print("Welcome \n 1. Fandom Score    {} \n 2. Hobbies Score   {} \n "
                      "3. Sports Played   {}\n 4. Calculate Nerd Score \n "
                      "5. Print Nerd rating of student \n 6. Restart program \n 7. Exit program".
                      format(fandom_number, hobbies_score, sports_played))

            # Calculation of NerdScore by importing nerdScore_30340284.py
            # calculateSkillEquation () method from skillEquation.py is used to calculate the nerd score.
            # Fandom score, hobbies score and sports played variables are passed into the calculateSkillEquation ()

            elif choice == 4:

                if fandom_number is not None and hobbies_score is not None and sports_played is not None:
                    print("Nerd Score is : {}".
                          format(skillEquation_30340284.calculateSkillEquation(fandom_number, hobbies_score, sports_played)))
                if fandom_number is None:
                    print("Fandom score missing\n")
                if hobbies_score is None:
                    print("Hobbies Score Missing\n")
                if sports_played is None:
                    print("Number of sports played is missing\n")

            # Multiple NerdScores are taken and their class is determined by importing findClass_30340284.py
            # A variable class_list is defined which stores different nerd classes in the form of list
            # Method countStudentClass () is used to determine the classes based on input studentScore_list
            # Finally, the method output is zipped with class_list and displayed as a dictionary using dict () function

            elif choice == 5:
                student_scores = input("Input nerd scores separated by spaces\n")
                studentScore_list = student_scores.split()
                class_list = ["Nerdlite", "Nerdling", "Nerdlinger", "Nerd", "Nerdington", "Nerdrometa", "Nerd Supreme"]
                nerdlist = findClass_30340284.countStudentClass(studentScore_list)
                if nerdlist == 0:
                    pass
                else:
                    print("CLASS \n {}".format(dict(zip(class_list, nerdlist))))
                menu()

            elif choice == 6:
                    menu()        # Restart program by calling menu() function

            elif choice == 7:
                exit()        # User wants to exit the program

            else:
                print("Enter valid choice {1, 2, 3, 4, 5, 6 or 7})")   # User integer input out of range {1,2,3,4,5,6,7}

        except ValueError:
            print("INVALID : Enter Integer input")             #
menu()
