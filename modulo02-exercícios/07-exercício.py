#  Crie um programa que permita
# calcular o valor total a ser pago em uma
# compra, levando em consideração os
# produtos adquiridos e suas quantidades.

ListaPrecos = {"Maça": 10.20,
               "Pera": 7.12, "Uva": 3.80, "Morango": 12.50}

print("Produtos disponíveis:")
for produto, preco in ListaPrecos.items():
    print(f"{produto}: R$ {preco:.2f}")

produto_escolhido = input("Digite o nome do produto que deseja comprar: ").strip().capitalize()

if produto_escolhido in ListaPrecos:
    quantidade = int(input(f"Quantas unidades de {produto_escolhido} deseja comprar? "))
    
    
    valor_total = quantidade * ListaPrecos[produto_escolhido]

    
    print(f"Você comprou {quantidade} {produto_escolhido}(s). Total a pagar: R$ {valor_total:.2f}")
else:
    print("Produto não encontrado. Verifique o nome e tente novamente.")