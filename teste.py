import random


def ler_ficha(nome): # terminado
    """
    Retorna a ficha completa de um personagem como uma string
    """
    with open(f'{nome}.txt', 'r', encoding='utf-8') as ficha_lista:
        ficha = ficha_lista.read()

        return ficha


def ver_mod(valor): # terminado
    """
    Retorna o modificador de um valor de habilidade
    """
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


def dado(lados=20): # terminado
    """
    Rola um dado com o número de lados fornecido (padrão 20)
    """
    resultado = random.randint(1, lados)
    return resultado


def ler_token():# terminado
    """
    Lê o token do bot
    """
    with open('token.txt', 'r', encoding='utf-8') as token:
        return token.read()


def conferir_registro(player): # terminado
    """
    Confere se um jogador está registrado ou não pelo seu id do discord, retorna o nome da ficha e o valor True ou false pra registrado ou não
    """
    with open('registrado.txt', 'r', encoding='utf-8') as registros:
        linhas = registros.readlines()
        for x in linhas:
            linha = x.split(' ')
            if linha[0] == str(player):
                return linha[1].strip(), True
        return 'Jogador não registrado', False


def ver_mod_player(player, habilidade): # terminado
    """
    Retorna o modificador de uma habilidade específica de um player pelo id do discord
    """
    ficha = encontrar_ficha(player)
    for x in ficha:
        linha = x.split(' ')
        if linha[0].lower() == habilidade.lower() + ':' :
            mod = ver_mod(linha[1].strip())
            return int(mod)
    print('Habilidade inválida!')


def encontrar_ficha(player): # terminado
    """
    Retorna a ficha completa de um personagem como uma lista
    """
    arquivo, _ = conferir_registro(player)
    with open(f'{arquivo}.txt', 'r', encoding='utf-8') as ficha_lista:
        ficha = ficha_lista.readlines()
    return ficha


def registrar_player(player):
    """
    Registra a ficha de um player pelo id do discord
    """
    with open('registrado.txt', 'r', encoding='utf-8') as registros:
        linhas = registros.readlines()
    num_player = len(linhas) + 1
    with open('registrado.txt', 'a', encoding='utf-8') as registros:
        registros.write(f'\n{player} player{num_player}')
    with open(f'player{num_player}.txt', 'w', encoding='utf-8') as ficha:
        ficha.write(f"Nome: player{num_player}\nFor: 10\nDes: 10\nCon: 10\nInt: 10\nSab: 10\nCar: 10")
    atualizar_gitignore(f'player{num_player}.txt')


def registrar_habilidade(player, habilidade, valor):
    """
    Muda o valor de uma habilidade
    """
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
    lastLine = len(ficha) - 1
    ficha[lastLine] = ficha[lastLine] + '\n'
    ficha.append(habilidade.upper() + ': ' + f'{valor}')
    reescrever_ficha(player, ficha)
    return


def reescrever_ficha(player, ficha):
    """
    Pega uma lista com os novos valores da ficha e substitui ela
    """
    arquivo, _ = conferir_registro(player)
    ficha_nova = ""
    for linha in ficha:
        ficha_nova = ficha_nova + linha
    with open(f'{arquivo}.txt', 'w', encoding='utf-8') as ficha_velha:
        ficha_velha.write(ficha_nova)


def atualizar_gitignore(player_filename):
    """
    Atualiza o gitignore pra ignorar um arquivo
    """
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
    """
    Confere se alguem tem o cargo de DM
    """
    mestre = any(role.name == "DM" for role in cargos)
    return mestre


def ver_valor_atributo(player, atributo):
    ficha = encontrar_ficha(player)
    for x in ficha:
        linha = x.split(' ')
        if linha[0].lower() == atributo.lower() + ':' :
            valor = linha[1].strip()
            return int(valor)
    print('Habilidade inválida!')
