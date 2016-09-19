# Description:

# The new "Avengers" movie has just been released! There are a lot of people at the cinema box office standing in a huge line. Each of them has a single 100, 50 or 25 dollars bill. A "Avengers" ticket costs 25 dollars.

# Vasya is currently working as a clerk. He wants to sell a ticket to every single person in this line.

# Can Vasya sell a ticket to each person and give the change if he initially has no money and sells the tickets strictly in the order people follow in the line?

# Return YES, if Vasya can sell a ticket to each person and give the change. Otherwise return NO.
# Examples:

# ### Python ###

# tickets([25, 25, 50]) # => YES 
# tickets([25, 100]) 
#          # => NO. Vasya will not have enough money to give change to 100 dollars

def tickets(people):
    print people
    count_1 = 0 # 25 bills
    count_2 = 0 # 50 bills
    count_3 = 0 # 100 bills
    for x in people:
        if x == 25:
            count_1 += 1
        elif x == 50:
            count_2 += 1
            count_1 -= 1
            if count_1 < 0 or count_2 < 0:
                return "NO"
        elif x == 100:
            if count_2 > 0 and count_1 > 0:
                count_3 += 1
                count_2 -= 1
                count_1 -= 1
            elif count_1 > 2:
                count_1 -= 3
            else:
                return "NO"
    return "YES"