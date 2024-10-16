#1 

#   write a function takes two lists of integers and determines if elements in each list are in the same relative order in both lists
#   we will need to keep track of position of each element in each list then compare the positions
#   we have the compare the positions of the matching elements to see if they both follow the same pattern: increasing or decreasing
#       loop through the first list
#           per element, loop through the second list to see if it exists
#               if it does, append the position of the value in the second list to a new array
        #             if it doesnt --> don't do anything
        # once we loop through each element in the first list, we will have a list of the positions of the matching values in the second list
        # iterate through the positions list
        # if current value is > next value --> false
        # else: True
        
# Pros of this solution: simplicity and readability.
# Cons of this solution: time complexity -- pretty slow

# def is_subsequence(lst, sequence):
#     arr = []
#     for i in lst:
#         for idx, j in enumerate(sequence):
#             if (i == j):
#                 arr.append(idx)
#     for k in range(len(arr) - 1):
#         if (arr[k] > arr[k + 1]):
#             return False
#     return True

# lst = [5, 6, 25, 1, -1, 8, 10]
# sequence = [1, 6, -1, 10]
# print(is_subsequence(lst, sequence))


#2

# def create_dictionary(keys, values):
#     new_dict = {}
    

#     for i in range (len(keys)):
#         new_dict[keys[i]] = values [i]

#     print(new_dict)

# create_dictionary(["peanut", "dragon", "star", "pop", "space"], ["butter", "fly", "fish", "corn", "ship"])


#3

# write a function that will print the key-value pair in a dictionary. If the key does not exist, print a message stating so.
# This problem taught a good amount about iterating through dictionaries, accessing and printing keys and values associated with them

def print_pair(dictionary, target):
    found = False
    for key, i in dictionary.items():
        # print(i)
        # print(target)
        if (target == key):
            print(f"Key: {key} \nValue: {dictionary[key]}")
            found = True
            break
    if not found:
        print("That pair does not exist!")
        


dictionary = {"spongebob": "squarepants", "patrick": "star", "squidward": "tentacles"}
print_pair(dictionary, "patrick")
print_pair(dictionary, "plankton")
print_pair(dictionary, "spongebob")
