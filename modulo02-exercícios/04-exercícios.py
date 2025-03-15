#  Crie uma tupla chamada alunos com
# informações de alunos, onde cada
# elemento da tupla é uma sub-tupla com
# nome, idade e nota. Imprima o nome do
# aluno com a maior nota.

alunos = (
    ("Julia", 20, 10),
    ("Jua", 22, 8.5),
    ("Jo", 19, 9.0),
    ("Lia", 21, 10)
)


aluno_maior_nota = max(alunos, key=lambda aluno: aluno[2])


print(f"O aluno com a maior nota é {aluno_maior_nota[0]}, com nota {aluno_maior_nota[2]}.")





