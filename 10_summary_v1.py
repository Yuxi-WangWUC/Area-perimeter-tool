"""
tool for calculate the area and perimeter for different shape
summary component
"""

import pandas

# initialise shapes lists
all_shapes = ["triangle", "rectangle", "circle", "parallelogram", "trapezium"]

first_hypotenuse = []
second_hypotenuse = []
height = []
radius = []
upper_base = []
down_base = []
perimeter = []
area = []

summary_list = [ first_hypotenuse, second_hypotenuse, height, radius, upper_base, down_base, perimeter, area]


shape_data_dict = {
    'Shape': all_shapes,
    'First hypotenuse': first_hypotenuse,
    'Second hypotenuse': second_hypotenuse,
    'Height': height,
    'Radius': radius,
    'Upper base': upper_base,
    'Down base': down_base,
    "Perimeter": perimeter,
    "Area": area
}

test_data = [
    [[3, 'First hypotenuse'], [5, 'Second hypotenuse', ],  [3, 'Height'], [4, 'Down base'], [12, 'Perimeter'], [6, 'Area']],
    [[7, 'Height'], [5, 'Upper base'], [5, 'Down base'], [24, 'Perimeter'], [35, 'Area']],
    [[3, 'Radius'], [18.84, 'Perimeter'], [28.26, 'Area']],
    [[4, 'First hypotenuse'], [4, 'Second hypotenuse'], [3, 'Height'], [5, 'Upper base'], [5, 'Down base'], [18, 'Perimeter'], [15, 'Area']],
    [[7, 'First hypotenuse'], [9, 'Second hypotenuse'], [6, 'Height'], [5, 'Upper base'], [13, 'Down base'], [34, 'Perimeter'], [54, 'Area']]
]

count = 0
for user_que in test_data:
    # assume no dimension have been entered
    for item in summary_list:
        item.append(0)

    # print shape lists
    # get summary
    shape_cal = test_data[count]
    count += 1

    for item in shape_cal:
        if len(item) > 0:
            to_find = (item[1])
            amount = (item[0])
            add_list = shape_data_dict[to_find]
            add_list[-1] = amount
# create dataframe and set index to shape column
shape_frame = pandas.DataFrame(shape_data_dict)
shape_frame = shape_frame.set_index('Shape')

# shorten column names
shape_frame = shape_frame.rename(columns={'First hypotenuse': 'Hyp 1',
                                          'Second hypotenuse': 'Hyp 2',
                                          'Upper base': 'Base U',
                                          'Down base': 'Base D'})

print(shape_frame)


