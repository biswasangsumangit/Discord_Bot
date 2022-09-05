import discord

client = discord.Client()

@client.event
async def on_ready():
    print('Online')


@client.event
async def on_message(message):

    if message.author == client.user:
        return

    if message.content == 'cool':
        await message.add_reaction('\U0001F60E')

@client.event
async def on_message_edit(before, after):
    await before.channel.send(
        f'{before.author} edit a message.\n'
        f'Before: {Before.content}\n'
        f'After: {After.content}'
    )

@client.event
async def on_reaction_add(reaction, user):
    await reaction.message.channel.send(f'{user} reacted with {reaction.emoji}')


client.run('MTAwODc5Njk2MTkyMDUyODQ2NQ.GNKRC4.kxr6FQG3nEZmbSpTiq9Nh0riCcxGqXqPfKcgus')