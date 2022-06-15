"""
tool to calculate the area and perimeter of different shapes
no blank component
v1 - set up loop for no blank, if the users didn't enter anything, the code will repeat to ask a valid answer
Yuxi Wang
"""

# functions go here


def not_blank(question, error_message):
    valid = False

    while not valid:
        response = input(question)
        # if the response is not blank, program continues
        if response != "":
            return response
        # if the response is blank, show error and repeat loop
        else:
            print(error_message)


# Main Routine goes here
shape = not_blank("Please enter a shape you want to calculate: ",
                  "Sorry, this can't be blank, "
                  "please enter a valid shape")
