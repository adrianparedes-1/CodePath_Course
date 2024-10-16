#3

"""
Understand: write a function that takes a string as a parameter and check if the string contrains every
letter in the english alphabet.

Planning:

ASCII values -- use a for a loop to check if the ASCII values 

Check if each character in the string contains a letter from the alphabet. Should probably check versus a library

Edge case -- length of the alphabet (isLower to make all letters in the string lower case) so length would be 26:


1st:

make all letters lowercase
if length of the string is < 26 --> False because it can't possibly have all letters in the alphabet

2nd:

Two pointer system -- pointer starts at T and another point at ASCII value for 'a'. Once it finds at, the first
pointer on the string is reset, and the second pointer moves on to the next letter in the alphabet.

"""

# def is_pangram(my_str):

#     new_string = my_str.isLower()

#     if (len(new_string < 26)): #edge case
#         return False
    
#     for i in range(len(new_string)):
#         if new_string[i]