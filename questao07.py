'''
A Loja Mamão com Açúcar está vendendo seus produtos em até 10 prestações sem juros. Faça um algoritmo que
pergunte um valor de uma compra, o número de prestações escolhidas e apresente como resultado o valor das
prestações.
'''

a = float(input("Qual o valor da compra?"))
b = float(input("Qual o número de prestações escolhidas?"))

print("")

print("O resultado do valor das prestações é de: R$", a / b)