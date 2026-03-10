from random import shuffle

#initial list
sticks = ['-', '--', '---', '----']

#mix sticks
def mix(list):
    shuffle(sticks)
    return list

# print(mix(sticks))

#ask to attemp
def try_luck():
    attemp = ''

    while attemp not in ['1', '2', '3', '4']:
        attemp = input("Choose a number between 1 and 4: ")

    return int(attemp)

result = try_luck()
print(result)

#check attemp
def check_attempt(list, attemp):
    if list[attemp - 1 ] == '-':
        print("Wash the dishes")
    else:
        print("This time you won")

    print(f"Your luck {list[attemp - 1]}")

sticks = mix(sticks)
option = try_luck()
check_attempt(sticks, option)

