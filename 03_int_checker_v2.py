"""
tool to calculate the area and perimeter of different shapes
int_checker component
v1 set up the code
v2
"""

# function goes here


def int_check(question):
    error = "Please enter a number between 0 and 10000"

    valid = False
    while not valid:

        # ask user for a positive  and check it is valid
        try:
            response = float(input(question))

            if response <= 0 or response >= 10000:
                print(error)
            else:
                return response
        # if a number is not entered, display an error
        except ValueError:
            print(error)


# main routine goes here
min_len = 0
max_len = 10000

len_1 = int_check("First length: ")


