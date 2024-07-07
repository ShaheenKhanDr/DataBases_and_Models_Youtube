# HomeWork_Lesson_1
# My_Intro
name = 'I am Dr_Shaheen_Khan'
age = 'Fifty Five years old'
profession = 'My_Profession_is_Teaching'
message = (name, age, profession)
print(message)

# Homework_Lesson_1_ANSWERS
# ANSWER _ 1
# Error: The 'chairs' variable is a string, and multiplying it by 'nails' may lead to unexpected results.
chairs = '15'
nails = 4
total_nails = int(chairs) * nails
message = 'I need to buy {} nails'.format(total_nails)
print('You need to buy {} nails'.format(message))

# ANSWER _ 2
my_name = 'Penelope'
my_age = 29
message = 'My name is {} and I am {} years old'.format(my_name, my_age)
print(message)

# ANSWER _ 3
# Define the parameters
eggs_per_box = 6
eggs_per_omelet = 4
total_boxes_of_eggs = 6  # You can adjust this value as needed

# Calculate the number of omelets
total_eggs = eggs_per_box * total_boxes_of_eggs
num_omelets = total_eggs // eggs_per_omelet
# Generate and display the output message
output_message = "You can make {} omelets with {} boxes of eggs.".format(num_omelets, total_boxes_of_eggs)
print(output_message)

# ANSWER _ 4
# Task 1: Replace the (.) with (!)
my_str = "I love coding."
my_str = my_str.replace('.', '!')
# Type your code here.
print(my_str)

# Task 2 - Reassign str so that all its characters are lowercase.
my_str_1 = "EVERY Exercise Brings Me Closer to Completing my GOALS."
my_str_1 = my_str_1.lower()
# Type your code here.
print(my_str_1)

# Task 3 - Does the string start with an A?
my_str_2 = "We enjoy traveling."
ans_1 = my_str_2.startswith('A')
# Type your code here.
print(ans_1)

# Task 4 - Find the length of the given string.
my_str_3 = "1.458.001"
ans_2 = len(my_str_3)
# Type your code here.
print(ans_2)

# ANSWER _ 5
# Task 1 - Slice the word so that you get "thon".
wrd = "Python"
ans_1 = wrd[2:]
# Type your answer here.
print(ans_1)

# Task 2 - Slice the word until "o".
wrd = "Python"
ans_1 = wrd[:wrd.index('o')]
# Type your answer here.
print(ans_1)

# Task 3 - Get "th" only.
wrd = "Python"
ans_1 = wrd[2:4]
# Type your answer here.
print(ans_1)

# Task 4 - Slice the word with steps of 2, excluding first and last characters.
wrd = "Python"
ans_1 = wrd[1:-1:2]
# Type your answer here
print(ans_1)
