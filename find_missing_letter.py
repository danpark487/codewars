# Description:
# Find the missing letter

# Write a method that takes an array of consecutive (increasing) letters as input and that returns the missing letter in the array.

# You will always get an valid array. And it will be always exactly one letter be missing. The length of the array will always be at least 2.
# The array will always contain letters in only one case.

# Example:

# ['a','b','c','d','f'] -> 'e'
# ['O','Q','R','S'] -> 'P'



def find_missing_letter(chars):
    abc = "abcdefghijklmnopqrstuvwxyz"
    ABC = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    print chars[0].isupper()
    if chars[0].isupper():
        for i in range(ABC.index(chars[0]), ABC.index(chars[0]) + len(chars)):
            if ABC[i] not in chars:
                return ABC[i]
    else:
        for i in range(abc.index(chars[0]), abc.index(chars[0]) + len(chars)):
            print abc[i]
            if abc[i] not in chars:
                return abc[i]