'''
Faça um algoritmo que leia a idade de uma pessoa expressa em anos, meses e dias e mostre-a expressa apenas
em dias. Obs: Considere os anos com 365 dias e os meses com 30 dias.
'''

a = int(input("Qual a sua idade em anos?"))
b = int(input("Qual a sua idade em meses?"))
c = int(input("Qual a sua idade em dias?"))

d = (a * 365) + (b * 30) +(c)

print("")
print("A sua idade é de", d, "dias")