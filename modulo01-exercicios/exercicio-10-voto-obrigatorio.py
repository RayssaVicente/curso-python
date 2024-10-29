#Elabore um programa que solicite a idade e
#informe quanto à obrigatoriedade do voto.

idade = int(input('Digite sua idade: '))

if idade >= 18 and idade <= 70:
  print(f'O voto é obrigatorio por que sua idade é {idade}')
elif (idade >= 16 and idade < 18) or idade > 70:
  print(f'O seu voto é facultativo por que sua idade é {idade}')
elif idade >=0 and idade < 16:
  print(f'O voto não é permitido')
else:
  print('Dado invalido ')