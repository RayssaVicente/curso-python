#Faça um programa que solicite o
#preço de uma mercadoria e o
#percentual de desconto. Exiba o valor
#do desconto e o preço a pagar.

preco_mercadoria = float(input("Digite o valor da mercadoria: "))
preco_desconto = int(input("Digite o valor do desconto em percentual: "))

preco_com_desconto =  (preco_desconto/100) * preco_mercadoria
preco_final = preco_mercadoria - preco_com_desconto


print(f"O valor do desconto é {preco_desconto}% sobre o valor da meracadoria que é {preco_mercadoria}, então você pagar {preco_final} ")