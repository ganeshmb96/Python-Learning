"""
    This file contains all that I have learnt for the itertools Python module.

    The link to the learning guide is here -> https://medium.com/star-gazers/python-itertools-5a6bd4124119
"""

#This is using the count operator which generates values in a range that are evenly spaced
import itertools
list_of_nums = []

for i in itertools.count(20,1):
    list_of_nums.append(i)
    if i>30:
        break

print(f"The result using the count operator is {list_of_nums}")

#This method below is using the cycle operator
# Create a list that shows several places
places = ["home", "school", "cafe", "gym","restaurants",  "park"]
places_cycle = itertools.cycle(places)
# If you didn't give a value, this would cycle forever
for i in range(9):
    # Then call next() whenever you want another one.
    place = next(places_cycle)
    # Print this value with format method
    print("Going {}".format(place))