# funções - definição e caracteristicas

#Bloco de código reutilizavel que executa uma tarefa especifica
# Uma função deve resolver somente um problema 
# Quanto mais generica for a solução , maior a possibilidade de reutilizá 

# sintaxe 
# def nome_da_função(#parametros):
    # return(#parametros)

# exercício 03

# def Paridade(numero):
#     if numero %2 == 0:
#         return True
#     else:
#         return False
    
# #Chamada da função
# resultado = Paridade(500)

# print(resultado)

#Exercício 04

# def calcular_desconto(preco_original, percentual_desconto):
#     preco_desconto = preco_original - percentual_desconto*preco_original
#     return preco_desconto

# # Chamada da função
# preco_original = float(input('Digite o valor do produto: '))
# percentual = float(input('Digite o percentual de desconto: '))
# resultado = calcular_desconto(preco_original100, percentual)
# print(f'O valor do produto com o desconto é R$ {resultado}')

#Exercício 05

# def saudacao(nome, mensagem = 'Olá'):
#     print(f'{mensagem}, {nome}')

# nomes =['francisco', 'Jorge', 'Marcos']
# #Chamada da Função
# saudacao(nomes, 'Oi')~


#Estudo Dirigido 07

#Exercício 01



# def palindromo(frase):
#     frase_sem_espaco = frase.replace(' ','')
#     frase_invertida = frase_sem_espaco[::-1]
#     if frase_sem_espaco == frase_invertida:
#         print(f'Essa frase {frase} é um PALINDROMO')
#     else:
#         print(f'Essa frase {frase} NÃO é um palindromo')

# #Chamada da função

# palindromo('Socorram me subi no onibus em Marrocos'.lower())


    


#Exercício 02

# def exibir_telefone(telefone):
#     telefone_formatado = telefone.replace('-','')
#     if len(telefone_formatado) == 7:
#         telefone_formatado = '3' + telefone_formatado
#         print(f'O telefone é {telefone_formatado}')

# #Chamada da função

# numero_telefone = input('Digite o numero do telefone: ')
# exibir_telefone(numero_telefone)


#Exercício 03

# def soma(n1, n2, n3):
#     return n1 + n2 + n3

# somas = soma(4, 5, 6)
# print(somas)

# #Exercício 04

# def area_triangulo (base, altura):
#     return base * altura / 2

# resultado = area_triangulo(10, 5)
# print(resultado)




