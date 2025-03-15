# Faça um Programa que leia 4 notas,
# mostre as notas e a média na tela.

contador = 0
soma = 0
while contador <= 3:
    nota = float(input("Digite uma nota: "))
    contador += 1
    soma += nota
    print(f"A {contador} nota é {nota}")

media = (soma)/4
print(f"A soma total é {soma} é a media é {media}")
