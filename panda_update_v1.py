import pandas

import numpy

# lists to hold ticket details
all_menu = ["Croissant", "Bagel", "Muffin", "Donut", "Sourdough Loaf", "Cupcake"]
all_bakery_costs = [6, 4, 3, 5, 8, 3]

bakery_dict = {
    'Name': all_menu,
    'Item Price': all_bakery_costs,
}

# create dataframe / table from dictionary
bakery_frame = pandas.DataFrame(bakery_dict)

# Rearranging index
bakery_frame.index = numpy.arange(1, len(bakery_frame) + 1)

print(bakery_frame)
print()

