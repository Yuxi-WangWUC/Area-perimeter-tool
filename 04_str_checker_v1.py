"""
tool for calculate the area and perimeter for different shapes
string checker component
v1 component string checker - check to make sure the function is called
"""


# string checking functions, takes in
# question and list of valid responses
def string_checker(question, to_check):

    valid = False
    while not valid:

        response = input(question).lower()

        if response in to_check:
            return response

        else:
            for item in to_check:
                # checks if response is the first letter of
                # an item in the list
                if response == item[0]:
                    # note: returns the entire response
                    # rather than just the first letter
                    return item

        print("Sorry that is not a valid response")


# Main routine starts here
for item in range(0, 5):
    shapes = string_checker("What shape you want to enter ",
                            ["triangle", "rectangle",
                             "circle", "parallelogram",
                             "trapezium"])
    print(shapes)
    print()
