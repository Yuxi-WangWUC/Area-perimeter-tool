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
def string_checker(choice, option):
    is_valid = ""
    chosen = ""

    for var_list in option:
        # if the shape is in one of the lists, return the full response
        if choice in var_list:
            # get full name of shape and put it in title case
            chosen = var_list[0].title()
            is_valid = "yes"
            break
        # if the chosen option is invalid, set is_valid to no
        else:
            is_valid = "no"

    # if the snack is not ok - repeat the question again
    if is_valid == "yes":
        return chosen
    else:
        return "invalid choice"


# get lists of shapes
def get_shape():
    # valid shapes holds list of all shapes
    # each item in valid snacks is a list with valid options (full name,
    # initial or first three letter)
    valid_shapes = [
    ["triangle", "tri"],
    ["Rectangle", "r"],
    ["circle", "c"],
    ["parallelogram", "p"],
    ["trapezium", "tra"]
]

    # list holds shape list
    shape_list = []
    expect_shape = ""

    while expect_shape != "xxx":
        # ask user for expect shape and put it in lowercase
        expect_shape = input("Shape: ").lower().strip()

        if expect_shape == "xxx":
            return shape_list
        # check the shape if it's valid
        shape_choice = string_checker(expect_shape, valid_shapes)
        print("You had chosen: ", shape_choice)

        # add shape to list
        # check that snack is not exit code before adding
        if shape_choice != "xxx" and shape_choice != "invalid choice":
            shape_list.append(shape_choice)




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
yes_no_list = [["yes", "y"], ["no", "n"]]



# set up main***************************************************

# introduction to users and get shapes


# initialise loops so that it runs at least once
shape_list = []
expect_shape = ""
shape = ""
num_shape = 0
MAX_QUE = 5
min_len = 0
max_len = 10000
# initialise variables
shape_ok = ""
shapes = ""

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

    if len(shape_list) != 0:
        print("Shape chosen: ")
        for item in shape_list:
            print(item)

            for var_list in valid_shapes:
                # if the snack is in one of the lists, return the full response
                if expect_shape in var_list:
                    # get full name of shape and put it in title case,
                    # so it looks normative when output
                    shapes = var_list[0].title()
                    shape_ok = "yes"
                    break

                # if the chosen snack is not valid, set snack_ok to no
                else:
                    shape_ok = "no"


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


