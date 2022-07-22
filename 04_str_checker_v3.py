"""
tool for calculate the area and perimeter for different shapes
string checker component
v1 component string checker - check to make sure the function is called
v2 set up valid shapes holds list of all shapes
v3 combine v2 into v1 and chance some variables
"""


# string checking functions, takes in
# question and list of valid responses
def string_checker(choice, option):
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


# main routine
for item in range(0, 5):
    # ask user for expect snack and put it in lowercase
    expect_shape = input("Shape: ").lower()

    # check the shape if it's valid
    shape_choice = string_checker(expect_shape, valid_shapes)

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
    # if the shape is not ok - repeat the question again
    if shape_ok == "yes":
        print("You had chosen: ", shapes)
    else:
        print("Please enter a valid choice")

# initialise variables
shape_ok = ""
shapes = ""
