from discord import Client
import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
import logging
from datetime import datetime

logging.basicConfig(filename='journalisation.log', filemode='w', encoding='utf-8', format='%(levelname)s: %(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.INFO)
logging.debug("Ceci est un message test de debug")
logging.info("Ceci est un message test d'info")
logging.warning("Ceci est un message test de warning")
logging.error("Ceci est un message test d'erreur")
logging.info("-------- Started ---------")


class MyBot(commands.Bot):
    def __init__(self):

        intents = discord.Intents.default()
        intents.presences = True
        intents.members = True
        super().__init__(command_prefix="!", intents=intents)

    # Créer un événement
    async def on_ready(self):
        print("Le bot est prêt !")
        time = str(datetime.now())
        f = open("journalisation.log", "a")
        f.write(time + " The bot " + self.user.name + " is logged to the server !\n")
        f.close()

    async def on_message(ctx, message):
        if message.content == "!légende":
            await message.channel.send("BLOODHOUND!!!")
            time = str(datetime.now())
            f = open("journalisation.log", "a")
            f.write(time + " La commande !légende à été utilisée \n")
            f.close()

        elif message.content == "!map":
            await message.channel.send("Certainement pas Kings Canyon mdr")
            time = str(datetime.now())
            f = open("journalisation.log", "a")
            f.write(time + " La commande !map à été utilisée\n")
            f.close()

        elif message.content == "!server":
            await message.channel.send("Ce server à été crée par Polarisé pendant le confinement afin de chill/travailler/jouer entre potes.")
            time = str(datetime.now())
            f = open("journalisation.log", "a")
            f.write(time + " La commande !server à été utilisée \n")
            f.close()

        if message.content.startswith('!help'):
            
            embed = discord.Embed(colour = discord.Colour.purple(), title="Liste des commandes disponibles :D")
            embed.add_field(name="!légende",value="Vous indique quelle est la meilleure légende d'Apex",inline =False)
            embed.add_field(name="!map",value="La map détestée de tous",inline =False)
            embed.add_field(name="!server",value="Petite description du server",inline =False)
            await message.channel.send(embed=embed)
            time = str(datetime.now())
            f = open("journalisation.log", "a")
            f.write(time + " La commande !help à été utilisée ! \n")
            f.close()

    async def on_member_join(self, member):
            guild = member.guild
            print("Quelqu'un a rejoint")
            if guild.system_channel is not None:
                to_send = 'bienvenue {0.mention} sur le serveur {1.name}'.format(member, guild)
                await guild.system_channel.send(to_send)
                time = str(datetime.now())
                f = open("journalisation.log", "a")
                f.write(time + " Un nouveau membre à join les Loulou ! \n")
                f.close()


load_dotenv(dotenv_path="config.txt")
bot = MyBot()
bot.run(os.getenv("TOKEN"))

