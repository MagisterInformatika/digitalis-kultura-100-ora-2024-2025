
with open('test.txt', 'r') as file:
    data = [line.strip("\n").split(" ") for line in file]

#list_container = [do something for each line in the file]

print(data)

for line in data:
    for item in line:
        print(item, end="")
    print()

#---------------------------------------------------------------------

"""
data = []

with open('test.txt', 'r') as file:
    for line in file:
        row = line.strip("\n").split(" ")
        data.append(row)

print(data)

for line in data:
    for item in line:
        print(item, end="")
    print()
"""

#---------------------------------------------------------------------

"""
file = open('test.txt', 'r')

data = []

for line in file:
    row = line.strip("\n").split(" ")
    data.append(row)

file.close()

print(data)

for line in data:
    for item in line:
        print(item, end="")
    print()
"""

#---------------------------------------------------------------------

'''
def manage_user_input():
    num_1 = int(input("Please enter the first number: "))
    operand = input("Please enter the operator: ")
    num_2 = int(input("Please enter the second number: "))
    return num_1, operand, num_2


def calculate_result(num_1, operand, num_2):
    if operand == "+":
        return num_1 + num_2
    if operand == "-":
        return num_1 - num_2
    if operand == "*":
        return num_1 * num_2
    if operand == "/":
        return divide(num_1, num_2)


def divide(num_1, num_2):
    return num_1 / num_2


def main():

    is_in_use = True

    while is_in_use:

        num_1, operand, num_2 = manage_user_input()

        result = calculate_result(num_1, operand, num_2)

        print(result)

        if input("another? y/n: ") == "n":
            is_in_use = False

if __name__ == '__main__':
    main()
'''
#---------------------------------------------------------------------
"""
import math
from math import *



def main(): #Table of contents - Félig, de inkább NEM!!!
  print(f'Hello, World!')

a = 3
b = 5
print(a + b)

if __name__ == '__main__':
  main()
"""

#Funkcionális Dekompozíció

#CRUD

# Create
# Read
# Update
# Delete