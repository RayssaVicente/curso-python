# Crie um dicionário que represente um
# catálogo de livros, onde as chaves são
# os títulos dos livros e os valores são os
# autores. Escreva um programa que
# solicite novos livros ao usuário e
# adicione ao catálogo até que o usuário
# informe que não deseja continuar a
# inserir livros.


Livros = {
    "Jogos Vorazes": "The Hunger",
    "Pânico": "Lauren Oliver",
    "Velozes e Furiosos": "Vin Diesel",
    "Rambo" : "Ted Kotcheff",
    "Mercenarios": "Sylvester Stallone",
    "Missão Impossivel": "Christopher MCQuarrie"
}

adicionar = ""

while True:
    adicionar = input("Deseja adicionar um livro? ")
    if adicionar == "sim":
        livrosNome = input("Digite o nome de um livro: ")
        livrosAutor = input("Digite o nome do Autor: ")
        Livros.update({livrosNome: livrosAutor})
    else:
        break

print(Livros)