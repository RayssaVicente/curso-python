#Escreva uma expressão que avalie se
#uma pessoa deve ou não pagar
#imposto. Considere que pagam
#imposto pessoas cujo salário é maior
#que R$ 1200.

salario = float(input("Digite seu salario: "))
if salario > 1200:
    print("Você devera pagar imposto de renda, poís seu salario e maior que R$1200")
else:
    print("Você não ira pagar imposto de renda pois seu salario não é maior que R$ 1200")