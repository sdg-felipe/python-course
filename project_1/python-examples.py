# VARIABLES

name = "pepe"
price = 2
prices = [1,2,3]
isLogged = False

# -------------------------------

# COMMENTS

# SINGLE LINLE
"""
MULTIPLE
LINE
"""

# -------------------------------

# STRING FORMATTING

first_name = "John"
last_name = "Smith"

print(f"Hi {first_name} {last_name}")

sentence = "Hi {} {}"
print(sentence.format(first_name, last_name))

# -------------------------------

# USER INPUT

user_name = input("Enter your first name: ")
print(user_name)

days = int(input("Enter number of days: "))
print(f"{days} days are {round(days / 7, 2)} weeks")

# -------------------------------

# LISTS

people_list = ["John", "Smith", "Pepe", "Ana"]
print(people_list)
print(len(people_list))
print(people_list[0:2])
people_list.append("Albert")
print(people_list)
people_list.insert(1, "Bob")
print(people_list)
people_list.remove('John')
print(people_list)
people_list.sort()
print(people_list)

# -------------------------------

# SETS AND TUPLES

my_set = {1,2,3,4,5,5,5}
print(my_set)
print(len(my_set))
my_set.add(6)
print(my_set)
my_set.discard(6)
print(my_set)
my_set.update([7,8])
print(my_set)

# NOT MODIFICABLE
my_tuple = (1,2,3,4,5,5,5)
print(my_tuple)
print(len(my_tuple))
print(my_tuple[0])

# -------------------------------

# BOOLEANS AND OPERATORS

like_coffe = True
like_tea = False
print(like_coffe == like_tea)
print(like_tea != like_coffe)
print(1 > 3 and 5 < 7)
print(1 > 3 or 5 < 7)
print(not(1 == 1))

# -------------------------------

# IF ELSE ELIF

x = 1
if x == 1:
    print("x is 1")
elif x == 2:
    print("x is 2")
else:
    print("x is not 1")

# -------------------------------

# LOOPS

my_list = [1,2,3,4,5]
sum_for = 0
for element in my_list:
    sum_for += element
    print(element)
print(f"The sum_for is {sum_for}")

sum_while = 0
while sum_while < 5:
    sum_while += 1
    if sum_while == 3:
        break
    print(sum_while)
print(f"The sum_while is {sum_while}")

# -------------------------------

# DICTIONARIES

user_dictionary = {
    'username': 'pepe',
    'age': 22,
    'city': 'San Jose',
}
print(user_dictionary)
print(len(user_dictionary))
user_dictionary["married"] = True
print(user_dictionary)
print(user_dictionary['married'])
print(user_dictionary.get('username'))
user_dictionary.pop('married')
print(user_dictionary)

for x,y in user_dictionary.items():
    print(x,y)

user_dictionary2 = user_dictionary.copy()
user_dictionary2.pop('age')
print(user_dictionary2)

# -------------------------------

# FUNCTIONS

def sayHello(name):
    print(f"Hello {name}")

sayHello("Felipe")

def multiply(x,y):
    return x * y

solution = multiply(2,3)
print(solution)

# -------------------------------

# IMPORTS

import project_1.function as grade_service
grades = {
    'homework_1': 85,
    'homework_2': 90,
    'homework_3': 100,
}

print(grade_service.calculate_homework(grades))

import random
print(random.randint(1,10))

# -------------------------------

# OOP