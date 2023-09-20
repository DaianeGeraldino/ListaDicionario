filmes = {
    'O castelo no céu' : 1989,
    'Sussuros no coracao' : 1995,
    'O serviço de Entregas da kiki' : 1989,
    'Tumulo de vagalumes' : 1988
}

for item in sorted(filmes, key=filmes.get):
    print (item, filmes[item])