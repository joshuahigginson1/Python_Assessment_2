# <QUESTION 1>

def one(input):
    num_list = []
    output_list = []
    input_list = input

    input_list = input.split(',')

    for number in input_list:

        number_int = int(number)

        if number_int % 2 != 0:
            num_list.append(int(number_int))
        else:
            continue

    output_string = str(num_list)
    output_string = output_string.strip('[]')
    output_string = output_string.replace(" ", "")

    if output_string == '':
        output_string = 'null'

    return output_string


# <QUESTION 2>

def two(input):
    full_list = input
    output_list = []

    for words in full_list:
        if words not in output_list:
            output_list.append(words)
        else:
            continue

    return output_list


# <QUESTION 3>


def three(input):
    full_list = input
    output_list = ''

    for letters in full_list[1::2]:
        output_list += letters

    return output_list


# <QUESTION 4>


def four(arg1):
    input = str(f" {arg1.lower()} ")
    check = " am "
    return input.count(check)


# <QUESTION 5>

# Write a function which checks the validity of a credit card number.
# The function will take a string and should return a boolean, True if the card is valid, or False if it is not.

# A credit card has a valid number if it satisfies the following criteria.
# - it must start with a 4, 5 or 6.
# - it must contain exactly 16 digits.
# - each digit must be 0-9 inclusive.
# - it may contain hyphens ("-"), to separate groups of 4 digits only, but it cannot contain any other characters.
# - it must not have 4 or more consecutive repeated digits.

# <EXAMPLES>

# five(0123-4567-8901-2345) → False
# five(401234567890123) → False
# five(4012 3456 7890 1234) → False
# five(4444-0123-4567-8901) → False
# five(4012-3456-7890-1234) → True
# five(4012345678901234) → True

# <HINT>
# How did we check if an entry was NOT IN a list?
# Think about maybe nesting 'if statements' and/or 'for loops'.

def five(input):
valid_chars_str = ['0','1','2','3','4','5','6','7','8','9','-']
nums = [1,2,3,4,5,6,7,8,9]
valid_start_nums = [4,5,6]

output = False

credit_list = []

    for numbers in input:
		if numbers in valid_chars_str:
			credit_list.append(numbers)

			if int(credit_list[0]) in valid_start_nums:




			else:
				output = False


		else:
			output = False







    take string

    must start with 4, 5, or 6

    len(obj) == 16


if no hypens, thats great. if hypens, check in groups of four.

    must not have 4 or more consecutive digits.

    output bool


    return False"""


# <QUESTION 6>


def six(email, parameter):
    name_url_split_list = email.split("@")
    name = name_url_split_list[0].lower()
    comp_url = name_url_split_list[1]
    comp_url_split_list = comp_url.split(".")
    comp = comp_url_split_list[0].lower()

    if parameter == 'person':
        output = name
    if parameter == 'company':
        output = comp

    return output


# <QUESTION 7>

# Given a string, return the length of the largest "block" in the string.
# A block is a run of adjacent chars that are the same, do not ignore case.

# <EXAMPLES>

# seven("hoopplla") → 2
# seven("abbCCCddDDDeeEEE") → 3
# seven("") → 0

# <HINT>
# Try using nested for loops and keep track of the longest block.

"""def seven(input):
    
    count = 0
    
    for letters in input:
        if 
    
    
    return """
"""

# <QUESTION 8>


def eight(n):
    if n == 0:
        output_eight = 0
    elif n == 1:
        output_eight = 1
    elif n > 1:
        output_eight = eight(n - 1) + eight(n - 2)

    return output_eight


# <QUESTION 9>

# Write a function which solves the following puzzle.

# We count 35 heads and 94 legs among the chickens and rabbits in a farm. How many rabbits and how many chickens do we have?
# The values for 'heads' and 'legs' will be inputs and can be different from 35 and 94.
# The output should be of the form (chickens,rabbits).
# If there are no solutions to the puzzle, return "no solutions"

# <EXAMPLES>

# nine(35, 94) → (23,12)
# nine(2, 6) → (1,1)
# nine(12,63) → "no soltuions"

# <HINT>
# How many legs/heads does a chicken have? chicken has 2 legs and 1 head.
# How many legs/heads does a rabbit have? rabbit has 4 legs and 1 head.
# If we have the right number of legs, do we have the right number of heads?


'''
"def nine(heads, legs):
    return "no solutions"
'''


# <QUESTION 10>


def ten(input):
    list = input.split(",")
    output_list = sorted(list)
    output_str = str()

    for word in output_list:
        output_str = output_str + str(f"{word},")

    output_str = output_str.replace(" ", "")
    output_str = output_str.strip("[]")
    output_str = output_str[:-1]

    return output_str