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
    help_descricao = """

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
            if mod > 0:
                await ctx.reply(f'Você tirou {resultado_final}! ({resultado} + {mod})')
            else:
                mod *= -1
                await ctx.reply(f'Você tirou {resultado_final}! ({resultado} - {mod})')
        else:
            await ctx.reply('Você não está registrado!')
    except BadArgument:
        print("Valor inválido")


@rolar.error
async def rtd_error(ctx: commands.Context, error: commands.CommandError):
    if isinstance(error, commands.BadArgument):
        await ctx.reply("Digite um número válido")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.reply("Digite um número válido")
    else:
        await ctx.reply("Ocorreu um erro ao processar o comando.")


bot.run(token)