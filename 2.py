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
output_list = []
input = first_input

for _, item in enumerate(input):
    output = 1
    for i in range(len(input)):
        if i != _:
            output *= input[i]
    output_list.append(output)
print(output_list)

## NOTE: Working but should try and do it without using two loops.


# Second Attempt:
# This is how you could do it with division...
# You can use numpy as you are given an array
import numpy as np

output_list = []
input = first_input

for item in input:
    output_list.append(np.prod(np.array(input)) // item)
print(output_list)
