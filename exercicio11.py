paises_capitais = {
    "Brasil": "Brasília",
    "Estados Unidos": "Washington, D.C.",
    "França": "Paris",
    "Japão": "Tóquio",
    "Índia": "Nova Deli",
    "Rússia": "Moscou",
    "China": "Pequim",
    "Canadá": "Ottawa",
    "Austrália": "Canberra",
    "Alemanha": "Berlim"
}

while True:
    capital = input("Digite o nome de uma capital para encontrar o país correspondente (ou 'sair' para encerrar): ").capitalize()
    
    if capital == 'Sair':
        break
    
    pais = "País não encontrado."
    for key, value in paises_capitais.items():
        if value == capital:
            pais = key
            break
    
    print(f"A capital {capital} pertence ao país {pais}.")
