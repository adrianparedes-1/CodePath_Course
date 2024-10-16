
def todays_mood():
    mood = "\U00002764"
    print("Today's mood: " + mood)

todays_mood()

def product(a, b):
    return a * b 

print(product(22,7))

#7

def time (num):
    if num == 1:
        return "4"
    elif isinstance(num,str):
        return '1'
    else:
        return '3'
    
print(time("Hello"))
print(time(1))

#8

def blackjack(score):
    if score == 21:
        return "Blackjack!"
    elif score > 21:
        return "Bust!"
    elif score >= 17 and score < 21:
        return "Nice hand!"
    elif score < 17:
        return "Hit me!"
    else:
        return "Not Valid. Try again."
    
print(blackjack(24), blackjack(19), blackjack(21), blackjack(10))

#9

def get_first(lst):
    if len(lst) < 1:
        return None
    else:
        return lst[0]
    
print(get_first([3,1,6,7,5]))

#10

def get_last(lst):
    if len(lst) < 1:
        return None
    else:
        return lst[len(lst) - 1]
    
print(get_last([3,1,6,7,5]))

#11

def counter(stop):
    for i in range (1, stop + 1):
        print(i)

counter(7)


#12

def sum_ten():
    sum = 0
    for i in range(1, 11):
        sum += i
    return sum

print(sum_ten())

#13

def sum_positive_range(stop):
    sum = 0
    for i in range (1, stop + 1):
        sum += i
    return sum
print(sum_positive_range(6))

#14

def sum_range(start, stop):
    sum = 0
    for i in range (start, stop + 1):
        sum += i
    return sum
print(sum_range(3,9))

#15

def print_negatives(lst):
    for i in range (len(lst)):
        if lst[i] < 0:
            print(lst[i])

print_negatives([3,-2,2,1,-5])