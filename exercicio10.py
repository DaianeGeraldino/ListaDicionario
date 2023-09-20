dicionario = {
    "python": "alto nivel.",
    "inteligência artificial": "cria",
    "criptografia": "#",
    "robótica": "robo.",
    "algoritmo": "pensar."
}

while True:
    palavra_chave = input("Digite uma palavra-chave (ou 'sair' para encerrar): ").lower()
    if palavra_chave == 'sair':
        break
    print(dicionario.get(palavra_chave, "Palavra não encontrada no dicionário."))

