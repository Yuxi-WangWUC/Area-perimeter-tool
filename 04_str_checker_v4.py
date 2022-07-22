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


# holds shape list for a single user
shape_list = []
expect_shape = ""
# loop to get shapes from the user
while expect_shape != "xxx":
    # ask user for expect shape and put it in lowercase
    expect_shape = input("Shape: ").lower()

    if expect_shape == "xxx":
        break
    # check the shape if it's valid
    shape_choice = string_checker(expect_shape, valid_shapes)
    print("You had chosen: ", shape_choice)

    # add shape to list
    # check that snack is not exit code before adding
    if shape_choice != "xxx" and shape_choice != "invalid choice":
        shape_list.append(shape_choice)


# show shape list
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

# initialise variables
shape_ok = ""
shapes = ""
