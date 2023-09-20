notas = {
    'daiane' : 12,
    'vinicius' : 12,
    'rafael' : 6,
    'vitoria' : 2,
}

soma = 0
for nota in notas.values():
    soma+=nota

media = soma/len(notas.values())

print(media)