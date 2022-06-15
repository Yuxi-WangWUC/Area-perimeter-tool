"""
tool to calculate the area and perimeter of different shapes
no blank component
v1 - set up loop for no blank, if the users didn't enter anything, the code will repeat to ask a valid answer
Yuxi Wang
"""

# functions go here


def not_blank(question):
    valid = False

    while not valid:
        response = input(question)

        if response != "":
            return response
        else:
            print("Sorry, this can't be blank")


# Main Routine goes here
shape = not_blank("Please enter a shape you want to calculate: ")
