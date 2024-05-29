import random


def ler_ficha(nome):
    with open(f'{nome}.txt', 'r', encoding='utf-8') as ficha_lista:
        ficha = ficha_lista.read()

        return ficha


def ver_mod(valor):
    try:
        mod = (valor - 10) // 2
        if mod >= 0:
            return f'+{mod}'
        else:
            return f'{mod}'
    except ValueError:
        print('Valor de habilidade inváido')
        return '???'
    except TypeError:
        print('Valor de habilidade inváido')
        return '???'


def dado(lados):
    resultado = random.randint(1, lados)
    return resultado


def ler_token():
    with open('token.txt', 'r', encoding='utf-8') as token:
        return token.read()


def conferir_registro(player):
    with open('registro.txt', 'r', encoding='utf-8') as registros:
        linhas = registros.readlines()


def ver_mod_player(player, habilidade):
    ficha = encontrar_ficha(player)
    for x in ficha:
        linha = x.split(' ')
        if linha[0] == habilidade + ':' :
            mod = ver_mod(linha[1])
            return mod
    print('Habilidade inválida!')



# def ler_ficha(nome):
#     with open(f'{nome}.txt', 'r', encoding='utf-8') as ficha_lista:
#         linhas = ficha_lista.readlines()
#         ficha = ""
#         for line in linhas:
#             ficha = ficha + line




#         return ficha
