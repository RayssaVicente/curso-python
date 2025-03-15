# Crie uma tupla chamada numeros com
# números inteiros. Verifique se um número
# específico está presente na tupla e imprima
# "Encontrado"ou"Não encontrado".

tupla =(2, 4, 5, 6, 8, 9, 10)

while True:
    numero = int(input("Digite um número: "))
    
    if numero in tupla:
        print("Número Encontrado")
    else:
        print("Número Não Encontrado")
      