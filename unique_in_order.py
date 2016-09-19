def unique_in_order(iterable):
    """
    Takes iterable, returns list of items without any elements with the same value next to each other in the same order of original list
    """
    unique_list = []
    counter = 0 # keeps track of index of last unique char added to list
    for i in range(len(iterable)):
        if not unique_list:
            unique_list.append(iterable[i])
        else:
            if iterable[i] != unique_list[counter]:
                unique_list.append(iterable[i])
                counter += 1
    return unique_list

# Better solutions:

# def unique_in_order(iterable):
#     result = []
#     prev = None
#     for char in iterable[0:]:
#         if char != prev:
#             result.append(char)
#             prev = char
#     return result

# The above solution's counter has a "counter" called "prev" that updates itself from None to the last unique char added
# The if statement checks whether the next object in list is equal to "prev"; if not equal, it adds the char and updates "prev" to that char

# def unique_in_order(iterable):
#     res = []
#     for item in iterable:
#         if len(res) == 0 or item != res[-1]:
#             res.append(item)
#     return res

# This solution simply checks the last element in the return list with the character being checked in original list
# It will only append items where the two are different