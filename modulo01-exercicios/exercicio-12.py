#Faça um programa que solicite um
#número ao usuário e que imprima a
#tabuada da multiplicação desse
#número de 1 até 10.

numero = int(input("Digite um número para saber a tabuada: "))
contador = 1

while(contador <= 10):
    print(f'{contador} X {numero} = {contador * numero}')
    contador = contador + 1