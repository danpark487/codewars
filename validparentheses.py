# Description:

# Write a function called validParentheses that takes a string of parentheses, and determines if the order of the parentheses is valid. validParentheses should return true if the string is valid, and false if it's invalid.

# Examples:
# validParentheses( "()" ) => returns true
# validParentheses( ")(()))" ) => returns false
# validParentheses( "(" ) => returns false
# validParentheses( "(())((()())())" ) => returns true

# All input strings will be nonempty, and will only consist of open parentheses '(' and/or closed parentheses ')'

def valid_parentheses(string):
    """
    Take string consisting of parentheses and chars, returns True/False based on valid use of parentheses
    """
    validity = 0
    for i in string:
        if validity == 0:
            if i == "(":
                validity += 1
            elif i == ")":
                return False
        elif validity >= 1:
            if i == ")":
                validity -= 1
            elif i == "(":
                validity += 1
    if validity != 0:
        return False
    else:
        return True

# better solution

# def valid_parentheses(string):
#     validity = 0
#     for i in string:
#         if i == "(":
#             validity += 1
#         if i == ")":
#             validity -= 1
#         if validity < 0:
#             return False
#     if validity == 0: 
#         return True
#     else:
#         return False