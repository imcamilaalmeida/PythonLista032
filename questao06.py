'''
Fazer um algoritmo que pergunte o nome de um vendedor, o seu salário fixo e o total de vendas efetuadas por
ele no mês (em dinheiro). Sabendo que este vendedor ganha 15% de comissão sobre suas vendas efetuadas,
exibir ao final o seu nome, o salário fixo, a comissão e o salário completo (fixo + comissão sobre vendas) no final
do mês
'''



a = input("Qual o seu nome?")
b = int(input("Qual o seu salário fixo?"))
c = int(input("Qual o total de vendas efetuadas nesse mês?"))

print("")

print("Olá,", a, "! Seu salário é de: R$", b, ", sua comissão do mês é de R$", c * 0.15, "e seu salário completo é de R$", b + (c * 0.15))