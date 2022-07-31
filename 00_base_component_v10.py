"""
tool to calculate the area and perimeter of different shapes
base component
v1 - set up the skeleton of the program, test the functions are called as required
v2 - trial random generator function component. Works well so will keep it
Yuxi Wang
"""

import pandas

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
def int_check(questions):

    error = "Please enter a number between 0 and 10000"

    valid = False
    while not valid:

        # ask user for a positive  and check it is valid
        try:
            response = float(input(questions))

            if response <= 0 or response >= 10000:
                print(error)
            else:
                return round(response, 2)
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

    # if the shape is not ok - repeat the question again
    if is_valid == "yes":
        return chosen
    else:
        return "invalid choice"


# set up lists and constants***********************************
answer_list = []


# set up main***************************************************

# introduction to users and get shapes
if __name__ == "__main__":
    # initialise loops so that it runs at least once
    num_shape = 0
    MAX_QUE = 5
    min_len = 0
    max_len = 10000

    print("placeholder")
    # ask users for input
    print("*******************MATH GAME****************************")
    print("**")
    print("** Welcome to my Area & Perimeter calculator ")

    # check shape for legitimacy
    # string check - send the list of shapes
    valid = True  # valid must re-initialised every time it is run in a loop
    # valid shapes holds list of all shapes
    # each item in valid shapes is a list with valid options (full name,
    # initial or first three letter)
    valid_shapes = [
        ["triangle", "tri"],
        ["rectangle", "r"],
        ["circle", "c"],
        ["parallelogram", "p"],
        ["trapezium", "tra"]]

    # holds shape list for a single user
    shape_list = ""
    expect_shape = ""
    shape_err = "This is not a valid answer. Please try again"
    shape_que = []

    # initialise shapes lists
    hyp_1 = []
    hyp_2 = []
    height = []
    radius = []
    base_u = []
    base_d = []
    perimeter = []
    area = []
    summary_list = [hyp_1, hyp_2, height, radius, base_u, base_d, perimeter, area]

    while expect_shape != "xxx" and MAX_QUE != num_shape:
        # ask user for expect shape and put it in lowercase
        print()
        expect_shape = input("Choose a shape to be calculated: ").lower().strip()

        # check the shape if it's valid
        shape_choice = string_checker(expect_shape, valid_shapes)

        # add shape to list
        # check that shape is not exit code before adding
        if shape_choice != "xxx" and shape_choice != "invalid choice":
            print("You had chosen: ", shape_choice)
            shape_list += shape_choice
            num_shape += 1

        elif expect_shape == "xxx":
            print("You had stopped the program.")
        else:
            print("This is a invalid choice, please enter again.")

        # ask the users for the dimensions
        if expect_shape == "xxx":
            num_shape += 0
            break

        # if triangle is chosen
        elif expect_shape == "triangle" or expect_shape == "tri":
            base_tri = int_check("Base: ")
            hypotenuse_tri_1 = int_check("First hypotenuse: ")
            hypotenuse_tri_2 = int_check("Second hypotenuse: ")
            height_tri = int_check("Height: ")
            ans_tri_peri = int_check("Answer for perimeter: ")

            total_tri_peri = round((hypotenuse_tri_1 + hypotenuse_tri_2 + base_tri), 2)
            if ans_tri_peri != total_tri_peri:
                print("Sorry, this is incorrect. The real answer is {:.2f}.".format(total_tri_peri))
            else:
                print("This is the correct answer. Well done")

            ans_tri_area = int_check("Answer for area: ")
            total_tri_area = round((base_tri * height_tri / 2), 2)
            if total_tri_area != ans_tri_area:
                print("Sorry, this is incorrect. The real answer is {:.2f}.".format(total_tri_area))
            else:
                print("This is the correct answer. Well done")

            # attend data to the lists
            hyp_1.append(hypotenuse_tri_1)
            hyp_2.append(hypotenuse_tri_2)
            base_d.append(base_tri)
            height.append(height_tri)
            perimeter.append(total_tri_peri)
            area.append(total_tri_area)

        # if rectangle is chosen
        elif expect_shape == "rectangle" or expect_shape == "r":
            height_r = int_check("Height: ")
            base_r = int_check("Base: ")
            ans_r_peri = int_check("Answer for perimeter in 2 decimal places: ")

            total_r_peri = round((height_r + base_r) * 2, 2)
            if ans_r_peri != total_r_peri:
                print("Sorry, this is incorrect. The real answer is {:.2f}.".format(total_r_peri))
            else:
                print("This is the correct answer. Well done")

            ans_r_area = int_check("Answer for area in 2 decimal places: ")
            total_r_area = round(base_r * height_r, 2)
            if total_r_area != ans_r_area:
                print("Sorry, this is incorrect. The real answer is {:.2f}.".format(total_r_area))
            else:
                print("This is the correct answer. Well done")

            # attend data to the lists
            base_u.append(base_r)
            base_d.append(base_r)
            height.append(height_r)
            perimeter.append(total_r_peri)
            area.append(total_r_area)

        # if circle is chosen
        elif expect_shape == "circle" or expect_shape == "c":
            radius_c = int_check("Radius, π = 3.14: ")
            ans_c_cir = int_check("Answer for circumference in 2 decimal places: ")
            pi = 3.14

            total_c_cir = round(radius_c * 2 * pi, 2)
            if ans_c_cir != total_c_cir:
                print("Sorry, this is incorrect. The real answer is {:.2f}.".format(total_c_cir))
            else:
                print("This is the correct answer. Well done")

            ans_c_area = int_check("Answer for area in 2 decimal places: ")
            total_c_area = round(radius_c * radius_c * pi, 2)
            if total_c_area != ans_c_area:
                print("Sorry, this is incorrect. The real answer is {:.2f}.".format(total_c_area))
            else:
                print("This is the correct answer. Well done")

            # attend data to the lists
            radius.append(radius_c)
            perimeter.append(total_c_cir)
            area.append(total_c_area)

        # if parallelogram is chosen
        elif expect_shape == "parallelogram" or expect_shape == "p":
            hypotenuse_p = int_check("Hypotenuse: ")
            height_p = int_check("Height: ")
            base_p = int_check("Base: ")

            ans_p_peri = int_check("Answer for perimeter in 2 decimal places: ")
            total_p_peri = round((base_p + hypotenuse_p)*2, 2)
            if ans_p_peri != total_p_peri:
                print("Sorry, this is incorrect. The real answer is {:.2f}.".format(total_p_peri))
            else:
                print("This is the correct answer. Well done")

            ans_p_area = int_check("Answer for area in 2 decimal places: ")
            total_p_area = round(base_p * height_p, 2)
            if total_p_area != ans_p_area:
                print("Sorry, this is incorrect. The real answer is {:.2f}.".format(total_p_area))
            else:
                print("This is the correct answer. Well done")
            # attend data to the lists
            hyp_1.append(hypotenuse_p)
            hyp_2.append(hypotenuse_p)
            base_u.append(base_p)
            base_d.append(base_p)
            height.append(height_p)
            perimeter.append(total_p_peri)
            area.append(total_p_area)

        # if trapezium is chosen
        elif expect_shape == "trapezium" or expect_shape == "tra":
            hypotenuse_tra_1 = int_check("First hypotenuse: ")
            hypotenuse_tra_2 = int_check("Second hypotenuse: ")
            base_tra_1 = int_check("First base: ")
            base_tra_2 = int_check("Second base: ")
            height_tra = int_check("Height: ")

            ans_tra_peri = int_check("Answer for perimeter in 2 decimal places: ")
            total_tra_peri = round((base_tra_1 + base_tra_2 + hypotenuse_tra_1 + hypotenuse_tra_2), 2)
            if ans_tra_peri != total_tra_peri:
                print("Sorry, this is incorrect. The real answer is {:.2f}.".format(total_tra_peri))
            else:
                print("This is the correct answer. Well done")

            ans_tra_peri = int_check("Answer for area in 2 decimal places: ")
            total_tra_peri = round((base_tra_1 + base_tra_2) * height_tra / 2, 2)
            if total_tra_peri != ans_tra_peri:
                print("Sorry, this is incorrect. The real answer is {:.2f}.".format(total_tra_peri))
            else:
                print("This is the correct answer. Well done")

            # attend data to the lists
            hyp_1.append(hypotenuse_tra_1)
            hyp_2.append(hypotenuse_tra_2)
            base_u.append(base_tra_1)
            base_d.append(base_tra_2)
            height.append(height_tra)
            perimeter.append(total_tra_peri)
            area.append(total_tra_peri)

        # tell users how many questions they asked
        if num_shape == MAX_QUE:
            print("You had asked {} questions. "
                  "You can ask no more question.".format(num_shape))
        elif 1 < num_shape < MAX_QUE - 1:
            print("You had asked {} questions. "
                  "You can ask {} more questions".format(num_shape, MAX_QUE - num_shape))
        elif num_shape == MAX_QUE - 1:
            print("You had asked {} question. "
                  "You can ask one more question.".format(num_shape))
        elif num_shape == 0:
            print("You had asked 0 question. "
                  "You can ask {} more questions".format(MAX_QUE))
        else:
            print("You had asked 1 question. "
                  "You can ask {} more questions.".format(MAX_QUE - num_shape))

        shape_data_dict = {
            'Shape': shape_list,
            'First hypotenuse': hyp_1,
            'Second hypotenuse': hyp_2,
            'Height': height,
            'Radius': radius,
            'Upper base': base_u,
            'Down base': base_d,
            "Perimeter": perimeter,
            "Area": area
        }

        count = 0
        for user_que in test_data:
            # assume no dimension have been entered
            for item in summary_list:
                item.append(0)

            # print shape lists
            # get summary
            shape_cal = test_data[count]
            count += 1

            for item in shape_cal:
                if len(item) > 0:
                    to_find = (item[1])
                    amount = (item[0])
                    add_list = shape_data_dict[to_find]
                    add_list[-1] = amount

        # create dataframe and set index to shape column
        shape_frame = pandas.DataFrame(shape_data_dict)
        shape_frame = shape_frame.set_index('Shape')

        # shorten column names
        shape_frame = shape_frame.rename(columns={'First hypotenuse': 'Hyp 1',
                                                  'Second hypotenuse': 'Hyp 2',
                                                  'Upper base': 'Base U',
                                                  'Down base': 'Base D'})

        # print summary
        print("*** Shape Calculation Tool Summary ***")
        print(shape_frame)

    shape_data_dict = {
        'Shape': shape_list,
        'Hyp_1': hyp_1,
        'Hyp_2': hyp_2,
        'Height': height,
        'Radius': radius,
        'Base_u': base_u,
        'Base_d': base_d,
        "Perimeter": perimeter,
        "Area": area
    }

    dota_teams = ['hyp_1', 'hyp_2', 'height', 'radius', 'base_u', 'base_d', 'perimeter', 'area']

    format_row = "{:>10}" * (len(dota_teams) + 1)
    print(format_row.format("", *dota_teams))
    for team, row in zip(dota_teams, shape_list):
        print(format_row.format(team, *row))
