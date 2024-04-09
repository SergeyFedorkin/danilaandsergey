import discord
import logging

TOKEN = "MTIyNzMzMDQ4OTg4NzQ5MDEyMA.GvieBU.5BuKcimgSVmndCCKU6BpTO0zwFQtJQPGqVsRnU"


class BombClickX(discord.Client):
    async def on_ready(self):
        print(f'{self.user} has connected to Discord!')
        for guild in self.guilds:
            print(
                f'{self.user} подключились к чату:\n'
                f'{guild.name}(id: {guild.id})')

    async def on_member_join(self, member):
        await member.create_dm()
        await member.dm_channel.send(
            f'Привет, {member.name}!'
        )

    async def on_message(self, message):
        if message.author == self.user:
            return
        if "тест" in message.content.lower():
            await message.channel.send("Добро пожаловать в BombClickX!")


intents = discord.Intents.default()
intents.members = True
intents.message_content = True
client = BombClickX(intents=intents)
client.run(TOKEN)


# Logging
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)