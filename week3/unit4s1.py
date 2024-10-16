#s1v2

"""
Understand:

perfect number -- all of its divisors when added are equal to that number

take a positive integer n and return True if the number is a "perfect" number

Plan:


brute force approach:
get the divisors and add them all up --  how do we find them?
    iterate through every number less than n
    use the modulus operator as a check where the current number n % (i) ==  0 --> proper divisor?

optimized approach:

    look at all of them numbers up to the square root of n
    Why the square root of n?
    sqrt(6) == 2 something --> look at less numbers

Once we have the proper divisor, how do we move forward?

add all divisors to a variable and check if it is equal to n. This will tell us if n is a perfect number or not.

"""

def is_perfect_number(n):
    num = 0

    for i in range(1, n):
        if n % i == 0:
            num += i

    # print(num)

    if num == n:
        return True
    else:
        return False
    
print(is_perfect_number(6))
print(is_perfect_number(28))
print(is_perfect_number(9))