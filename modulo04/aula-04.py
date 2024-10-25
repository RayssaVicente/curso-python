#Estudo dirigido 7

#Exercício 05

def verificar_numero(numero):
    if numero >0:
        return 'p'
    else:
        return 'n'

#Chamada da função 

numero = float(input('Digite um número: '))
retorno = verificar_numero(numero)

if retorno == 'p':
    print('O numero informado é positivo')
else:
    print('O numero informado é negativo ou zero')


def contar_digitos(numero):
    return len(numero)

numero = input('Informe um número inteiro')
print(contar_digitos(numero))


#Exercício 08

def  verificar_strings(palavra1, palavra2):
    if len(palavra1) == len(palavra2):
        print('As palavras possuem o mesmo comprimento')
    else:
        print('As palavras NÂO possuem o mesmo conteudo')
    if palavra1 == palavra2:
        print('As palavras contem o mesmo conteudo')
    else:
        print("As palavras NÂO possuem o mesmo conteudo")
    

#Exercício 10

def decimal_binario(numero):
    numero_binario = []
    while True:
        resto = numero % 2
        numero = numero // 2
        numero_binario .append(resto)
        if numero < 2:
            numero_binario.append(numero)
            numero_binario.reverse()
            break
    return numero_binario

numero = int(input('Digite um número inteiro: '))
lista = (decimal_binario(numero))
for numero in lista:
    print(numero, end='')

#Exercício 11

def Eprimo(numero):
    for item in range(1, numero+1):
        #depois faço

#Exercício 12

def pertence_intervalo(numero_minimo, numero_maximo):
    numero = float(input('Digite um número real: '))
    if numero >= numero_minimo and numero_maximo:
        return f'o número {numero} pertence ao intervalo[{numero_minimo}, {numero_maximo}]'
    else:
        print(f'O número{numero}')

