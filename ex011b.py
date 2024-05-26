km = int(input('Qual é a distancia da sua viagem: '))
valor = km * 0.55
print('\033[33m=\033[m' * 40)
if km > 200:
    print('Sua viagem vai ter \033[32m"Desconto"\033[m \npor ser acima de \033[31m200Km\033[m')
    print('Você vai pagar \033[34mR$ {}\033[m'.format(km * 0.45))
else:
    print('A sua viagem vai custar R$ {:.2f}'.format(valor))
print('\033[33m=\033[m' * 40)
