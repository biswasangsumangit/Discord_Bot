import discord

client = discord.Client()

@client.event
async def on_ready():
    print('Bot is now online and ready to roll')


@client.event
async def on_message(message):

    if message.author == client.user:
        return

    if message.content == 'hello':
        await message.channel.send('Welcome to durgapur')


client.run('MTAwODc5Njk2MTkyMDUyODQ2NQ.GNKRC4.kxr6FQG3nEZmbSpTiq9Nh0riCcxGqXqPfKcgus')