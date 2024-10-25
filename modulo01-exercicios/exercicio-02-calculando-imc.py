#Desenvolva um algoritmo
#capaz de calcular o IMC(Índice
#de Massa Corpórea) de uma
#pessoa.

print("Para calcular o IMC")
peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))
imc = peso / (altura*altura)
print(f"Seu IMC é {imc:.2f}")