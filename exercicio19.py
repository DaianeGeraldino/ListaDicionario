from operator import itemgetter

jogadores = {
    'Cristiano Ronaldo' : 851,
    'Lionel Messi' : 819,
    'Pelé' : 767,
    'Joe Bambrick' : 629
}

maior = max(jogadores.items(), key=itemgetter(1))
print(maior)