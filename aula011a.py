cores = {'limpa': '\033[m,',
         'azul': '\033[34m',
         'amarelo': '\033[7;33m',
         'pretoebranco': '\033[7;30m'}
nome = str(input('Seu nome: '))
print('Prazer em te conhecer {}{}{}'.format(cores['amarelo'], nome, cores['limpa']))
