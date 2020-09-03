from random import randint

valor_quant = []
senha  = []
lista_caract = [
['a', 'b', 'c', 'd', 'f', 'g', 'h', 'i', 'j', 'k', 'l,', 'm', 'n', 'o', 'p', 'q', 
'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'],

['A', 'B', 'C', 'D', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 
'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'S'],

['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20']
]

def escolha():
    try:
        quant = int(input('Digite a quantidade de caracteres: '))
        valor_quant.append(quant)
    except:
        print('Digite um numero valido\n')
        quant = int(input('Digite a quantidade de caracteres: '))
        valor_quant.append(quant)

def gerar_senha():
    for x in range(valor_quant[0]):
        carcter1= lista_caract[randint(0,2)]
        if lista_caract[randint(0,2)] == lista_caract[2]:
            num_carect = lista_caract[2]
            carcter1= num_carect[randint(0,19)]
        else:
            carcter1= lista_caract[randint(0,1)][randint(0,25)]
        senha.append(carcter1)
    for b in range(len(senha)):
        print(senha[b], end="")

escolha()
gerar_senha()