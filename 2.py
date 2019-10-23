# Daily Coding Problems: 2

# Given an array of integers, return a new array such that each element at
# index i of the new array is the product of all the numbers in the original
# array except the one at i.
#
# For example, if our input was [1, 2, 3, 4, 5], the expected output
# would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1],
# the expected output would be [2, 3, 6].

# Follow-up: what if you can't use division?

first_input = [1, 2, 3, 4, 5]
second_input = [3, 2, 1]

#---------------------------------------------------------------------------#

# My Solution:
output = 1  ## FIXME: want to find a way to do it wihtout hardcoding this
output_list = []

for _, item in enumerate(first_input):
    
