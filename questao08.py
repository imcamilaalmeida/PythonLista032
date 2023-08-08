'''
Fazer um algoritmo que receba o preço de custo de um produto e mostre como resposta o valor de venda. Sabe-
se que o preço de custo receberá um acréscimo de acordo com um percentual informado pelo usuário.
'''

a = int(input("Qual o preço de custo do produto?"))
b = int(input("Qual o percentual de acréscimo?"))
c = b / 100
print("")

print("O valor de venda do produto será de: R$", (a * c) + a)