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

x = ler_ficha('registro')
print(x)