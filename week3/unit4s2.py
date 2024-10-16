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