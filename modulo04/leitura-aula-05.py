# Abertura do arquivo

# file = open('registros.txt', 'r', encoding='utf-8')

# Leitura do Arquivo
# print(file.read()) retorna o conteúdo do arquivo por completo
#print(file.readline()) #retorna o conteúdo da primeira linha
#print(file.readlines()) #cloca numa lista e separa os elementos de cada linha
# file.write() # adiciona uma dado no arquivo
# file.close() # fecha o arquivo


# def gravar_arquivo(nome_arquivo, dado):
#     file = open(nome_arquivo+'.txt', 'a', encoding='utf-8')
#     file.write('\n'+dado)
#     file.close()


# nome_arquivo = input('Informe o nome do arquivo: ')
# dado = input('Informe o conteúdo que deseja salvar: ')
# gravar_arquivo(nome_arquivo, dado)

# def leitura_arquivo(nome_aquivo):
#     #Abertura do arquivo
#     file = open(nome_aquivo+'.txt', 'r', encoding='utf-8')
#     #Leitura do arquivo
#     for item in file.readlines():
#         print(item)
#     #Fechamento do arquivo
#     file.close()

# nome_arquivo = input('Informe o nome do arquivo: ')
# leitura_arquivo(nome_arquivo)


# def leitura_arquivo(nome_aquivo):
#     #Abertura do arquivo e fechamento do arquivo automaticamente
#     with open(nome_aquivo+'.txt', 'a', encoding='utf-8') as file:
    
#     #Leitura do arquivo
#         file.write('\n'+dado)
    

# nome_arquivo = input('Informe o nome do arquivo: ')
# leitura_arquivo(nome_arquivo)