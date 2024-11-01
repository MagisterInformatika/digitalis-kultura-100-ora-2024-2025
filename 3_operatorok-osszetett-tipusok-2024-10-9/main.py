# integer - int

int()

123 + 456
123 - 456
123 * 456
123 / 456
456 // 123
456 % 123 # modulo
10**3

123 < 456
123 > 456
123 <= 456
123 >= 456
123 == 456
123 != 456

# floating point - float

float()

1.23 + 4.56
1.23 - 4.56
1.23 * 4.56
1.23 / 4.56
4.56 // 1.23
4.56 % 1.23 # modulo
2**0.5

1.23 < 4.56
1.23 > 4.56
1.23 <= 4.56
1.23 >= 4.56
1.23 == 4.56
1.23 != 4.56

# character string - str

str()

"asd" + "lol"
"asd" * 3
f"asd {2 * 3} lol {3 / 2} xd"
"aabbbcccdd".count("b")
"asd xd asd lol asd".count("asd")
"asd lol xd".find("lol")
"asd lol xd".find("lmao")
"asd lol xd".index("lol")
"asd lol xd".index("lmao")

# true/false - bool

bool()

True and False

# A     B     A and B
# True  True  True
# True  False False
# False True  False
# False False False

True or False

# A     B     A or B
# True  True  True
# True  False True
# False True  True
# False False False

# True xor False

# A     B     A xor B
# True  True  False
# True  False True
# False True  True
# False False False

not True

# A     not A
# True  False
# False True

True == False
True != False

# list

list()

[]
[1, 2, 3]
["asd", "lol", "xd"]
[1, "asd", True, [1, 2, 3]]

[1, 2, 3] + [4, 5, 6]
[1, 2, 3] * 3

["asd", "lol", "xd"][0]
["asd", "lol", "xd"][1]
["asd", "lol", "xd"][2]

A = ["asd", "lol", "xd"]
A.append("lmao")
A

A.count("lol")
A.index("lol")
A.pop()
A.pop(1)
A.insert(1, "lol")
A.remove("lol")
A.extend([1, 2, 3])
A.reverse()

# A[0], A[1] = A[1], A[0]

# set

set()

{1, 2, 3}
{1, 2, 2, 1, 4, 3, 4}
{1, 1, "asd", 2.5, "xd", "xd"}

{1, 2, 3} | {3, 4, 5}
{1, 2, 3} & {3, 4, 5}
{1, 2, 3} - {3, 4, 5}

B = {1, 2, 3}
B.update({3, 4, 5})
B.intersection_update({2, 3, -1})
B.difference_update({2, 5})

B.add(9)
B.discard(3)
B.pop()
