'''
Desenvolver um programa que pergunte ao usuário o seu peso e sua altura. Ao final o programa deverá exibir na
tela o valor do índice de massa corporal desta pessoa (IMC).
Fórmula: IMC = peso / altura2 - Obs: peso em quilos e altura em metros.
'''
import math

a = int(input("Insira seu peso em quilos:"))
b = float(input("Insira sua altura em metros:"))
c = a / math.pow(b,2)

print("")

print("Seu IMC é de:", c)