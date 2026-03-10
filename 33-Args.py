# def addition(a, b):
#     return a+b
#
# print(addition(5, 6, 5))

# def addition(*args):
#     total = 0
#
#     for arg in args:
#         total += arg
#
#     return total
#
# print(addition(5, 6, 5))

def addition(*args):

    return sum(args)

print(addition(5, 6, 5))