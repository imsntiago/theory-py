serie = "N-02"

# if serie == "N-01":
#     print("Samsung")
# elif serie == "N-02":
#     print("Nokia")
# elif serie == "N-03":
#     print("Motorola")
# else:
#     print("The product does not exist")

# match serie:
#     case "N-01":
#         print("Samsung")
#     case "N-02":
#         print("Nokia")
#     case "N-03":
#         print("Motorola")
#     case _:
#         print("The product does not exist")

client = {'name': 'Federico',
          'age': 45,
          'occupation': 'instructor'}

movie = {'title': 'Matrix',
         'technical_file': {'Star': 'Keanu Reeves',
                            'director': 'Lana and Lilly Wachowski'}}

elements = [client, movie, 'book']

for e in elements:
    match e:
        case {'name': name,
              'age': age,
              'occupation': occupation}:
            print("It\'s a client")
            print(name, age, occupation)

        case {'title': title,
              'technical_file': {'star': star,
                                 'director': director}}:
            print('It\'s a movie')
            print(title, star, director)

        case _:
            print("I don\'t know")



