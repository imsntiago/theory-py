# def check_3_digits(number):
#     return number in range(100, 1000)
#
# # addition = 599 + 377
#
# result = check_3_digits(addition)
# print(result)

# def check_3_digits(list):
#     for n in list:
#         if n in range(100, 1000):
#             return True
#         else:
#             pass
#
#     return False
#
# result = check_3_digits([55, 99, 6000])
# print(result)

def check_3_digits(list):

    list_3_digits = []

    for n in list:
        if n in range(100, 1000):
            list_3_digits.append(n)
        else:
            pass

    return list_3_digits

result = check_3_digits([555, 99, 600])
print(result)
