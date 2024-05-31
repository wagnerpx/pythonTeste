print('Vou classificar o seu nome!')
nome = str(input('Digite o seu nome? ')).title().strip()
if nome == 'Wagner':
    print('É um nome Forte!')
elif nome == 'Maria' or nome == 'João' or nome == 'José':
    print('Seu nome é muito popular no Brasil!')
else:
    print('é um nome comum.')
print(f'Tenha um bom dia, {nome}!')
