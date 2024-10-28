#Crie um programa que solicite ao usuário uma
#senha e compare com a senha armazenada em uma
#variável. Se as senhas forem iguais, exiba"Acesso
#permitido", caso contrário, exiba"Acesso negado".

senha = int(input("Digite sua senha(somente com números): "))
senha_verificacao = int(input("Digite sua senha novemente(soemnete com números): "))
if senha == senha_verificacao:
    print("Acesso permitido")
else:
    print("Acesso negado")