"""
tool for calculate the area and perimeter for different shape
create a summary summary table
v2
"""


def summary_generator(summary, decoration):
    sides = decoration * 3
    summary = "{} {} {}".format(sides, summary, sides)
    top_bottom = decoration * len(summary)

    print(top_bottom)
    print(summary)
    print(top_bottom)

    return ""


# main routine
test_data = [
    [[3, 'First hypotenuse'], [5, 'Second hypotenuse', ],  [3, 'Height'], [4, 'Down base'], [12, 'Perimeter'], [6, 'Area']],
    [[7, 'Height'], [5, 'Upper base'], [5, 'Down base'], [24, 'Perimeter'], [35, 'Area']],
    [[3, 'Radius'], [18.84, 'Perimeter'], [28.26, 'Area']],
    [[4, 'First hypotenuse'], [4, 'Second hypotenuse'], [3, 'Height'], [5, 'Upper base'], [5, 'Down base'], [18, 'Perimeter'], [15, 'Area']],
    [[7, 'First hypotenuse'], [9, 'Second hypotenuse'], [6, 'Height'], [5, 'Upper base'], [13, 'Down base'], [34, 'Perimeter'], [54, 'Area']]
]

welcome_greeting = test_data
welcome_decoration = "*"

summary_generator(welcome_greeting, welcome_decoration)
print()
unicorn_summary = "congratulations"
unicorn_decoration = "!"
summary_generator(unicorn_summary, unicorn_decoration)

