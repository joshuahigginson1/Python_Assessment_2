# Imports -----------------------------

import random
import math


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
    output = output.replace(",", "")
    output = output.replace(" ", "")
    output = output.replace("'", "")

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


def six(input):
    if input[-2].lower() == 'p' and input[-1].lower() == 'y':
        output = True
    else:
        output = False
    return output


# <QUESTION 7>


def seven(a, b, c):
    input_list = [a, b, c]
    input_list = sorted(input_list)

    smol_mid_dif = input_list[1] - input_list[0]
    mid_big_dif = input_list[2] - input_list[1]

    if smol_mid_dif == mid_big_dif:
        output = True

    else:
        output = False

    return output


# <QUESTION 8>


def eight(input, a):

    input_list = list(input)

    middle_of_string = (len(input) / 2)
    middle_of_string = math.ceil(middle_of_string)

    start_of_remove = int(a/2)

    starting_index = (middle_of_string - start_of_remove) - 1

    for repeats in range(a):
        input_list.pop(starting_index)


    output = str(input_list)
    output = output.strip("[]")
    output = output.replace(" ", '')
    output = output.replace(",", '')
    output = output.replace("'",'')

    return output


# <QUESTION 9>


def nine(string1, string2):
    string1_in_string2 = False
    string2_in_string1 = False

    for letter1 in string1:
        if letter1 in string2:
            string1_in_string2 = True
            continue
        else:
            string1_in_sting2 = False
            break

    for letter2 in string2:
        if letter2 in string1:
            string2_in_string1 = True
        else:
            string2_in_string1 = False
            break

    if string1_in_string2 == True or string2_in_string1 == True:
        output = True

    else:
        output = False

    return output


# <QUESTION 10>


def ten(X, Y):
    num_of_elements = X
    num_of_lists = Y
    x_list = []
    y_list = []

    for lists in range(num_of_lists):
        for elements in range(num_of_elements):
            list_value = lists * elements
            x_list.append(list_value)
        y_list.append(x_list)
        x_list = []

    return y_list
