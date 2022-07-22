"""
tool for calculate the area and perimeter for different shapes
string checker component
v1 component string checker - check to make sure the function is called
v2 set up valid shapes holds list of all shapes
"""

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

# initialise variables
shape_ok = ""
shapes = ""


# loop three times to make a quick testing
for item in range(0,3):
    # ask user for expect snack and put it in lowercase
    expect_shape = input("Shape: ").lower()

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
