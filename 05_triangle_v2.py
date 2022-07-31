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
    base_tri = round(int_check("Base: "), 2)
    hypotenuse_tri_1 = round(int_check("First hypotenuse: "), 2)
    hypotenuse_tri_2 = round(int_check("Second hypotenuse: "), 2)
    height_tri = round(int_check("Height: "), 2)
    ans_tri_peri = round(int_check("Answer for perimeter: "), 2)

    total_tri_peri = round((hypotenuse_tri_1 + hypotenuse_tri_2 + base_tri), 2)
    if ans_tri_peri != total_tri_peri:
        print("Sorry, this is incorrect. The real answer is {:.2f}.".format(total_tri_peri))
    else:
        print("This is the correct answer. Well done")

    ans_tri_area = round(int_check("Answer for area: "), 2)
    total_tri_area = round((base_tri * height_tri / 2), 2)
    if total_tri_area != ans_tri_area:
        print("Sorry, this is incorrect. The real answer is {:.2f}.".format(total_tri_area))
    else:
        print("This is the correct answer. Well done")
    print()
