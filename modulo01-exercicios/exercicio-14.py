#Escreva um programa que
#solicita ao usuário um número
#inteiro positivo n e calcula a soma
#de todos os números pares de 1 a n.

n = int(input('Digite um número inteiro positivo: '))

soma = 0
contador = 1  

while contador <= n:
    if contador % 2 == 0:  
        soma += contador  
    contador += 1 

print(f'A soma dos números pares de 1 a {n} é {soma}')
