"""
tool to calculate the area and perimeter of different shapes
base component
v1 - set up the skeleton of the program, test the functions are called as required
v2 - trial random generator function component. Works well so will keep it
Yuxi Wang
"""

# set up functions**********************************************


# function to check for integers. will loop until an integer is input
def int_checker():
    print("placeholder")


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

# set up lists and constants************************************


answer_list = []
yes_no_list = [["yes", "y"],["no","n"]]
shapes = ["triangle", "rectangle", "circle", "parallelogram", "trapezium"]


# set up main***************************************************
if __name__ == "__main__":
    # set local variables within the main routine
    min_num = 0
    max_num = 5

    print("placeholder")
    # ask users for input
    print("*******************MATH GAME****************************")
    print("**")
    print("** Welcome to my Area & Perimeter calculator ")
    shape = input("** Choose an shape for your game: triangle, rectangle, circle, parallelogram or trapezium ")
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
        if shape == "triangle" or "t":
            # print("go to triangle")
            triangle()
        elif shape == "rectangle" or "r":
            # print("got to rectangle")
            rectangle()
        elif shape == "circle" or "c":
            # print("go to circle")
            circle()
        elif shape == "parallelogram" or "p":
            # print("go to parallelogram")
            parallelogram()
        else:
            # print("go to trapezium")
            trapezium()


