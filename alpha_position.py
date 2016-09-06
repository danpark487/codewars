# Welcome. In this kata you are required to, given a string, replace every letter with its position in the alphabet.
# If anything in the text isn't a letter, ignore it and don't return it.
# a being 1, b being 2, etc. As an example:
# alphabet_position("The sunset sets at twelve o' clock.")
# Should return "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11" (As a string.)

def alphabet_position(text):
    """
    This is where you should put what the function does, what variables it takes in, and what it outputs
    This is called a docstring
    """
    lower_text = text.lower() # make all characters into lowercase
    only_alpha = " ".join(lower_text)
    only_alpha = only_alpha.split() # convert into list
    # You could combine the 3 above.  to split_text = " ".join(text.lower()).split() This is generally accepted in python

 
    only_alpha = [char for char in only_alpha if char.isalpha()] # new list with only alphabet characters
    
    final_list = [] # empty list to be filled with for statement below
    for letter in only_alpha: 
        final_list.append(str(ord(letter)-96)) # appends the alphabet position to new list
    # You could also do this using a dictionary.  How would you do that?
    final_list = " ".join(final_list) # joins new list
 
    return final_list
