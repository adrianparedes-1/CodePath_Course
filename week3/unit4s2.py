#1
'''
understand: write a function that takes two strings as parameters and checks if the the string has been long pressed
Long pressed means that every character in the first string is in the second string in the same position

plan: check if name is in typed -- this will immediately tell us if it is long pressed
If it is not in typed then return false
we can do this by making a dictionary but we will use the two pointer method
have a pointer that starts at the beginning of name and another that starts at typed

have a counter variable that keeps track of frequency in name and typed. make sure count1 <= count2
a
count1 = 1
a
count2 = 1

l
count1 = 1
a
count2 = 2

e
count1 = 1
l
count2 = 1
'''
def is_long_pressed(name, typed):
    pass