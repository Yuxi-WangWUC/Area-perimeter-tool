"""
tool to calculate the area and perimeter of different shapes
loop component
v1 set up the loop
"""
# Start of loop

# initialise loops so that it runs at least once
shape = ""
num_shape = 0
MAX_QUE = 5

while shape != "xxx" and num_shape < MAX_QUE:
    # tell user how many times they can ask for help
    if num_shape < MAX_QUE - 1:
        print("You can ask {} more "
              "questions".format(MAX_QUE - num_shape))
    # warn users that they can only ask one more question
    else:
        print("You can ask one more question")

    # Get details...
    shape = input("Shape: ")
    if shape != "xxx":
        num_shape += 1
    else:
        num_shape += 0
    print()

if num_shape == MAX_QUE:
    print("You had ask {} questions".format(num_shape))
elif num_shape == MAX_QUE - 1:
    print("You had ask {} questions.  \n"
          "You can ask one more question."
          .format(num_shape, MAX_QUE - num_shape))
else:
    print("You had ask {} question.  \n"
          "You can ask {} more questions."
          .format(num_shape, MAX_QUE - num_shape))
