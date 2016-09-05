# Description:
# Bob is preparing to pass IQ test. The most frequent task in this test is to find out which one of the given numbers differs from the others. Bob observed that one number usually differs from the others in evenness. Help Bob — to check his answers, he needs a program that among the given numbers finds one that is different in evenness, and return a position of this number.
# ! Keep in mind that your task is to help Bob solve a real IQ test, which means indexes of the elements start from 1 (not 0)

# Examples :
# iq_test("2 4 7 8 10") => 3 // Third number is odd, while the rest of the numbers are even
# iq_test("1 2 1 1") => 2 // Second number is even, while the rest of the numbers are odd

def iq_test(numbers):
  """
  Take in string of numbers, converts into list of integers,
  Check integers if even/odd, compile two lists for even/odd
  Whichever has least number of elements in list is "different" number
  Return index (plus 1) of "different" number from  original list
  """
  odd_list = [] # empty list for odd numbers
  even_list = [] # empty list for even numbers
  numbers_list = numbers.split() # make a list of input
  intlist = [int(x) for x in numbers_list] # convert elements of list to integers
  for number in intlist: # check for even/odd
    if number%2 == 0: # add to even_list if even
      even_list.append(number) 
    else: # add to odd_list if odd
      odd_list.append(number)
  if len(even_list) > len(odd_list): # return index of element from short list in the original list
    return intlist.index(odd_list[0]) + 1 
  else:
    return intlist.index(even_list[0]) + 1