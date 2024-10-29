#Uma empresa concederá um aumento de salário
#aos seus funcionários, variável de acordo com o
#cargo, conforme mostra a tabela
#Crie um programa que solicite ao usuário o salário e o
#cargo de um determinado funcionário. Na sequência,
#o programa deve calcular e imprimir o seu novo
#salário. Caso o cargo informado não esteja na tabela,
#o programa deve imprimir“Cargo inválido”.

cargo = input("Digite seu cargo: ")
salario = float(input("Digite seu salario: "))

if cargo == 'Programador de Sistemas':
    aumento = salario*(30/100)
    novo_salario = salario + aumento
    print(f"Ocorreu um aumento de 30% no seu salario, seu novo salario é {novo_salario}")
elif cargo == 'Analise de Sistemas':
    aumento = salario*(20/100)
    novo_salario = salario + aumento
    print(f"Ocorreu um aumento de 20% no seu salario, seu novo salario é {novo_salario}")
elif cargo == 'Analise de Banco de Dados':
    aumento = salario*(15/100)
    novo_salario = salario + aumento
    print(f"Ocorreu um aumento de 15% no seu salario, seu novo salario é {novo_salario}")
else:
    print("Cargo inválido")