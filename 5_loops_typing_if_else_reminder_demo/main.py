
is_in_use = True

while is_in_use:

    num_1 = int(input("Please enter the first number: "))
    operand = input("Please enter the operator: ")
    num_2 = int(input("Please enter the second number: "))

    if operand == "+":
        print(num_1 + num_2)
    if operand == "-":
        print(num_1 - num_2)
    if operand == "*":
        print(num_1 * num_2)
    if operand == "/":
        print(num_1 / num_2)

    if input("another? y/n: ") == "n":
        is_in_use = False



#----------------------------------------------------------------------------------------------------#
"""
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for number in numbers:
    if number % 2 == 0:
        print(number)
    else:
        number = "odd"

print(numbers)

print()

for i in range(0, 10, 1):
    if numbers[i] % 2 == 0:
        print(numbers[i])
    else:
        numbers[i] = "odd"

print(numbers)
"""

#----------------------------------------------------------------------------------------------------#
"""
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for number in numbers:
    if number % 2 == 0:
        continue
    print(number)
"""
#----------------------------------------------------------------------------------------------------#
'''
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for number in numbers:
    if number == 11:
        print(number)
        break
else:
    print("number not in list")
'''

#----------------------------------------------------------------------------------------------------#
"""
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for number in numbers:
    print(number)

print()

for i in range(0, 10, 1):
    print(numbers[i])
"""

"""
C# Example

for(int i = 0; i < 10; i++)

{
    Console.Writeline("Hello, World");
}


int[] numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9};

foreach(var number in numbers):
{
    Console.Writeline(number);
}"""


#----------------------------------------------------------------------------------------------------#
"""
for i in range(3):
    print("magister")

print()

ctr = 0
while ctr < 3:
    print("Magister")
    ctr += 1
"""

#----------------------------------------------------------------------------------------------------#

"""num_1 = int(input("Please enter the first number: "))
operand = input("Please enter the operator: ")
num_2 = int(input("Please enter the second number: "))

if operand == "+":
    print(num_1 + num_2)
if operand == "-":
    print(num_1 - num_2)
if operand == "*":
    print(num_1 * num_2)
if operand == "/":
    print(num_1 / num_2)
"""
#----------------------------------------------------------------------------------------------------#

'''
def print_hi(name):
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

if __name__ == '__main__':
    print_hi('PyCharm')
'''

