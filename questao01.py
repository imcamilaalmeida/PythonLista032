'''
Desenvolver um programa que pergunte o valor da conta a ser paga no restaurante e exiba como resposta o
valor com o acréscimo dos 10% da gorjeta do garçom.
'''

bill = float(input("Qual o valor da conta a ser paga? R$"))

gar= 0.1

tot = bill + (bill * gar)

print("O valor a ser pago será de: R$", tot)