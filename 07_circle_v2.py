"""
tool for calculate the area and perimeter for different shapes
circle component
v1 first version of the circle function
get dimensions of circle, loop for several times
calculate the circumference and area, check against user's answer
if correct, then well down
if not, then print the correct answer
"""

import math


# function goes here
def int_check(questions):
    error = "Please enter a number between 0 and 10000"

    valid = False
    while not valid:

        # ask user for a positive  and check it is valid
        try:
            response = float(input(questions.strip()))

            if response <= 0 or response >= 10000:
                print(error)
            else:
                return response
        # if a number is not entered, display an error
        except ValueError:
            print(error)


# main routine
for i in range(0, 4):
    radius_c = round(int_check("Radius (π = 3.14): "), 2)
    ans_c_cir = round(int_check("Answer for circumference: "), 2)
    pi = 3.14

    total_c_cir = round(radius_c * 2 * pi, 2)
    if ans_c_cir != total_c_cir:
        print("Sorry, this is incorrect. The real answer is {:.2f}.".format(total_c_cir))
    else:
        print("This is the correct answer. Well done")

    ans_c_area = round(int_check("Answer for area: "), 2)
    total_c_area = round(radius_c * radius_c * pi, 2)
    if total_c_area != ans_c_area:
        print("Sorry, this is incorrect. The real answer is {:.2f}.".format(total_c_area))
    else:
        print("This is the correct answer. Well done")
    print()
