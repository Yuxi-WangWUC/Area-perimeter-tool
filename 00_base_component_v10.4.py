"""
tool to calculate the area and perimeter of different shapes
base component
v1 - set up the skeleton and no_blank function of the program, test the functions are called as required
v2 - set up the while loop under the main routine
v3 - set up the int_checker function
v4 - set up the lists that may use later and string checker
v5-v9 - set yp the calculation for all the shapes
v10 - print out the summary
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

    error = "Sorry, this is a invalid response. Please enter a positive number."

    valid = False
    while not valid:

        # ask user for a positive  and check it is valid
        try:
            response = float(input(questions))

            if response <= 0:
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
    print("** Welcome to my Area & Perimeter calculator tool ")
    print("You can choose five shapes to calculate: Triangle, "
          "Rectangle, Circle, Parallelogram and Trapezium ")
    print("You can also enter the letter code: tri, r, c, p, tra for five shapes")
    print("Type xxx to stop the code")
    print("So let's start it!")

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
    shape_list = []
    expect_shape = ""
    shape_err = "This is not a valid answer. Please try again"
    shape_que = []

    # create the lists for triangle to print out later
    triangle = 0
    hyp_tri_l = []
    hyp_tri_r = []
    h_tri = []
    base_tri = []
    peri_tri = []
    area_tri = []

    # create the lists for rectangle to print out later
    rectangle = 0
    base_r = []
    h_r = []
    peri_r = []
    area_r = []

    # create the lists for circle to print out later
    circle = 0
    r_c = []
    peri_c = []
    area_c = []

    # create the lists for parallelogram to print out later
    parallelogram = 0
    hyp_p = []
    h_p = []
    base_p = []
    peri_p = []
    area_p = []

    # create the lists for trapezium to print out later
    trapezium = 0
    hyp_tra_l = []
    hyp_tra_r = []
    h_tra = []
    base_tra_u = []
    base_tra_d = []
    peri_tra = []
    area_tra = []

    while expect_shape != "xxx" and MAX_QUE != num_shape:
        # ask user for expect shape and put it in lowercase
        print()
        expect_shape = input("Let's choose a shape to calculate: ").lower().strip()

        # check the shape if it's valid
        shape_choice = string_checker(expect_shape, valid_shapes)

        # add shape to list
        # check that shape is not exit code before adding
        if shape_choice != "xxx" and shape_choice != "invalid choice":
            print("You have chosen: ", shape_choice)
            shape_list.append(shape_choice)
            num_shape += 1

        elif expect_shape == "xxx":
            print("You have stopped the program.")
        else:
            print("Sorry, this is a invalid choice, please enter again.")

        # ask the users for the dimensions
        if expect_shape == "xxx":
            num_shape += 0
            break

        # if triangle is chosen
        elif expect_shape == "triangle" or expect_shape == "tri":

            # ask for dimensions
            base_triangle = round(int_check("Please enter the length for Base: "), 2)
            hypotenuse_tri_l = round(int_check("Please enter the length for Left hypotenuse: "), 2)
            hypotenuse_tri_r = round(int_check("Please enter the length for Right hypotenuse: "), 2)
            height_tri = round(int_check("Please enter the length for Height: "), 2)
            ans_tri_peri = round(int_check("Please enter your answer for Perimeter: "), 2)

            total_tri_peri = round((hypotenuse_tri_l + hypotenuse_tri_r + base_triangle), 2)
            if ans_tri_peri != total_tri_peri:
                print("Oops, this is incorrect. The real answer is {:.2f}. You can get it next time!".format(total_tri_peri))
            else:
                print("Wow, this is the correct answer! Well done! You are getting there!")

            ans_tri_area = round(int_check("Please enter your answer for Area: "), 2)
            total_tri_area = round((base_triangle * height_tri / 2), 2)
            if total_tri_area != ans_tri_area:
                print("Oops, this is incorrect. The real answer is {:.2f}. You can get it next time!.".format(total_tri_area))
            else:
                print("Wow, this is the correct answer! Well done! You are getting there!")

            # attend data to the lists
            triangle += 1
            hyp_tri_l.append(hypotenuse_tri_l)
            hyp_tri_r.append(hypotenuse_tri_r)
            base_tri.append(base_triangle)
            h_tri.append(height_tri)
            peri_tri.append(total_tri_peri)
            area_tri.append(total_tri_area)

        # if rectangle is chosen
        elif expect_shape == "rectangle" or expect_shape == "r":

            # ask for dimensions
            height_r = round(int_check("Please enter the length for Height: "), 2)
            base_rectangle = round(int_check("Please enter the length for Base: "), 2)
            ans_r_peri = round(int_check("Please enter your answer for Perimeter: "), 2)

            total_r_peri = round((height_r + base_rectangle) * 2, 2)
            if ans_r_peri != total_r_peri:
                print("Oops, this is incorrect. The real answer is {:.2f}. You can get it next time!".format(total_r_peri))
            else:
                print("Wow, this is the correct answer! Well done! You are getting there!")

            ans_r_area = round(int_check("Please enter your answer for Area: "), 2)
            total_r_area = round(base_rectangle * height_r, 2)
            if total_r_area != ans_r_area:
                print("Oops, this is incorrect. The real answer is {:.2f}. You can get it next time!".format(total_r_area))
            else:
                print("Wow, this is the correct answer! Well done! You are getting there!")

            # attend data to the lists
            rectangle += 1
            base_r.append(base_rectangle)
            h_r.append(height_r)
            peri_r.append(total_r_peri)
            area_r.append(total_r_area)

        # if circle is chosen
        elif expect_shape == "circle" or expect_shape == "c":

            # ask for dimensions
            radius_c = round(int_check("Please enter the length for Radius (π = 3.14): "), 2)
            ans_c_cir = round(int_check("Please enter your answer for Circumference: "), 2)
            pi = 3.14

            total_c_cir = round(radius_c * 2 * pi, 2)
            if ans_c_cir != total_c_cir:
                print("Oops, this is incorrect. The real answer is {:.2f}. You can get it next time!".format(total_c_cir))
            else:
                print("Wow, this is the correct answer! Well done! You are getting there!")

            ans_c_area = round(int_check("Please enter your answer for Area: "), 2)
            total_c_area = round(radius_c * radius_c * pi, 2)
            if total_c_area != ans_c_area:
                print("Oops, this is incorrect. The real answer is {:.2f}. You can get it next time!".format(total_c_area))
            else:
                print("Wow, this is the correct answer! Well done! You are getting there!")

            # attend data to the lists
            circle += 1
            r_c.append(radius_c)
            peri_c.append(total_c_cir)
            area_c.append(total_c_area)

        # if parallelogram is chosen
        elif expect_shape == "parallelogram" or expect_shape == "p":

            # ask for dimensions
            hypotenuse_p = round(int_check("Please enter the length for Hypotenuse: "), 2)
            height_p = round(int_check("Please enter the length for Height: "), 2)
            base_parallelogram = round(int_check("Please enter the length for Base: "), 2)

            ans_p_peri = round(int_check("Please enter your answer for Perimeter: "), 2)
            total_p_peri = round((base_parallelogram + hypotenuse_p)*2, 2)
            if ans_p_peri != total_p_peri:
                print("Oops, this is incorrect. The real answer is {:.2f}. You can get it next time!".format(total_p_peri))
            else:
                print("Wow, this is the correct answer! Well done! You are getting there!")

            ans_p_area = round(int_check("Please enter your answer for Area: "), 2)
            total_p_area = round(base_parallelogram * height_p, 2)
            if total_p_area != ans_p_area:
                print("Oops, this is incorrect. The real answer is {:.2f}. You can get it next time!".format(total_p_area))
            else:
                print("Wow, this is the correct answer! Well done! You are getting there!")

            # attend data to the lists
            parallelogram += 1
            hyp_p.append(hypotenuse_p)
            base_p.append(base_parallelogram)
            h_p.append(height_p)
            peri_p.append(total_p_peri)
            area_p.append(total_p_area)

        # if trapezium is chosen
        elif expect_shape == "trapezium" or expect_shape == "tra":

            # ask for dimensions
            hyp_left_tra = round(int_check("Please enter the length for Left hypotenuse: "), 2)
            hyp_right_tra = round(int_check("Please enter the length for Right hypotenuse: "), 2)
            base_trapezium_u = round(int_check("Please enter the length for Upper base: "), 2)
            base_trapezium_d = round(int_check("Please enter the length for Down base: "), 2)
            height_tra = round(int_check("Please enter the length for Height: "), 2)

            ans_tra_peri = round(int_check("Please enter your answer for Perimeter: "), 2)
            total_tra_peri = round((base_trapezium_u + base_trapezium_d + hyp_left_tra + hyp_right_tra), 2)
            if ans_tra_peri != total_tra_peri:
                print("Oops, this is incorrect. The real answer is {:.2f}. You can get it next time!".format(total_tra_peri))
            else:
                print("Wow, this is the correct answer! Well done! You are getting there!e")

            ans_tra_peri = round(int_check("Please enter your answer for Area: "), 2)
            total_tra_area = round((base_trapezium_u + base_trapezium_d) * height_tra / 2, 2)
            if total_tra_peri != ans_tra_peri:
                print("Oops, this is incorrect. The real answer is {:.2f}. You can get it next time!".format(total_tra_peri))
            else:
                print("Wow, this is the correct answer! Well done! You are getting there!")

            # attend data to the lists
            trapezium += 1
            hyp_tra_l.append(hyp_left_tra)
            hyp_tra_r.append(hyp_right_tra)
            base_tra_u.append(base_trapezium_u)
            base_tra_d.append(base_trapezium_d)
            h_tra.append(height_tra)
            peri_tra.append(total_tra_peri)
            area_tra.append(total_tra_area)

        # tell users how many questions they asked
        if shape_choice != "xxx" and shape_choice != "invalid choice":
            if num_shape == MAX_QUE:
                print("You have asked {} questions. "
                      "You can ask no more question.".format(num_shape))
            elif 1 < num_shape < MAX_QUE - 1:
                print("You have asked {} questions. "
                      "You can ask {} more questions".format(num_shape, MAX_QUE - num_shape))
            elif num_shape == MAX_QUE - 1:
                print("You have asked {} question. "
                      "You can ask one more question.".format(num_shape))
            elif num_shape == 0:
                print("You have asked 0 question. "
                      "You can ask {} more questions".format(MAX_QUE))
            else:
                print("You have asked 1 question. "
                      "You can ask {} more questions.".format(MAX_QUE - num_shape))

    print()
    print("*****************************************")
    print("Let's look at your calculation summary")

    # print out what shapes the users asked
    if len(shape_list) > 1:
        print("You have asked {} shapes:{}".format(len(shape_list), shape_list))
    else:
        print("You have asked {} shape:{}".format(len(shape_list), shape_list))
    print("Here is the data for the calculation: ")

    # summary for triangle
    if triangle > 1:
        print("Triangles:")

        print("Left Hypotenuses: {}".format(hyp_tri_l))

        print("Right Hypotenuses: {}".format(hyp_tri_r))

        print("Bases: {}".format(base_tri))

        print("Heights: {} ".format(h_tri))

        print("Perimeters: {}".format(peri_tri))

        print("Areas: {}".format(area_tri))

    elif triangle == 1:
        print("Triangle:")

        print("Left Hypotenuse: {}".format(hyp_tri_l))

        print("Right Hypotenuse: {}".format(hyp_tri_r))

        print("Base: {}".format(base_tri))

        print("Height: {} ".format(h_tri))

        print("Perimeter: {}".format(peri_tri))

        print("Area: {}".format(area_tri))

    print()

    # summary for rectangle
    if rectangle > 1:
        print("Rectangles: ")

        print("Bases: {}".format(base_r))

        print("Heights: {}".format(h_r))

        print("Perimeters: {}".format(peri_r))

        print("Areas: {}".format(area_r))

    elif rectangle == 1:
        print("Rectangle: ")

        print("Base: {}".format(base_r))

        print("Height: {}".format(h_r))

        print("Perimeter: {}".format(peri_r))

        print("Area: {}".format(area_r))

    print()

    # summary for circle
    if circle > 1:
        print("Circles: ")

        print("Radii: {}".format(r_c))

        print("Circumferences: {}".format(peri_c))

        print("Areas: {}".format(area_c))

    elif circle == 1:
        print("Circle: ")

        print("Radius: {}".format(r_c))

        print("Circumference: {}".format(peri_c))

        print("Area: {}".format(area_c))

    print()

    # summary for parallelogram
    if parallelogram > 1:
        print("Parallelograms: ")

        print("Hypotenuses: {}".format(hyp_p))

        print("Bases: {}".format(base_p))

        print("Heights: {}".format(h_p))

        print("Perimeters: {}".format(peri_p))

        print("Areas: {}".format(area_p))

    elif parallelogram == 1:
        print("Parallelogram: ")

        print("Hypotenuse: {}".format(hyp_p))

        print("Base: {}".format(base_p))

        print("Height: {}".format(h_p))

        print("Perimeter: {}".format(peri_p))

        print("Area: {}".format(area_p))

    print()

    # summary for trapezium
    if trapezium > 1:
        print("Trapeziums: ")

        print("Left Hypotenuses: {}".format(hyp_tra_l))

        print("Right Hypotenuses: {}".format(hyp_tra_r))

        print("Upper Bases: {}".format(base_tra_u))

        print("Down Bases: {}".format(base_tra_d))

        print("Heights: {}".format(h_tra))

        print("Perimeters: {}".format(peri_tra))

        print("Areas: {}".format(area_tra))
    elif trapezium == 1:
        print("Trapezium: ")

        print("Left Hypotenuse: {}".format(hyp_tra_l))

        print("Right Hypotenuse: {}".format(hyp_tra_r))

        print("Upper Base: {}".format(base_tra_u))

        print("Down Base: {}".format(base_tra_d))

        print("Height: {}".format(h_tra))

        print("Perimeter: {}".format(peri_tra))

        print("Area: {}".format(area_tra))

