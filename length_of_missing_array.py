# Description:

# You get an array of arrays.
# If you sort the arrays by their length, you will see, that their length-values are consecutive.
# But one array is missing!


# You have to write a method, that return the length of the missing array.

# Example:
# [[1, 2], [4, 5, 1, 1], [1], [5, 6, 7, 8, 9]] --> 3


# If the array of arrays is null/nil or empty, the method should return 0.

# When an array in the array is null or empty, the method should return 0 too!
# There will always be a missing element and its length will be always between the given arrays.


def get_length_of_missing_array(array_of_arrays):
    if not array_of_arrays or [] in array_of_arrays or None in array_of_arrays:
        return 0
    arrays = [len(arr) for arr in array_of_arrays]
    for i in range(min(arrays),max(arrays)):
        if i not in arrays:
            return i