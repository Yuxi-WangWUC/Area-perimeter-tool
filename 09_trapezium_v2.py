"""
tool for calculate the area and perimeter for different shape
trapezium component
v1 first version of the trapezium function
get dimensions of trapezium, loop for several times
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
    hypotenuse_1 = round(int_check("First hypotenuse: "), 2)
    hypotenuse_2 = round(int_check("Second hypotenuse: "), 2)
    base_tra_1 = round(int_check("First base: "), 2)
    base_tra_2 = round(int_check("Second base: "), 2)
    height_tra = round(int_check("Height: "), 2)

    ans_tra_peri = round(int_check("Answer for perimeter in 2 decimal places: "), 2)
    total_tra_peri = round((base_tra_1 + base_tra_2 + hypotenuse_1 + hypotenuse_2), 2)
    if ans_tra_peri != total_tra_peri:
        print("Sorry, this is incorrect. The real answer is {:.2f}.".format(total_tra_peri))
    else:
        print("This is the correct answer. Well done")

    ans_tra_peri = round(int_check("Answer for area in 2 decimal places: "), 2)
    total_tra_peri = round((base_tra_1 + base_tra_2) * height_tra / 2, 2)
    if total_tra_peri != ans_tra_peri:
        print("Sorry, this is incorrect. The real answer is {:.2f}.".format(total_tra_peri))
    else:
        print("This is the correct answer. Well done")
    print()
