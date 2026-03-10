# def addition(**kwargs):
#     print(type(kwargs))
#
# addition(x=3, y=5, z=2)

def addition(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} = {value}")

addition(x=3, y=5, z=2)

