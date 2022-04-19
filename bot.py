from discord import Client
import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

class MyBot(commands.Bot):
    def __init__(self):

        intents = discord.Intents.default()
        intents.presences = True
        intents.members = True
        super().__init__(command_prefix="!", intents=intents)

   # async def on_ready(self):
   #a     self.log.infolog(f"{self.user} has connected to Discord!")

    # Créer un événement
    async def on_ready(self):
        print("Le bot est prêt !")

    async def on_message(ctx, message):
        if message.content == "Meilleure Légende d'Apex?":
            await message.channel.send("BLOODHOUND!!!")
        elif message.content == "Meilleure map d'Apex?":
            await message.channel.send("Certainement pas Kings Canyon mdr")
    
    async def on_member_join(self, member):
            guild = member.guild
            print("Quelqu'un a rejoint")
            if guild.system_channel is not None:
                to_send = 'bienvenue {0.mention} sur le serveur {1.name}'.format(member, guild)
                await guild.system_channel.send(to_send)

load_dotenv(dotenv_path="config.txt")
bot = MyBot()
bot.run(os.getenv("TOKEN"))
