"""
tool to calculate the area and perimeter of different shapes
base component
v1 - set up the skeleton of the program, test the functions are called as required
v2 - trial random generator function component. Works well so will keep it
Yuxi Wang
"""

# set up functions**********************************************


def not_blank(question):
    valid = False

    while not valid:
        response = input(question)
        # if the response is not blank, program continues
        if response != "":
            return response
        # if the response is blank, show error and repeat loop
        else:
            print("Sorry, this can't be blank, "
                  "please enter a valid shape")

# function to check for integers. will loop until an integer is input

# check for an integer between 2 values
def int_checker():

    error = "Please enter a number between 0 and 10000"

    valid = False
    while not valid:

        # ask user for a positive  and check it is valid
        try:
            response = float(input(question))

            if response <= 0 or response >= 10000:
                print(error)
            else:
                return response
        # if a number is not entered, display an error
        except ValueError:
            print(error)


# function to check string is within an allowable list. Will loop until an allowable word is input
def string_checker(list_of_allowable):
    print("placeholder")


# function to calculate the area and perimeter for triangle
def triangle():
    print("triangle function")


# function to calculate the area and perimeter for rectangle
def rectangle():
    print("rectangle function")


# function to calculate the area and perimeter for circle
def circle():
    print("circle function")


# function to calculate the area and perimeter for parallelogram
def parallelogram():
    print("parallelogram function")


# function to calculate the area and perimeter for trapezium
def trapezium():
    print("trapezium function")


# set up lists and constants***********************************
answer_list = []
yes_no_list = [["yes", "y"],["no","n"]]
shapes = ["triangle", "rectangle", "circle", "parallelogram", "trapezium"]


# set up main***************************************************

# introduction to users and get shapes
if __name__ == "__main__":
    # set local variables within the main routine
    min_num = 0
    max_num = 5

    print("placeholder")
    # ask users for input
    print("*******************MATH GAME****************************")
    print("**")
    print("** Welcome to my Area & Perimeter calculator ")
    # get shape (no blank)
    shape = input("Please choose a shape between triangle, rectangle, circle, parallelogram and trapezium")
    # check shape for legitimacy
    # string check - send the list of shapes

    # ask user for the dimensions.
    # int checker to check it's an integer, loop until suitable integer

    # ask user for their answer and check against it
    # int checker to check on the integer
    num_questions = 1

    # loop until number of questions is asked
    for questions in range(0, num_questions):
        # print("placeholder")
        if shape == "triangle" or shape == "t":
            # print("go to triangle")
            triangle()
        elif shape == "rectangle" or shape == "r":
            # print("got to rectangle")
            rectangle()
        elif shape == "circle" or shape == "c":
            # print("go to circle")
            circle()
        elif shape == "parallelogram" or shape == "p":
            # print("go to parallelogram")
            parallelogram()
        elif shape == "trapezium" or shape == "tra":
            # print("go to trapezium")
            trapezium()
        else:
            shape = not_blank("Please enter a shape you want to calculate: ")


# initialise loops so that it runs at least once
shape = ""
num_shape = 0
MAX_QUE = 5
min_len = 0
max_len = 10000

while shape != "xxx" and num_shape < MAX_QUE:
    # tell user how many times they can ask for help
    if num_shape < MAX_QUE - 1:
        print("You can ask {} more "
              "questions".format(MAX_QUE - num_shape))
    # warn users that they can only ask one more question
    else:
        print("You can ask one more question")

    # Get details...
    shape = input("Shape: ")
    if shape != "xxx":
        num_shape += 1
    else:
        num_shape += 0
    print()

# tell users how many questions they had asked and how many they can ask next
if num_shape == MAX_QUE:
    print("You had ask {} questions".format(num_shape))
elif num_shape == MAX_QUE - 1:
    print("You had ask {} questions.  \n"
          "You can ask one more question."
          .format(num_shape, MAX_QUE - num_shape))
else:
    print("You had ask {} question.  \n"
          "You can ask {} more questions."
          .format(num_shape, MAX_QUE - num_shape))


