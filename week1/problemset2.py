def abovethreshold(lst, threshold):
    arr = []
    for i in range (len(lst) - 1):
        if (lst[i] > threshold):
            arr.append(lst[i])
    return arr

# print(abovethreshold([8,2,13,11,4,10,14], 10))

#1

# function that prints each element in a list
#   for loop that iterates through each element in the list
#   first check if the list is empty, then go through list
#   call function

def print_list(lst):
        for i in range (len(lst)):
            print(lst[i])

print_list(["squirtle", "gengar", "charizard", "pikachu"])
print_list([])


#4

def flip_sign(lst):
    arr = []
    for i in (lst):
        arr.append(i * -1)

    return arr

print(flip_sign([1,-2,-3,4]))

#7

# to determine if a # is even, we would divide it by 2.
#   if the remainder is 0 then it is even

def get_evens(lst):
    arr = []
    for i in (lst):
        if (i % 2 == 0):
            arr.append(i)
    return arr
print(get_evens([1,2,3,4]))


#8

def multiples_of_five():
    for i in range (1,101):
        if (i % 5 == 0):
            print(i)

multiples_of_five()

#9

def find_divisors(n):
    for i in range (1, n + 1):
        if (n % i == 0):
            print(i)

find_divisors(6)

#10

def fizzbuzz(n):
    for i in range (1, n + 1):
        if (i % 3 == 0):
            print("Fizz")
        elif (i % 5 == 0):
            print("Buzz")
        else:
            print(i)

fizzbuzz(13)

#11

def print_indices(lst):
    for i in range (len(lst)):
        print(i)

print_indices([5,1,3,8,2])


#12


# function will search for target in a list
#   If found, return the position
#   If not found, return -1

def linear_search(lst, target):
    for i in range (len(lst)):
        if (target == lst[i]):
            return i
        elif (i == len(lst) and target != lst(i)):
            return -1
        
lst = [1,4,5,2,8]
position = linear_search(lst,5)
print(position)