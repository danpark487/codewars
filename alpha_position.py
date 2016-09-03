def alphabet_position(text):
    lower_text = text.lower() # make all characters into lowercase
    only_alpha = " ".join(lower_text)
    only_alpha = only_alpha.split() # convert into list
    
 
    only_alpha = [char for char in only_alpha if char.isalpha()] # new list with only alphabet characters
    
    final_list = [] # empty list to be filled with for statement below
    for letter in only_alpha: 
        final_list.append(str(ord(letter)-96)) # appends the alphabet position to new list
    
    final_list = " ".join(final_list) # joins new list
 
    return final_list