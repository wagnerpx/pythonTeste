frase = 'Wagner Alexandre Peixoto da Silva'
frase.count(' ')
nfrase = frase.replace(' ', '')
letras = len(nfrase.strip())
print('Seu nome tem {} letras.'.format(letras))
print(frase.upper())
print(frase.lower())
nome = frase.split()
print('Seu primeiro nome é {}'.format(nome[0]))
t = len(nome[0][0:])
print(t)