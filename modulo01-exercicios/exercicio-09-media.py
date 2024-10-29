#Crie um programa que peça ao usuário
#duas notas e calcule a média. Se a média for
#maior ou igual a 7, imprima "Aprovado". Caso
#contrário, se a média estiver entre 4 e 6.9,
#imprima"Recuperação". Caso contrário estiver entre 0 e 4,
#imprima"Reprovado"

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2

if media >= 7 :
  print(f'APROVADO, Sua média foi {media}')
elif media >= 4 and media < 6.9:
  print(f'Você está em RECUPERAÇÃO, Sua média foi {media}')
elif media >= 0 and media < 4:
  print(f'Você está REPROVADO, Sua média foi {media}')
