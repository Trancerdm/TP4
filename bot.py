from discord import Client
import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
from argparse import ArgumentParser

class MyBot(commands.Bot):
    def __init__(self):

        intents = discord.Intents.default()
        intents.presences = True
        intents.members = True
        super().__init__(command_prefix="!", intents=intents)

    # Créer un événement
    async def on_ready(self):
        print("Le bot est prêt !")

    async def on_message(ctx, message):
        if message.content == "!légende":
            await message.channel.send("BLOODHOUND!!!")

        elif message.content == "!map":
            await message.channel.send("Certainement pas Kings Canyon mdr")

        elif message.content == "!server":
            await message.channel.send("Ce server à été crée par Polarisé pendant le confinement afin de chill/travailler/jouer entre potes.")

        if message.content.startswith('!help'):
            embed = discord.Embed(colour = discord.Colour.red(), title="Liste des commandes disponibles :D")
            embed.add_field(name="!légende",value="Vous indique quelle est la meilleure légende d'Apex",inline =False)
            embed.add_field(name="!map",value="La map détestée de tous",inline =False)
            embed.add_field(name="!server",value="Petite description du server",inline =False)
            await message.channel.send(embed=embed)

        # elif message.content == "!help":
        #     await message.channel.send("Meilleure Légende d'Apex? | Meilleure map d'Apex? | !help | !server")
    
    async def on_member_join(self, member):
            guild = member.guild
            print("Quelqu'un a rejoint")
            if guild.system_channel is not None:
                to_send = 'bienvenue {0.mention} sur le serveur {1.name}'.format(member, guild)
                await guild.system_channel.send(to_send)

    async def embed():
        embed = discord.Embed(
            title = 'Title',
            description = 'description',
            colour = discord.Colour.blue()
        )

        await bot.say(embed=embed)

load_dotenv(dotenv_path="config.txt")
bot = MyBot()
bot.run(os.getenv("TOKEN"))

