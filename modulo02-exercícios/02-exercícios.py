# Escreva um programa que permaneça em
# laço lendo números inteiros enquanto os
# valores digitados forem diferentes de zero.
# Cada número não zero digitado deve ser
# incluído em uma lista. Ao final, exiba a lista e
# seu tamanho.

lista = []


while True:
    numero = int(input("Digite numeros inteiros: "))
    if numero == 0:
     break 


    lista.append(numero)

print(f"Lista de números digitados {lista}")
print(f"A quantidade de números listados é {len(lista)}")
        

