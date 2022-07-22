"""
tool for calculate the area and perimeter for different shapes
triangle component
v1 first version of the triangle function
get dimensions of triangle, loop for three times
calculate the perimeter and area, check against user's answer
if correct, then well down
if not, then print the correct answer
"""


# function goes here
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
                return response
        # if a number is not entered, display an error
        except ValueError:
            print(error)


# main routine
for i in range(0, 2):
    len_1 = int_check("First length: ")
    len_2 = int_check("Second length: ")
    len_3 = int_check("Third length: ")
    height_tri = int_check("Height: ")
    base_tri = int_check("Base: ")
    ans_tri_peri = int_check("Answer for perimeter in 2 decimal places: ")

    total_tri_peri = len_1 + len_2 + len_3
    if ans_tri_peri != total_tri_peri:
        print("Sorry, this is incorrect. The real answer is {}.".format(total_tri_peri))
    else:
        print("This is the correct answer. Well done")

    ans_tri_area = int_check("Answer for area in 2 decimal places: ")
    total_tri_area = base_tri * height_tri / 2

    if total_tri_area != ans_tri_area:
        print("Sorry, this is incorrect. The real answer is {}.".format(total_tri_area))
    else:
        print("This is the correct answer. Well done")
    print()
