#2

#write a function that takes in a list of names and returns a dictionary
# with the elements as keys in the dictionary and the values as unique integers

"""
-- for loop that iterates through the list and populates the keys in the dictionary
        looping var would be value in dict

"""


def student_directory(student_names):
    dict = {}
    counter = 1

    for i in student_names:
        dict[i] = counter
        counter += 1
    
    return dict

student_names = ["Ada Lovelace", "Tu Youyou", "Mae Jemison", "Rajeshwari Chatterjee", "Alan Turing"]

print(student_directory(student_names))