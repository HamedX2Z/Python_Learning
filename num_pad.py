# In Python, a 2D collection, often referred to as a two-dimensional array or matrix, is essentially an array of arrays.
# This means each element in the main array is another array. These are useful when you need to represent data in a
# grid or matrix format.
#
# For example, num_pad is a 2D collection where each sub-array represents a row of a num pad.
# You can iterate over each row and then each element within each row.
#
# Example:
# num_pad = ((1, 2, 3,),
#            (4, 5, 6,),
#            (7, 8, 9),
#            ("*", 0, "#"))
#
# Here, num_pad[0] will give you the first row (1, 2, 3)
# and num_pad[0][1] will give you the second element of the first row, which is 2.
#
# The nested for-loop construction allows you to access and print each element in the 2D collection in a structured manner.

num_pad = ((1, 2, 3,),
           (4, 5, 6,),
           (7, 8, 9),
           ("*", 0, "#"))

for row in num_pad:
    for num in row:
        print(num, end=" ")
    print()