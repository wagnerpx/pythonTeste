from palavraforca import palavra
letras_usuario = []
chances = 5
ganhou = False

while True:

    for letra in palavra:
        if letra.lower() in letras_usuario:
            print(letra, end=" ")
        else:
            print("_", end=" ")
    print(f"Você tem {chances} vidas")
    tentativa = input("Escolha uma letra para adivinhar: ")
    letras_usuario.append(tentativa.lower())
    if tentativa.lower() not in palavra.lower():
        chances -= 1

    ganhou = True
    for letra in palavra:
        if letra.lower() not in letras_usuario:
            ganhou = False

    if chances == 0 or ganhou:
        break

if ganhou:
    print(f"Parabens você ganhou! A palavra secreta é \033[34m{palavra}\033[m")
else:
    print(f"Você perdeu! A palavra era {palavra}")
