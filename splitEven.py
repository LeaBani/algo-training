def split_integer(num, parts):
    divison = num // parts # divison entière en python "//"
    rest = num % parts

    res = [divison] * (parts - rest) + [divison + 1] * rest
    
    return res

resultat = split_integer(20, 5)
# print(resultat)