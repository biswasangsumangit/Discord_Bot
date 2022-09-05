import discord

"""
client = discord.Client()

@client.event
async def on_ready():
    print('Ready')

client.run('MTAwODc5Njk2MTkyMDUyODQ2NQ.GNKRC4.kxr6FQG3nEZmbSpTiq9Nh0riCcxGqXqPfKcgus')    
"""


class MyClient(discord.Client):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.target_message_id = 1009142288259235880

    async def on_ready(self):
        print('Ready')

    async def on_raw_reaction_add(self, payload):
        """
        Give a roll based on a reaction emoji
        """

        if payload.message_id != self.target_message_id:
            return

        guild = client.get_guild(payload.guild_id)

        if payload.emoji.name == '🥔':
            role = discord.utils.get(guild.roles, name='Potato person')
            await payload.member.add_roles(role)
        elif payload.emoji.name == '🐵':
            role = discord.utils.get(guild.roles, name='Funky monkey')
            await payload.member.add_roles(role)
        elif payload.emoji.name == '😎':
            role = discord.utils.get(guild.roles, name='Cool Guy')
            await payload.member.add_roles(role)

    async def on_raw_reaction_remove(self, payload):
        """
        Remove a roll based on a reaction emoji
        """

        if payload.message_id != self.target_message_id:
            return

        guild = client.get_guild(payload.guild_id)
        member = guild.get_member(payload.user_id)

        if payload.emoji.name == '🥔':
            role = discord.utils.get(guild.roles, name='Potato person')
            await member.remove_roles(role)
        elif payload.emoji.name == '🐵':
            role = discord.utils.get(guild.roles, name='Funky monkey')
            await member.remove_roles(role)
        elif payload.emoji.name == '😎':
            role = discord.utils.get(guild.roles, name='Cool Guy')
            await member.remove_roles(role)

intents = discord.Intents.default()
intents.members = True

client = MyClient(intents=intents)
client.run('MTAwODc5Njk2MTkyMDUyODQ2NQ.GoyNEG.0Mhuh6IM65z9MPJ1eDTylx_JBlzyvqolPJxFI8')
