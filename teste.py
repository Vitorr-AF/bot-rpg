import random

# Retorna a ficha completa de um personagem como uma string
def ler_ficha(nome): # terminado
    with open(f'{nome}.txt', 'r', encoding='utf-8') as ficha_lista:
        ficha = ficha_lista.read()

        return ficha

# Retorna o modificador de um valor de habilidade
def ver_mod(valor): # terminado
    print(valor)
    valor = int(valor)
    try:
        mod = (valor - 10) // 2
        return mod
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
            if linha[0] == str(player):
                return linha[1].strip(), True
        return 'Jogador não registrado', False

# Retorna o modificador de uma habilidade específica de um player específico pelo id
def ver_mod_player(player, habilidade): # terminado
    ficha = encontrar_ficha(player)
    for x in ficha:
        linha = x.split(' ')
        if linha[0].lower() == habilidade.lower() + ':' :
            mod = ver_mod(linha[1].strip())
            return int(mod)
    print('Habilidade inválida!')

# Retorna a ficha completa de um personagem como uma lista
def encontrar_ficha(player): # terminado
    arquivo, _ = conferir_registro(player)
    with open(f'{arquivo}.txt', 'r', encoding='utf-8') as ficha_lista:
        ficha = ficha_lista.readlines()
    return ficha

# Registra a ficha de um player pelo id
def registrar_player(player):
    with open('registrado.txt', 'r', encoding='utf-8') as registros:
        linhas = registros.readlines()
    num_player = len(linhas) + 1
    with open('registrado.txt', 'a', encoding='utf-8') as registros:
        registros.write(f'\n{player} player{num_player}')
    with open(f'player{num_player}.txt', 'w', encoding='utf-8') as ficha:
        ficha.write(f"Nome: player{num_player}\nFor: 10\nDes: 10\nCon: 10\nInt: 10\nSab: 10\nCar: 10")
    atualizar_gitignore(f'player{num_player}.txt')


def registrar_habilidade(player, habilidade, valor):
    ficha = encontrar_ficha(player)
    for x in range(len(ficha)):
        linha = ficha[x].split(' ')
        if linha[0].lower() == habilidade.lower() + ':' and x+1 < len(ficha):
            ficha[x] = habilidade.upper() + ': ' + f'{valor}\n'
            reescrever_ficha(player, ficha)
            return
        elif linha[0].lower() == habilidade.lower() + ':' and x+1 == len(ficha):
            ficha[x] = habilidade.upper() + ': ' + f'{valor}'
            reescrever_ficha(player, ficha)
            return
    print("Habilidade inválida!")


def reescrever_ficha(player, ficha):
    arquivo, _ = conferir_registro(player)
    ficha_nova = ""
    for linha in ficha:
        ficha_nova = ficha_nova + linha
    with open(f'{arquivo}.txt', 'w', encoding='utf-8') as ficha_velha:
        ficha_velha.write(ficha_nova)


def atualizar_gitignore(player_filename):
    gitignore_path = '.gitignore'
    
    try:
        with open(gitignore_path, 'r', encoding='utf-8') as gitignore_file:
            linhas = gitignore_file.readlines()
    except FileNotFoundError:
        linhas = []

    if player_filename + '\n' not in linhas:
        with open(gitignore_path, 'a', encoding='utf-8') as gitignore_file:
            gitignore_file.write('\n' + player_filename)


def checar_mestre(cargos):
    mestre = any(role.name == "DM" for role in cargos)
    return mestre