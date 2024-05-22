# nome = input('Qual é o seu nome? ')
# print('Prazer em te conhecer {:=^40}'.format(nome))

# n1 = int(input('Primeiro valor: '))
# n2 = int(input('Segundo valor: '))
# print('A soma vale {}'.format(n1 + n2))

n1 = int(input('Digite um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('\n\nA soma é {}, \no produto é {} \ne a divisão é {:.2f}'.format(s, m, d))
print('Divisão inteira {} \ne potência {}'.format(di, e))
