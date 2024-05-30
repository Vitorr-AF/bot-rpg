from teste import *




player = 1234556789
habilidade = "for"

try:
    registro = conferir_registro(player)
    if registro[1] == True:
        resultado = dado(20)
        mod = ver_mod_player(player, habilidade)
        resultado_final = resultado + mod
        if mod > 0:
            print(f'Você tirou {resultado_final}! ({resultado} + {mod})')
        else:
            mod *= -1
            print(f'Você tirou {resultado_final}! ({resultado} - {mod})')
    else:
        print("Você não está registrado!")
except ValueError:
    print("Valor inválido")