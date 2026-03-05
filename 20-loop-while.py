# coins = 5
#
# while coins > 0:
#     print(f"I have {coins} coins")
#     coins -= 1
# else:
#     print("I dont have more money")

# answer = 's'
#
# while answer == 's':
#     answer = input("Do you want to continue? (s/n): ")
# else:
#     print("Gracias")

# answer = 's'
#
# while answer == 's':
#     pass
#
# print("Gracias")

# name = input("Your name: ")
# for letter in name:
#     if letter == 'r':
#         break
#     print(letter)

name = input("Your name: ")
for letter in name:
    if letter == 'r':
        continue
    print(letter)

