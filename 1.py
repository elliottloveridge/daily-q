# Daily Coding Problems: 1

# Given a list of numbers and a number k, return whether any two numbers
# from the list add up to k.
#
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

# Bonus: Can you do this in one pass?

test_data = [10, 15, 2, 4]
test_k = 17

#-----------------------------------------------------------------------------------------------------#

# So what you'd want is something that creates a list of all possible
# sums you can make from that list and then a check on that second
# list to see if the value exists.

# My Solution:
for _, item in enumerate(test_data):
    if _ != 0 and test_data[0] + item == test_k: print('true')

# Description:
# Looped through items in the list. Enumerate was used so that you wouldn't
# add the first item to itself (if _ != 0)
