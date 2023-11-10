

# Dictionary: (List <-> Array)

"""
Array:  length is fixed.
List:   length is NOT fixed.
Tuple:  length is fixed + u can't change it
"""
# age_list = [19, 17, 20, 15, 21]


# # Solution 1: (for showing names for each item)
# name_list = ["Amy", "Anson", "Angus", "Anna", "Abrakadabra"]
# age_list = [19, 17, 20, 15, 21]

# for i in range(len(name_list)):
#     print(name_list[i], age_list[i])



# # Solution 2:
# age_list = [("Amy", 19), ("Anson", 17), ("Angus", 20), ("Anna", 15), ("Abrakadabra", 21)]
# age_list = [["Amy", 19], ["Anson", 17], ["Angus", 20], ["Anna", 15], ["Abrakadabra", 21]]


# Solution with Dictionary:
age_dict = {
    "Amy": 19,
    "Anson": 17,
    "Angus": 20,
    "Anna": 15,
    "Abrakadabra": 21
}

# # Printing dictionary items
# print(age_dict["Anson"])

# # Iterating

# for x in age_dict:
#     print(x, age_dict[x])


# 
print(age_dict.keys())