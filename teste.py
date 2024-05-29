import random

# Retorna a ficha completa de um personagem como uma string
def ler_ficha(nome): # terminado
    with open(f'{nome}.txt', 'r', encoding='utf-8') as ficha_lista:
        ficha = ficha_lista.read()

        return ficha

# Retorna o modificador de um valor de habilidade
def ver_mod(valor): # terminado
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

# Rola um dado com o número de lados
def dado(lados): # terminado
    resultado = random.randint(1, lados)
    return resultado

# Lê o token do bot
def ler_token():# terminado
    with open('token.txt', 'r', encoding='utf-8') as token:
        return token.read()

# Confere se um jogador está registrado ou não pelo id 
# Index[0] tem o nome da ficha, e index[1] tem o valor True ou False pra registrado ou não
def conferir_registro(player): # terminado
    with open('registrado.txt', 'r', encoding='utf-8') as registros:
        linhas = registros.readlines()
        for x in linhas:
            linha = x.split(' ')
            if linha[0] == player:
                return linha[1], True
        return 'Jogador não registrado', False

# Retorna o modificador de uma habilidade específica de um player específico pelo id
def ver_mod_player(player, habilidade): # terminado
    ficha = encontrar_ficha(player)
    for x in ficha:
        linha = x.split(' ')
        if linha[0] == habilidade + ':' :
            mod = ver_mod(linha[1])
            return mod
    print('Habilidade inválida!')

# Retorna a ficha completa de um personagem como uma lista
def encontrar_ficha(player): # terminado
    arquivo, _ = conferir_registro(player)
    with open(f'{arquivo}.txt', 'r', encoding='utf-8') as ficha_lista:
        ficha = ficha_lista.readlines()
    return ficha
