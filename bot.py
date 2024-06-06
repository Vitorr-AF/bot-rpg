from teste import *
import discord
from discord.ext import commands
import random
from discord.ext.commands.errors import BadArgument


# Permissões do bot (permissões padrões além de ver mensagens e usuários)
permissoes = discord.Intents.default()
permissoes.message_content = True
permissoes.members = True


token = ler_token()

bot = commands.Bot(command_prefix=".", intents=permissoes)


#.help (mostra a lista de comandos)
@bot.command()
async def ajuda(ctx: commands.Context):
    help_descricao = """.ajuda: mostra todos os comandos
.srolar (numero de lados): rola um dado de sorte / sem modificador
.rolar (habilidade): rola o dado de uma habilidade específica
.registrar: te registra na lista de jogadores e cria uma ficha padrão pra você
.minha_ficha: mostra a sua ficha completa
    """
    help_m = discord.Embed(title="Lista de comandos atuais:", description=help_descricao, color=discord.Color.blue())

    await ctx.reply(embed=help_m)


@bot.command()
async def srolar(ctx: commands.Context, lados: int):
    try:
        resultado = dado(lados)
        await ctx.reply(f'Você tirou {resultado}!')
    except BadArgument:
        print("Valor inválido")


@bot.command()
async def rolar(ctx: commands.Context, habilidade):
    try:
        player = ctx.author.id
        registro = conferir_registro(player)
        if registro[1] == True:
            resultado = dado(20)
            mod = ver_mod_player(player, habilidade)
            resultado_final = resultado + mod
            if mod >= 0:
                await ctx.reply(f'Você tirou {resultado_final}! ({resultado} + {mod})')
            else:
                mod *= -1
                await ctx.reply(f'Você tirou {resultado_final}! ({resultado} - {mod})')
        else:
            await ctx.reply('Você não está registrado!')
    except BadArgument:
        print("Valor inválido")


@bot.command()
async def registrar(ctx: commands.Context):
    player = ctx.author.id
    _, registrado = conferir_registro(player)
    if registrado == True:
        await ctx.reply("Você ja esta registrado!")
    else:
        registrar_player(player)
        await ctx.reply("Registrado com sucesso!")

@rolar.error
async def rtd_error(ctx: commands.Context, error: commands.CommandError):
    if isinstance(error, commands.BadArgument):
        await ctx.reply("Digite um número válido")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.reply("Digite um número válido")
    else:
        await ctx.reply("Ocorreu um erro ao processar o comando.")

@bot.command()
async def minha_ficha(ctx: commands.Context):
    player = ctx.author.id
    ficha_nome, registrado = conferir_registro(player)
    if registrado == True:
        ficha = ler_ficha(ficha_nome)
        await ctx.reply(f"{ficha}")
    else:
        await ctx.reply("Você não está registrado")

bot.run(token)