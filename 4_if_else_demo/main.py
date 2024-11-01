
user_input = input("Enter a phrase: foo/bar/foobar ")

if user_input == "foo":
    print("spam")

elif user_input == "bar":
    print("eggs")

elif user_input == "foobar":
    print("spamandeggs")

else:
    print("undefined behavior")


match user_input:
    case "foo":
        print("spam")
    case "bar":
        print("eggs")
    case "foobar":
        print("spamandeggs")
    case _:
        print("undefined behavior")


"""is_in_cooldown = True

is_threshold_passed = False

if is_in_cooldown:
    print("Cooldown")

flag = True

if flag:
    print("asd")
else:
    print("lol")
"""
"""usr_input = input("Please provide a boolean value t/f:")

answer = "Igen" if usr_input == "t" else "Nem"

print(answer)

#print("Igen" if usr_input == "t" else "Nem")"""

"""shot_cooldown = True
cooldown_time_threshold = 1000
time_elapsed = 0


if shot_cooldown == True and time_elapsed > cooldown_time_threshold:
    shot_cooldown = False
        
if shot_cooldown == True:
    if time_elapsed > cooldown_time_threshold:
        shot_cooldown = False"""


"""if flag == True: #EZT NEM!!!!!!!!!!!
    flag = False
    print("True")

print("First Statement")

if flag == False:
    flag = True
    print("False")

print("Second Statement")"""

"""if flag == True:
    print("true")
    flag = False

elif flag == False:
    print("false")
    flag = True

else:
    print("excuse me wut?")

print(flag)"""

"""
def main()


if __name__ == '__main__':
    main()
"""
