produtos = {
    'calca' : 200,
    'blusa' : 150,
    'sapato' : 120,
    'oculos' : 150
}

for produto in produtos.items():
    if produto[1] < 150:
        print(f"O {produto[0]} a baixo do estoque")
    elif produto[1]>=150:
        print(f"O {produto[0]} estoque OK")