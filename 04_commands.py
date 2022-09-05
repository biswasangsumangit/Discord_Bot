from discord.ext import commands

bot = commands.Bot(command_prefix='!')

@bot.command()
async def punch(ctx, arg):
    """
    !punch Papai
    """

    await ctx.send(f'punched {arg}')

@bot.command()
async def double_punch(ctx, arg1, arg2):
    """
    !double_punch Papai Babai
    """

    await ctx.send(f' double punched {arg1} and {arg2}')

@bot.command()
async def roundhouse_kick(ctx, *args):
    """
    !roundhouse_kick Papai Babai Tatai Guddu
    """

    everyone = ', '.join(args)
    await ctx.send(f'Roundhouse_kicked {everyone}')

@bot.command()
async def info(ctx):
    """
    ctx - context (information about how the command was executed)

    !info
    """

    await ctx.send(ctx.guild)
    await ctx.send(ctx.author)
    await ctx.send(ctx.message.id)

bot.run('MTAwODc5Njk2MTkyMDUyODQ2NQ.GoyNEG.0Mhuh6IM65z9MPJ1eDTylx_JBlzyvqolPJxFI8')