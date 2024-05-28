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

# def ler_ficha(nome):
#     with open(f'{nome}.txt', 'r', encoding='utf-8') as ficha_lista:
#         linhas = ficha_lista.readlines()
#         ficha = ""
#         for line in linhas:
#             ficha = ficha + line




#         return ficha
