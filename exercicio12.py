cidades_e_estados = {
    "São Paulo": "São Paulo",
    "Rio de Janeiro": "Rio de Janeiro",
    "Belo Horizonte": "Minas Gerais",
    "Salvador": "Bahia",
    "Curitiba": "Paraná",
    "Recife": "Pernambuco",
    "Fortaleza": "Ceará",
    "Porto Alegre": "Rio Grande do Sul",
    "Goiânia": "Goiás",
    "Manaus": "Paraná"
}

estados_sem_repeticao = list(set(cidades_e_estados.values()))

print("Estados sem repetição:")
for estado in estados_sem_repeticao:
    print(estado)
