#Escreva um programa que
#recebe uma string do usuário e
#conta o número de vogais (a, e, i, o,u) na string

string = input("Digite uma palavra: ").lower()
contador = 0

for letras in string:
    if letras in 'aeiou':
        contador += 1

print(f'Essa palavra tem {contador} vogais.') 
