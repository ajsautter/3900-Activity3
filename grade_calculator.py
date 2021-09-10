# Andrew Sautter
# ISQA 3900 9/10/2021
#The purpose of this program is to be able to input values and those values
# be converted to a grading system

def display_title():
    #initial prompt to the user
    print("Welcome to Grade Calculator")

#function to ask user for point value, add null value preventions
def get_totalPoints():
    #input function for getting the score
    gradeScore = float(input("Enter your total points earned for term:\t"))
    if gradeScore <= 0:
        print("Your value must be a positive number")
    return gradeScore

def get_letterGrade(averageEarned):
   #initializing the variable but having the conditionals declare it.
    letterGrade = ""
    print("we are in get_letterGrade")
    if 920 <= averageEarned >= 1000:
        letterGrade = "A"
    elif 919 <= averageEarned >= 880:
        letterGrade = "B+"
    elif 879 <= averageEarned >= 820:
        letterGrade = "B"
    elif 819 <= averageEarned >= 780:
        letterGrade = "C+"
    elif 779 <= averageEarned >= 720:
        letterGrade = "C"
    elif 719 <= averageEarned >= 680:
        letterGrade = "D+"
    elif 679 <= averageEarned >= 600:
        letterGrade = "D"
    elif 599 >= averageEarned:
        letterGrade = "F"

    return print("You earned an average of ", averageEarned/1000*100, "\tThe letter grade is ",  letterGrade)
def main():
    display_title()
    choice = input("Would you like to enter a grade?\t")
    while choice.lower() == "y":
        averageEarned = get_totalPoints()
        letterGrade = get_letterGrade(averageEarned)
    #print("You earned an average of ", averageEarned/1000*100, "\tThe letter grade is ",  letterGrade)
    #intially tried to have the print in this main but I couldn't get a str variable out of the
    # get_lettergrade function
        choice = input("Continue? (y/n) ")
    print("Thank you for using the problem!")
    print()


if __name__ == "__main__":
    main()