# Crie um programa que recebe uma
#string e substituia todas as ocorrências


texto = input("Digite uma frase: ")


antigo = input("Digite o trecho a ser substituído: ")


novo = input("Digite o novo valor: ")


texto_modificado = texto.replace(antigo, novo)


print("Texto modificado:", texto_modificado)
