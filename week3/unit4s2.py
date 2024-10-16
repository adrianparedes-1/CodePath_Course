#1
def is_long_pressed(name, typed):
    ptr1 = 0
    ptr2 = 0

    while ptr2 < len(typed):
        # If characters match, move both pointers
        if ptr1 < len(name) and name[ptr1] == typed[ptr2]:
            ptr1 += 1
        # If typed character matches the previous typed character, just move ptr2
        elif ptr2 > 0 and typed[ptr2] == typed[ptr2 - 1]:
            pass  # Allow long press
        else:
            return False  # Mismatch
        ptr2 += 1  # Always move ptr2 forward

    # Check if all characters in name were matched
    return ptr1 == len(name)

# Test cases
name1 = "alex"
typed1 = "aaleex"
print(is_long_pressed(name1, typed1))  # True

name2 = "saeed"
typed2 = "ssaaedd"
print(is_long_pressed(name2, typed2))  # False

name3 = "courtney"
typed3 = "courtney"
print(is_long_pressed(name3, typed3))  # True



#2

'''
understand: write a function that will output the amount of satisfied children given a list of greed factors and cookie sizes

the problem is asking us compare the two lists to come to a conclusion

what if there are no cookies? No child is satisfied.
what if there are more children than cookies? search for a children who has a content level that matches the cookie size so at least those children will be content


plan:

use 2 pointer method to set 2 pointers at the beginning of each list.
We will simply compare the current index in both lists. If the current index of g > current index of s --> children is not satisfied (create a variable that is increased when a child is satisfied)
Stop going through the list if ptr1 reaches the end of their list

if the size of s < size of g --> search for any index in g with the value in the current index of s (increase counting variable if a child is found with the same content level)
'''

def find_content_children(s, g):
    ptr1 = 0
    ptr2 = 0
    count = 0

    while ptr1 < len(g):
        # print(f"Pointer 1:{ptr1}")
        # print(f"Pointer 2:{ptr2}")
        # print(count)
        if g[ptr1] > s[ptr2]:
            pass
        else:
            count += 1
        ptr2 += 1
        ptr1 += 1
    return count

# g = [1,2,3]
# s = [1,1,3]

# Answer: 2

g = [1,1]
s = [2,2,2]

# Answer: 2

print("Output:", find_content_children(s, g))



#3
"""
understand: the problem is asking us to create a function that takes a string as an argument and determines if the string can be a palindrome if a character is deleted.

a palindrome is a string that is mirrored.


plan: 1. check if there are any unique characters. 
    How do we check for a unique character? we could initialize a dictionary to keep track of frequency by using a key-value pair. Then we can compare key in the dictionary that has a value of 1 and remove it from the string.
    This will create a substring which we could use to check if it is a palindrome.
2. Create a sub-string without the unique character and check if it is a palindrome.
3. How to check if a string is a palindrome? We can do this by using the 2 pointer method. We can set a pointers to first and last elements in the sub-string, and we can traverse the string through both pointers.
    If any character found by the left or right pointer is not the same, then the substring is not a palindrome.
    If the pointers meet in the middle and all the characters match, then the substring is a palindrome.

"""
def valid_palindrome(s):
    dict = {}
    substring = " "
    

# populate the dictionary with values and frequencies in the string
    for i in s:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    print(s)
    print(dict)

    for idx, value in enumerate(s):
        if dict[value] == 1:
            substring = s[:idx] + s[idx + 1:]
    print(substring)

    ptr1 = 0
    ptr2 = (len(substring) - 1)
    # print(f"Pointer 1: {ptr1}")
    # print(f"Pointer 2: {ptr2}")

    # now we can check if the substring is a palindrome
    while ptr1 < ptr2:
        print(f"Pointer 1: {ptr1}")
        print(f"Pointer 2: {ptr2}")
        if substring[ptr1] != substring[ptr2]:
            return False
        ptr1 += 1
        ptr2 -= 1

    return True


s = "aba"
s2 = "abca"
s3 = "abc"

print(valid_palindrome(s))
print(valid_palindrome(s2))
print(valid_palindrome(s3))


#4

'''
understand: write a function that takes a list of numbers and checks for the largest positive number in the list. Once it finds this number, search for the negative version in the list. 
If it exists, return the positive integer. If it does not exist, return -1.

plan:

1. iterate through the list and hold the current largest positive number.
2. Once we find that number, find the negative version.
3. Output depending on whether the negative version was found or not.
'''

def find_largest_k(nums):
    largest = nums[0]
    for i in nums:
        if largest < i:
            largest = i

    for j in nums:
        if -largest == j:
            return largest
    return -1

nums = [-1,2,-3,3,-1]
print(find_largest_k(nums))

nums2 = [-10,2,7,-3]
print(find_largest_k(nums2))


#5
'''
 understand: this problem is asking us to use the sliding window technique to find a good substring of length 3. 
 A good substring is a substring that does not contain any repeated characters.
 If a substring is found, we should count the occurrence.

 plan:

 1. iterate through the list.
 2. create a substring
 3. turn the substring into a set and check if the length of the substring is 3 (a set removes all duplicates so if the substring has a duplicate, the length will be less than 3)
 4. increase counting variable

 '''

def count_good_substrings(s):
    count = 0

    for i in range(len(s)):
        window = s[i:i + 3]

        if (len(set(window))) == 3:
            count += 1
    
    return count

s1 = "xyzzaz"
s2 = "xyzxyz"
print(count_good_substrings(s1))
print(count_good_substrings(s2))