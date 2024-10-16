#3

"""
1. make string all lowercase
2. compare string versus alphabet

"""

# import string

# def is_pangram(my_str):
#     lc_str = my_str.lower()
#     new_str = string.ascii_lowercase

#     for i in new_str:
#         if i not in lc_str:
#             return False
        
#     return True


# my_str = "The quick brown fox jumps over the lazy dog"
# print(is_pangram(my_str))

# str2 = "The dog jumped"
# print(is_pangram(str2))



#4

"""


"""

# def reverse_string(my_str):
#     return my_str[::-1]


# my_str = "live"
# print(reverse_string(my_str))

"""
write a function that returns the first unique character in a list



"""

def first_unique_char(my_str):
    dict = {}

    for i in my_str:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1

    for index, value in enumerate(my_str):
        if dict[value] == 1:
            return index
    
    return -1

my_str = "leetcode"
print(first_unique_char(my_str))

str2 = "loveleetcode"
print(first_unique_char(str2))

str3 = "aabb"
print(first_unique_char(str3))
    
    # for key, value in dict.items():
    #     if value == 1:
    #         return key


