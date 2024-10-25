# def ler_arquivo(nome_arquivo):
#     with open(f'{nome_arquivo}.txt', 'r', encoding='utf-8') as file:
#         lista = file.readlines()
#         lista.pop(0)
#         lista.pop(-1)
        
#     with open(f'{nome_arquivo}.txt', 'w', encoding='utf-8') as file:
#         for item in lista:
#             file.write(item)


# nome_arquivo = input('Informe o nome do arquivo: ')
# ler_arquivo(nome_arquivo)

def matricular_aluno(nome_aluno, curso):
    with open('matriculas.txt', 'a', encoding='utf-8') as file:
        file.write(f'Nome: {nome_aluno}, Curso: {curso}')

nome_aluno = input('Informe o nome do aluno que sera matriculado: ')
curso = input('Informe o curso que o aluno sera matricula:')
matricular_aluno(nome_aluno, curso)