import operator

frutas = {
    'Abacate' : 5,
    'Banana' : 10,
    'Amora' : 7,
    'Bacaba' : 2
}

maior = max(frutas.items(), key=operator.itemgetter(1))

print(maior)