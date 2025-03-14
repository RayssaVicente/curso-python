#Escreva um programa que mostre na
#tela os dez primeiros termos de uma
#progressão aritmética (PA) com
#primeiro termo P e razão R. Os dois
#números P e R são inteiros e devem ser
#lidos do teclado.

termo_pa = int(input('Digite o primeiro termo da PA: '))
razao_pa = int(input('Digite a razão da PA: '))
contador_termos = 1
termo_anterior = termo_pa
print(f'O 1° termo equivale a {termo_pa}')

while(contador_termos < 10):
  proximo_termo = termo_anterior + razao_pa
  print(f'O{contador_termos+1}° equivale a {proximo_termo}')
  contador_termos = contador_termos + 1
  termo_anterior = proximo_termo