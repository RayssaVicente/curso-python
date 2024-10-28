#Escreva um programa que calcule o
#tempo de uma viagem de carro.
#Pergunte a distância a percorrer e a
#velocidade média esperada para a
#viagem.

print("Vamos calcular o tempo da sua viagem de carro")
distancia = float(input("Digite a distancia que ira pecorrer na viagem: "))
velocidade_media = float(input("Digite a velocidade media do seu carro: "))
tempo = distancia/velocidade_media
print(f"O tempo que você ira precisar para fazer essa viagem com distancia de {distancia}km e velociade de {velocidade_media} é {tempo:.2}h")