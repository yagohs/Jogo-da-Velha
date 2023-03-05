contador = True
i = 0
n1 = 1
n2 = 2
n3 = 3
n4 = 4
n5 = 5
n6 = 6
n7 = 7
n8 = 8
n9 = 9
j2 = 0
nome2 = ''

mensagemdevitoria = 'Você Ganhou! '
nome1 = input('Jogador 1 escolha entre O e X')
if nome1 == 'x':
    nome2 = 'o'
else:
    nome2 = 'x'
while True:

    print(f'     {n1}  |  {n2}  |  {n3}  ')
    print('   -----+-----+-----')
    print(f'     {n4}  |  {n5}  |  {n6}  ')
    print('   -----+-----+-----')
    print(f'     {n7}  |  {n8}  |  {n9}  ')


    if contador == True:
        j1 = int(input('Jogador 1 digite um Número entre 1 à 9'))
        contador = False
    else:
        j2 = int(input('Jogador 2 digite um Número entre 1 à 9'))
        contador = True

    if n1 == j1:
        n1 = nome1
    elif n1 == j2:
        n1 = nome2

    if n2 == j1:
        n2 = nome1
    elif n2 == j2:
        n2 = nome2

    if n3 == j1:
        n3 = nome1
    elif n3 == j2:
        n3 = nome2

    if n4 == j1:
        n4 = nome1
    elif n4 == j2:
        n4 = nome2

    if n5 == j1:
        n5 = nome1
    elif n5 == j2:
        n5 = nome2

    if n6 == j1:
        n6 = nome1
    elif n6 == j2:
        n6 = nome2

    if n7 == j1:
        n7 = nome1
    elif n7 == j2:
        n7 = nome2

    if n8 == j1:
        n8 = nome1
    elif n8 == j2:
        n8 = nome2

    if n9 == j1:
        n9 = nome1
    elif n9 == j2:
        n9 = nome2

    #if (n1 == nome1 and n2 == nome1 and n3 == nome1 :
        #print('Voce ganhou')
       # break
    if (n1 == n2 == n3):
        if n1 == nome1:
            print(f'Jogador 1, {mensagemdevitoria}')
        else:
            print(f'Jogador 2, {mensagemdevitoria}')
        break

    elif (n1 == n4 == n7):
        if n1 == nome1:
            print(f'Jogador 1, {mensagemdevitoria}')
        else:
            print(f'Jogador 2, {mensagemdevitoria}')
        break

    elif (n1 == n5 == n9):
        if n1 == nome1:
            print(f'Jogador 1, {mensagemdevitoria}')
        else:
            print(f'Jogador 2, {mensagemdevitoria}')
        break

    elif (n2 == n5 == n8):
        if n2 == nome1:
            print(f'Jogador 1, {mensagemdevitoria}')
        else:
            print(f'Jogador 2, {mensagemdevitoria}')
        break

    elif (n3 == n6 == n9):
        if n3 == nome1:
            print(f'Jogador 1, {mensagemdevitoria}')
        else:
            print(f'Jogador 2, {mensagemdevitoria}')
        break

    elif (n3 == n5 == n7):
        if n3 == nome1:
            print(f'Jogador 1, {mensagemdevitoria}')
        else:
            print(f'Jogador 2, {mensagemdevitoria}')
        break

    elif (n4 == n5 == n6):
        if n4 == nome1:
            print(f'Jogador 1, {mensagemdevitoria}')
        else:
            print(f'Jogador 2, {mensagemdevitoria}')
        break

    elif (n7 == n8 == n9):
        if n7 == nome1:
            print(f'Jogador 1, {mensagemdevitoria}')
        else:
            print(f'Jogador 2, {mensagemdevitoria}')
        break