# Tarefa Cálculo Númerico módulo 1 - Python/Aps1
# Esse programa teve como base o seguinte documento: https://www.ic.unicamp.br/~mc102/mc102-2s2018/labs/roteiro-lab09.html

# Cartela com 24 números distintos dispostos em uma matriz com 5 linhas e 5 colunas, sendo que o elemento central não recebe número.
# Os números da primeira coluna devem estar no intervalo de 1 a 15.
# Os números da segunda coluna devem estar no intervalo de 16 a 30.
# Os números da terceira coluna devem estar no intervalo de 31 a 45.
# Os números da quarta coluna devem estar no intervalo de 46 a 60.
# Os números da quinta coluna devem estar no intervalo de 61 a 75.
# Os números são sorteados e anunciados juntamente com o identificador das colunas, como, por exemplo, B-02, I-17 ou G-54.

# REGRA: O jogador ganha se completar com os números sorteados = UMA LINHA, UMA COLUNA ou UMA DIAGONAL.
# EXEMPLO: +----------------+ +----------------+ +----------------+ +----------------+
#          | B  I  N  G  O  | | B  I  N  G  O  | | B  I  N  G  O  | | B  I  N  G  O  |
#          +================+ +================+ +================+ +================+
#          | 12 24 43 49 72 | | 12 24 XX 49 72 | | XX 24 43 49 72 | | 12 24 43 49 XX |
#          | 07 23 31 57 62 | | 07 23 XX 57 62 | | 07 XX 31 57 62 | | 07 23 31 XX 62 |
#          | 04 20 XX 51 73 | | 04 20 XX 51 73 | | 04 20 XX 51 73 | | 04 20 XX 51 73 |
#          | XX XX XX XX XX | | 08 21 XX 50 61 | | 08 21 38 XX 61 | | 08 XX 38 50 61 |
#          | 05 27 40 54 63 | | 05 27 XX 54 63 | | 05 27 40 54 XX | | XX 27 40 54 63 |
#          +----------------+ +----------------+ +----------------+ +----------------+

# O jogador tem direito a uma única cartela por partida.

#INÍCIO DE CÓDIGO
#A numeração das bolas vai de 01 - 75.

# 1- Gerar a Cartela do Participante e imprimir na tela.
# 2- Lista que contenha os números SORTEADOS.
# 3- Lista que contenha os numeros MARCADOS.
# 4- Lista que contenha os numeros NÃO MARCADOS.

import random as rd

# Cria a lista de Números disponíveis
NumerosB = []
for x in range(1, 16):
    NumerosB.append(x)
NumerosI = []
for x in range(16, 31):
    NumerosI.append(x)
NumerosN = []
for x in range(31, 46):
    NumerosN.append(x)
NumerosG = []
for x in range(46, 61):
    NumerosG.append(x)
NumerosO = []
for x in range(61, 76):
    NumerosO.append(x)

# Lista completa de Números
Numeros = NumerosB + NumerosI + NumerosN + NumerosG + NumerosO
ColunaB = rd.sample(NumerosB, 5)
ColunaI = rd.sample(NumerosI, 5)
ColunaN = rd.sample(NumerosN, 4)
ColunaG = rd.sample(NumerosG, 5)
ColunaO = rd.sample(NumerosO, 5)
linha1 = []
linha2 = []
linha3 = []
linha4 = []
linha5 = []
digSec = []
digPri = []

for x in range(0, 1):
    linha1.append(ColunaB[0])
    linha1.append(ColunaI[0])
    linha1.append(ColunaN[0])
    linha1.append(ColunaG[0])
    linha1.append(ColunaO[0])
    linha2.append(ColunaB[1])
    linha2.append(ColunaI[1])
    linha2.append(ColunaN[1])
    linha2.append(ColunaG[1])
    linha2.append(ColunaO[1])
    linha3.append(ColunaB[2])
    linha3.append(ColunaI[2])
    # linha3.append(ColunaN[2])
    linha3.append(ColunaG[2])
    linha3.append(ColunaO[2])
    linha4.append(ColunaB[3])
    linha4.append(ColunaI[3])
    linha4.append(ColunaN[2])
    linha4.append(ColunaG[3])
    linha4.append(ColunaO[3])
    linha5.append(ColunaB[4])
    linha5.append(ColunaI[4])
    linha5.append(ColunaN[3])
    linha5.append(ColunaG[4])
    linha5.append(ColunaO[4])
    digPri.append(ColunaO[0])
    digPri.append(ColunaG[1])
    digPri.append(ColunaI[3])
    digPri.append(ColunaB[4])
    digSec.append(ColunaB[0])
    digSec.append(ColunaI[1])
    digSec.append(ColunaG[3])
    digSec.append(ColunaO[4])


cartela = ColunaB + ColunaI + ColunaN + ColunaG + ColunaO

print(f'Lista de Números: %s\nLista de Números da cartela: %s\n' % (Numeros, cartela))
print('-=' * 16)
print()

# Display da cartela.
space = " "
XX = "XX"
print(f'Sua cartela contém os seguintes números:\n', cartela)
print(f"""
        +----------------+
        | B  I  N  G  O  |
        +================+
        | """ + '{:>2}'.format(str(cartela[0])) + space + str(cartela[5]) + space + str(cartela[10]) + space + str(cartela[14]) + space + str(cartela[19]) + """ |
        | """ + '{:>2}'.format(str(cartela[1])) + space + str(cartela[6]) + space + str(cartela[11]) + space + str(cartela[15]) + space + str(cartela[20]) + """ |
        | """ + '{:>2}'.format(str(cartela[2])) + space + str(cartela[7]) + space + XX + space + str(cartela[16]) + space + str(cartela[21]) + """ |
        | """ + '{:>2}'.format(str(cartela[3])) + space + str(cartela[8]) + space + str(cartela[12]) + space + str(cartela[17]) + space + str(cartela[22]) + """ |
        | """ + '{:>2}'.format(str(cartela[4])) + space + str(cartela[9]) + space + str(cartela[13]) + space + str(cartela[18]) + space + str(cartela[23]) + """ |
        +----------------+
    """)

# Cartela editável
cartaEditavelB = (f"""
        +----------------+
        | B  I  N  G  O  |
        +================+
        | """ + XX + space + str(cartela[5]) + space + str(cartela[10]) + space + str(cartela[14]) + space + str(cartela[19]) + """ |
        | """ + XX + space + str(cartela[6]) + space + str(cartela[11]) + space + str(cartela[15]) + space + str(cartela[20]) + """ |
        | """ + XX + space + str(cartela[7]) + space + XX + space + str(cartela[16]) + space + str(cartela[21]) + """ |
        | """ + XX + space + str(cartela[8]) + space + str(cartela[12]) + space + str(cartela[17]) + space + str(cartela[22]) + """ |
        | """ + XX + space + str(cartela[9]) + space + str(cartela[13]) + space + str(cartela[18]) + space + str(cartela[23]) + """ |
        +----------------+
    """)
cartaEditavelI = (f"""
        +----------------+
        | B  I  N  G  O  |
        +================+
        | """ + '{:>2}'.format(str(cartela[0])) + space + XX + space + str(cartela[10]) + space + str(cartela[14]) + space + str(cartela[19]) + """ |
        | """ + '{:>2}'.format(str(cartela[1])) + space + XX + space + str(cartela[11]) + space + str(cartela[15]) + space + str(cartela[20]) + """ |
        | """ + '{:>2}'.format(str(cartela[2])) + space + XX + space + XX + space + str(cartela[16]) + space + str(cartela[21]) + """ |
        | """ + '{:>2}'.format(str(cartela[3])) + space + XX + space + str(cartela[12]) + space + str(cartela[17]) + space + str(cartela[22]) + """ |
        | """ + '{:>2}'.format(str(cartela[4])) + space + XX + space + str(cartela[13]) + space + str(cartela[18]) + space + str(cartela[23]) + """ |
        +----------------+
    """)
cartaEditavelN = (f"""
        +----------------+
        | B  I  N  G  O  |
        +================+
        | """ + '{:>2}'.format(str(cartela[0])) + space + str(cartela[5]) + space + XX + space + str(cartela[14]) + space + str(cartela[19]) + """ |
        | """ + '{:>2}'.format(str(cartela[1])) + space + str(cartela[6]) + space + XX + space + str(cartela[15]) + space + str(cartela[20]) + """ |
        | """ + '{:>2}'.format(str(cartela[2])) + space + str(cartela[7]) + space + XX + space + str(cartela[16]) + space + str(cartela[21]) + """ |
        | """ + '{:>2}'.format(str(cartela[3])) + space + str(cartela[8]) + space + XX + space + str(cartela[17]) + space + str(cartela[22]) + """ |
        | """ + '{:>2}'.format(str(cartela[4])) + space + str(cartela[9]) + space + XX + space + str(cartela[18]) + space + str(cartela[23]) + """ |
        +----------------+
    """)
cartaEditavelG = (f"""
        +----------------+
        | B  I  N  G  O  |
        +================+
        | """ + '{:>2}'.format(str(cartela[0])) + space + str(cartela[5]) + space + str(cartela[10]) + space + XX + space + str(cartela[19]) + """ |
        | """ + '{:>2}'.format(str(cartela[1])) + space + str(cartela[6]) + space + str(cartela[11]) + space + XX + space + str(cartela[20]) + """ |
        | """ + '{:>2}'.format(str(cartela[2])) + space + str(cartela[7]) + space + XX + space + XX + space + str(cartela[21]) + """ |
        | """ + '{:>2}'.format(str(cartela[3])) + space + str(cartela[8]) + space + str(cartela[12]) + space + XX + space + str(cartela[22]) + """ |
        | """ + '{:>2}'.format(str(cartela[4])) + space + str(cartela[9]) + space + str(cartela[13]) + space + XX + space + str(cartela[23]) + """ |
        +----------------+
    """)
cartaEditavelO = (f"""
        +----------------+
        | B  I  N  G  O  |
        +================+
        | """ + '{:>2}'.format(str(cartela[0])) + space + str(cartela[5]) + space + str(cartela[10]) + space + str(cartela[14]) + space + XX + """ |
        | """ + '{:>2}'.format(str(cartela[1])) + space + str(cartela[6]) + space + str(cartela[11]) + space + str(cartela[15]) + space + XX + """ |
        | """ + '{:>2}'.format(str(cartela[2])) + space + str(cartela[7]) + space + XX + space + str(cartela[16]) + space + str(cartela[21]) + """ |
        | """ + '{:>2}'.format(str(cartela[3])) + space + str(cartela[8]) + space + str(cartela[12]) + space + str(cartela[17]) + space + XX + """ |
        | """ + '{:>2}'.format(str(cartela[4])) + space + str(cartela[9]) + space + str(cartela[13]) + space + str(cartela[18]) + space + XX + """ |
        +----------------+
    """)
cartaEditavel1 = (f"""
        +----------------+
        | B  I  N  G  O  |
        +================+
        | """ + XX + space + XX + space + XX + space + XX + space + XX + """ |
        | """ + '{:>2}'.format(str(cartela[1])) + space + str(cartela[6]) + space + str(cartela[11]) + space + str(cartela[15]) + space + str(cartela[20]) + """ |
        | """ + '{:>2}'.format(str(cartela[2])) + space + str(cartela[7]) + space + XX + space + str(cartela[16]) + space + str(cartela[21]) + """ |
        | """ + '{:>2}'.format(str(cartela[3])) + space + str(cartela[8]) + space + str(cartela[12]) + space + str(cartela[17]) + space + str(cartela[22]) + """ |
        | """ + '{:>2}'.format(str(cartela[4])) + space + str(cartela[9]) + space + str(cartela[13]) + space + str(cartela[18]) + space + str(cartela[23]) + """ |
        +----------------+
    """)
cartaEditavel2 = (f"""
        +----------------+
        | B  I  N  G  O  |
        +================+
        | """ + '{:>2}'.format(str(cartela[0])) + space + str(cartela[5]) + space + str(cartela[10]) + space + str(cartela[14]) + space + str(cartela[19]) + """ |
        | """ + XX + space + XX + space + XX + space + XX + space + XX + """ |
        | """ + '{:>2}'.format(str(cartela[2])) + space + str(cartela[7]) + space + XX + space + str(cartela[16]) + space + str(cartela[21]) + """ |
        | """ + '{:>2}'.format(str(cartela[3])) + space + str(cartela[8]) + space + str(cartela[12]) + space + str(cartela[17]) + space + str(cartela[22]) + """ |
        | """ + '{:>2}'.format(str(cartela[4])) + space + str(cartela[9]) + space + str(cartela[13]) + space + str(cartela[18]) + space + str(cartela[23]) + """ |
        +----------------+
    """)
cartaEditavel3 = (f"""
        +----------------+
        | B  I  N  G  O  |
        +================+
        | """ + '{:>2}'.format(str(cartela[0])) + space + str(cartela[5]) + space + str(cartela[10]) + space + str(cartela[14]) + space + str(cartela[19]) + """ |
        | """ + '{:>2}'.format(str(cartela[1])) + space + str(cartela[6]) + space + str(cartela[11]) + space + str(cartela[15]) + space + str(cartela[20]) + """ |
        | """ + XX + space + XX + space + XX + space + XX + space + XX + """ |
        | """ + '{:>2}'.format(str(cartela[3])) + space + str(cartela[8]) + space + str(cartela[12]) + space + str(cartela[17]) + space + str(cartela[22]) + """ |
        | """ + '{:>2}'.format(str(cartela[4])) + space + str(cartela[9]) + space + str(cartela[13]) + space + str(cartela[18]) + space + str(cartela[23]) + """ |
        +----------------+
    """)
cartaEditavel4 = (f"""
        +----------------+
        | B  I  N  G  O  |
        +================+
        | """ + '{:>2}'.format(str(cartela[0])) + space + str(cartela[5]) + space + str(cartela[10]) + space + str(cartela[14]) + space + str(cartela[19]) + """ |
        | """ + '{:>2}'.format(str(cartela[1])) + space + str(cartela[6]) + space + str(cartela[11]) + space + str(cartela[15]) + space + str(cartela[20]) + """ |
        | """ + '{:>2}'.format(str(cartela[2])) + space + str(cartela[7]) + space + XX + space + str(cartela[16]) + space + str(cartela[21]) + """ |
        | """ + XX + space + XX + space + XX + space + XX + space + XX + """ |
        | """ + '{:>2}'.format(str(cartela[4])) + space + str(cartela[9]) + space + str(cartela[13]) + space + str(cartela[18]) + space + str(cartela[23]) + """ |
        +----------------+
    """)
cartaEditavel5 = (f"""
        +----------------+
        | B  I  N  G  O  |
        +================+
        | """ + '{:>2}'.format(str(cartela[0])) + space + str(cartela[5]) + space + str(cartela[10]) + space + str(cartela[14]) + space + str(cartela[19]) + """ |
        | """ + '{:>2}'.format(str(cartela[1])) + space + str(cartela[6]) + space + str(cartela[11]) + space + str(cartela[15]) + space + str(cartela[20]) + """ |
        | """ + '{:>2}'.format(str(cartela[2])) + space + str(cartela[7]) + space + XX + space + str(cartela[16]) + space + str(cartela[21]) + """ |
        | """ + '{:>2}'.format(str(cartela[3])) + space + str(cartela[8]) + space + str(cartela[12]) + space + str(cartela[17]) + space + str(cartela[22]) + """ |
        | """ + XX + space + XX + space + XX + space + XX + space + XX + """ |
        +----------------+
    """)
cartaEditaveldp = (f"""
        +----------------+
        | B  I  N  G  O  |
        +================+
        | """ + '{:>2}'.format(str(cartela[0])) + space + str(cartela[5]) + space + str(cartela[10]) + space + str(cartela[14]) + space + XX + """ |
        | """ + '{:>2}'.format(str(cartela[1])) + space + str(cartela[6]) + space + str(cartela[11]) + space + XX + space + str(cartela[20]) + """ |
        | """ + '{:>2}'.format(str(cartela[2])) + space + str(cartela[7]) + space + XX + space + str(cartela[16]) + space + str(cartela[21]) + """ |
        | """ + '{:>2}'.format(str(cartela[3])) + XX + space + str(cartela[12]) + space + str(cartela[17]) + space + str(cartela[22]) + """ |
        | """ + XX + space + str(cartela[9]) + space + str(cartela[13]) + space + str(cartela[18]) + space + str(cartela[23]) + """ |
        +----------------+
    """)
cartaEditavelds = (f"""
        +----------------+
        | B  I  N  G  O  |
        +================+
        | """ + XX + space + str(cartela[5]) + space + str(cartela[10]) + space + str(cartela[14]) + space + str(cartela[19]) + """ |
        | """ + '{:>2}'.format(str(cartela[1])) + space + XX + space + str(cartela[11]) + space + str(cartela[15]) + space + str(cartela[20]) + """ |
        | """ + '{:>2}'.format(str(cartela[2])) + space + str(cartela[7]) + space + XX + space + str(cartela[16]) + space + str(cartela[21]) + """ |
        | """ + '{:>2}'.format(str(cartela[3])) + space + str(cartela[8]) + space + str(cartela[12]) + space + XX + space + str(cartela[22]) + """ |
        | """ + '{:>2}'.format(str(cartela[4])) + space + str(cartela[9]) + space + str(cartela[13]) + space + str(cartela[18]) + space + XX + """ |
        +----------------+
    """)
# Funções
listaSorteados = []
listaSorteados2 = []
numNaoPreenchido = []

# Adiciona o número sorteado na lista Sorteado
def selecionados():
    listaSorteados.append(num)
    listaSorteados2.append(numSorteados)
    Numeros.remove(numSorteados)
    print(f'Lista de números sorteados: ', listaSorteados)
    print(f'Lista de números restantes: ', Numeros)
    print()

for x in range(0, 75):
    listaBase = []
    numSorteados = int(rd.choice(Numeros))

    if numSorteados < 16:
        num = (f'B-%s' % numSorteados)
        print(f'Último Número sorteado: B-%s' % numSorteados)
        selecionados()

    elif numSorteados < 31:
        num = (f'I-%s' % numSorteados)
        print(f'Último Número sorteado: I-%s' % numSorteados)
        selecionados()

    elif numSorteados < 46:
        num = (f'N-%s' % numSorteados)
        print(f'Último Número sorteado: N-%s' % numSorteados)
        selecionados()

    elif numSorteados < 61:
        num = (f'G-%s' % numSorteados)
        print(f'Último Número sorteado: G-%s' % numSorteados)
        selecionados()

    else:
        num = (f'O-%s' % numSorteados)
        print(f'Último Número sorteado: 0-%s' % numSorteados)
        selecionados()

    for J in ColunaB:
        if J in listaSorteados2:
            listaBase.append(J)
    if listaBase == ColunaB:
        print(f'\033[1;31mBINGO\033[m == Parabéns! você preencheu a coluna B na Rodada de Nº: \033[1;31m%s\033[m com os seguintes números: ' %(len(listaSorteados2)), ColunaB)
        print(f'Sua Cartela é: \n', cartaEditavelB)
        break
    else:
        listaBase = []

    for J in ColunaI:
        if J in listaSorteados2:
            listaBase.append(J)
    if listaBase == ColunaI:
        print(f'\033[1;31mBINGO\033[m == Parabéns! você preencheu a coluna I na Rodada de Nº: \033[1;31m%s\033[m com os seguintes números: ' %(len(listaSorteados2)), ColunaI)
        print(f'Sua Cartela é: \n', cartaEditavelI)
        break
    else:
        listaBase = []

    for J in ColunaN:
        if J in listaSorteados2:
            listaBase.append(J)
    if listaBase == ColunaN:
        print(f'\033[1;31mBINGO\033[m == Parabéns! você preencheu a coluna N na Rodada de Nº: \033[1;31m%s\033[m com os seguintes números: ' %(len(listaSorteados2)), ColunaN)
        print(f'Sua Cartela é: \n', cartaEditavelN)
        break
    else:
        listaBase = []

    for J in ColunaG:
        if J in listaSorteados2:
            listaBase.append(J)
    if listaBase == ColunaG:
        print(f'\033[1;31mBINGO\033[m == Parabéns! você preencheu a coluna G na Rodada de Nº: \033[1;31m%s\033[m com os seguintes números: ' %(len(listaSorteados2)), ColunaG)
        print(f'Sua Cartela é: \n', cartaEditavelG)
        break
    else:
        listaBase = []

    for J in ColunaO:
        if J in listaSorteados2:
            listaBase.append(J)
    if listaBase == ColunaO:
        print(f'\033[1;31mBINGO\033[m == Parabéns! você preencheu a coluna O na Rodada de Nº: \033[1;31m%s\033[m com os seguintes números: ' %(len(listaSorteados2)), ColunaO)
        print(f'Sua Cartela é: \n', cartaEditavelO)
        break
    else:
        listaBase = []

    for J in linha1:
        if J in listaSorteados2:
            listaBase.append(J)
    if listaBase == linha1:
        print(f'\033[1;31mBINGO\033[m == Parabéns! você preencheu a linha 1 na Rodada de Nº: \033[1;31m%s\033[m com os seguintes números: ' %(len(listaSorteados2)), linha1)
        print(f'Sua Cartela é: \n', cartaEditavel1)
        break
    else:
        listaBase = []

    for J in linha2:
        if J in listaSorteados2:
            listaBase.append(J)
    if listaBase == linha2:
        print(f'\033[1;31mBINGO\033[m == Parabéns! você preencheu a linha 2 na Rodada de Nº: \033[1;31m%s\033[m com os seguintes números: ' %(len(listaSorteados2)), linha2)
        print(f'Sua Cartela é: \n', cartaEditavel2)
        break
    else:
        listaBase = []

    for J in linha3:
        if J in listaSorteados2:
            listaBase.append(J)
    if listaBase == linha3:
        print(f'\033[1;31mBINGO\033[m == Parabéns! você preencheu a linha 3 na Rodada de Nº: \033[1;31m%s\033[m com os seguintes números: ' %(len(listaSorteados2)), linha3)
        print(f'Sua Cartela é: \n', cartaEditavel3)
        break
    else:
        listaBase = []

    for J in linha4:
        if J in listaSorteados2:
            listaBase.append(J)
    if listaBase == linha4:
        print(f'\033[1;31mBINGO\033[m == Parabéns! você preencheu a linha 4 na Rodada de Nº: \033[1;31m%s\033[m com os seguintes números: ' %(len(listaSorteados2)), linha4)
        print(f'Sua Cartela é: \n', cartaEditavel4)
        break
    else:
        listaBase = []

    for J in linha5:
        if J in listaSorteados2:
            listaBase.append(J)
    if listaBase == linha5:
        print(f'\033[1;31mBINGO\033[m == Parabéns! você preencheu a linha 5 na Rodada de Nº: \033[1;31m%s\033[m com os seguintes números: ' %(len(listaSorteados2)), linha5)
        print(f'Sua Cartela é: \n', cartaEditavel5)
        break
    else:
        listaBase = []

    for J in digPri:
        if J in listaSorteados2:
            listaBase.append(J)
    if listaBase == digPri:
        print(f'\033[1;31mBINGO\033[m == Parabéns! você preencheu a Diagonal Principal na Rodada de Nº: \033[1;31m%s\033[m com os seguintes números: ' %(len(listaSorteados2)), digPri)
        print(f'Sua Cartela é: \n', cartaEditaveldp)
        break
    else:
        listaBase = []

    for J in digSec:
        if J in listaSorteados2:
            listaBase.append(J)
    if listaBase == digSec:
        print(f'\033[1;31mBINGO\033[m == Parabéns! você preencheu a Diagonal Secundária na Rodada de Nº: \033[1;31m%s\033[m com os seguintes números: ' %(len(listaSorteados2)), digSec)
        print(f'Sua Cartela é: \n', cartaEditavelds)
        break
    else:
        listaBase = []
