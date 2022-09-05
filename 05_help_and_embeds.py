import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!')
bot.remove_command('help')

@bot.command()
async def help(ctx):
    embed = discord.Embed(
        title='Bot commands',
        description='Welcome to the help section. Here are all the commands for this game',
        colour=discord.Colour.blue()
    )
    embed.add_field(
        name='!help',
        value='List all of the commands',
        inline=False
    )
    embed.add_field(
        name='!punch',
        value='Punch another player',
        inline=False
    )
    embed.add_field(
        name='!double_punch',
        value='Double punch another player',
        inline=False
    )
    embed.add_field(
        name='!roundhouse_kick',
        value='Roundhouse kicked another player',
        inline=False
    )

    await ctx.send(embed=embed)

@bot.command()
async def punch(ctx, arg):
    """
    !punch another player
    """

    await ctx.send(f'punched {arg}')

@bot.command()
async def double_punch(ctx, arg1, arg2):
    """
    !double_punch another player
    """

    await ctx.send(f' double punched {arg1} and {arg2}')

@bot.command()
async def roundhouse_kick(ctx, *args):
    everyone = ', '.join(args)
    await ctx.send(f'Roundhouse_kicked {everyone}')

bot.run('MTAwODc5Njk2MTkyMDUyODQ2NQ.GoyNEG.0Mhuh6IM65z9MPJ1eDTylx_JBlzyvqolPJxFI8')