coffe_price = [('Capuchino', 1.5), ('Expresso', 1.2), ('Moka', 1.9)]

# for element in coffe_price:
#     print(element)

# for coffe, price in coffe_price:
#     # print(coffe)
#     print(price * 0.45)

def expensive_coffe(list_prices):
    higher_price = 0
    expensive_coffe = ''

    for coffe, price in list_prices:
        if price > higher_price:
            higher_price = price
            expensive_coffe = coffe
        else:
            pass

    return (expensive_coffe, higher_price)

print(expensive_coffe(coffe_price))