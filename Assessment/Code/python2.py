# Imports -----------------------------

import random

# Questions --------------------------

# <QUESTION 1>


def one(input):
    output = ''

    for chars in input:
        for n in range(3):
            output += chars

    return output


# <QUESTION 2>


def two(input):
    output = ''

    if input > 1:

        for factors in range(2, input):
            if (input % factors) == 0:
                output = False
                break
        else:
            output = True

    else:
        output = False

    return output


# <QUESTION 3>


def three(input):
    list_of_numbers = []

    str_cat = str(input)  # Makes sure that the input to the function is a string.
    str_sum = str(f'{str_cat} {str_cat}{str_cat} {str_cat}{str_cat}{str_cat} {str_cat}{str_cat}{str_cat}{str_cat}')
    str_list = str_sum.split(" ")  # Split the long list of new strings by whitespace.

    for string in str_list:
        list_of_numbers.append(int(string))  # Convert each string object in str_list to an int + append to new list.

    output = sum(list_of_numbers)  # Sum all numbers in the list.

    return output


# <QUESTION 4>


def four(input1, input2):
    output_list = []

    if len(input1) == len(input2):
        for count, letters in enumerate(input1):
            index = count
            output_list.append(input1[index])
            output_list.append(input2[index])

    else:
        output = ''

    output = str(output_list)
    output = output.strip("[]")
    output = output.replace(",","")
    output = output.replace(" ", "")
    output = output.replace("'","")

    return output

# <QUESTION 5>


def five():

    output = []

    while len(output) < 5:
        potential_num = random.randint(100, 200)
        if potential_num % 2 == 0:
            output.append(potential_num)

    return output

# <QUESTION 6>

# Given a string, return the boolean True if it ends in "py", and False if not.

# Ignore Case.

# For Example:

# six("ilovepy") → True
# six("welovepy") → True
# six("welovepyforreal") → False
# six("pyiscool") → False

# <HINT>
# There are no hints for this question.

def six(input):
    return False


# <QUESTION 7>

# Given three ints, a b c, one of them is small, one is medium and one is large.

# Return the boolean True if the three values are evenly spaced, so the
# difference between small and medium is the same as the difference between
# medium and large.

# Do not assume the ints will come to you in a reasonable order.

# <EXAMPLES>

# seven(2, 4, 6) → True
# seven(4, 6, 2) → True
# seven(4, 6, 3) → False
# seven(4, 60, 9) → False

# <HINT>
# There is a function for lists called sort.
# Use the cli to access the documentation help(list.sort)

def seven(a, b, c):
    return False


# <QUESTION 8>

# Given a string and an integer, n, return a string that removes n letters from the 'middle' of the string.

# The string length will be at least n, and be odd when the length of the input is odd, so there will always be a 'middle'.

# <EXAMPLES>

# eight("Hello", 3) → "Ho"
# eight("Chocolate", 3) → "Choate"
# eight("Chocolate", 1) → "Choclate"

# <HINT>
# Use the cli to access the documentation help(str.replace)

def eight(input, a):
    return ""


# <QUESTION 9>

# Given two string inputs, if one can be made from the other return the boolean True, if not return the boolean False.

# <EXAMPLES>

# nine("god", "dog") → True
# nine("tree", "tiredest") → True
# nine("cat", "dog") → False
# nine("tripping", "gin") → True

# <HINT>
# There are no hints for this question.

def nine(string1, string2):
    return False


# <QUESTION 10>

# Write a function which takes 2 integers greater than 0, X,Y as input and generates a 2-dimensional array.

# The element value in the i-th row and j-th column of the array should be i*j.

# <EXAMPLES>

# ten(3,2) → [[0,0,0],[0,1,2]]
# ten(2,1) → [[0,0]]
# ten(3,4) → [[0,0,0],[0,1,2],[0,2,4],[0,3,6]]

# <HINT>
# Think about nesting for loops.

def ten(X, Y):
    return []
