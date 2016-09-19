# Your task is to sort a given string. Each word in the String will contain a single number. This number is the position the word should have in the result.

# Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).

# If the input String is empty, return an empty String. The words in the input String will only contain valid consecutive numbers.

# For an input: "is2 Thi1s T4est 3a" the function should return "Thi1s is2 3a T4est"

def order(sentence):
    """
    Takes in sentence with various integers inside words, returns new sentence with words in order of the integer within
    """
    dict_sent = {} 
    new_list = []
    integer = "123456789"
    sentence = sentence.split()
    for x in sentence:
        for char in x:
            if char in integer:
                dict_sent[int(char)] = x # adds the word with the key of the integer within the word
    for i in range(1,len(sentence)+1):
        new_list.append(dict_sent[i]) # adds words by the key order of the dictionary
    return " ".join(new_list)