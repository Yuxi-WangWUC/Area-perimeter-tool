"""
tool for calculate the area and perimeter for different shapes
rectangle component
v1 first version of the rectangle function
get dimensions of rectangle, loop for three times
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
for i in range(0, 4):
    height_r = round(int_check("Height: "), 2)
    base_r = round(int_check("Base: "), 2)
    ans_r_peri = round(int_check("Answer for perimeter in 2 decimal places: "), 2)

    total_r_peri = round((height_r + base_r) * 2, 2)
    if ans_r_peri != total_r_peri:
        print("Sorry, this is incorrect. The real answer is {:.2f}.".format(total_r_peri))
    else:
        print("This is the correct answer. Well done")

    ans_r_area = round(int_check("Answer for area in 2 decimal places: "), 2)
    total_r_area = round(base_r * height_r, 2)
    if total_r_area != ans_r_area:
        print("Sorry, this is incorrect. The real answer is {:.2f}.".format(total_r_area))
    else:
        print("This is the correct answer. Well done")
    print()
