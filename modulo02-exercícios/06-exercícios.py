# Escreva um programa que
# compare duas listas. Utilizando
# operações com conjuntos, imprima:
# os valores comuns às duas listas os
# valores que só existem na primeira
# os valores que existem apenas na
# segunda
# uma lista com os elementos não
# repetidos das duas listas.

Lista1 = [1, 2, 3, 4, 5, 6,]
Lista2 = [7, 8, 3, 4, 11, 12]

set1 = set(Lista1)
set2 = set(Lista2)

comuns = set1 & set2
primeira = set1 - set2
segunda = set2 -set1
nao_repeticao = set1 ^ set2

print(f"Valores comuns ás duas listas: {comuns}")
print(f"Valores que só tem na primeira lista: {primeira}")
print(f"Valores que só tem na segunda lista: {segunda}")
print(f"Valores que não repetidos nas duas lista: {nao_repeticao}")