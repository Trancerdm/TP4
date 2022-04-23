from discord import Client
import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
import json
from logging import Logger
from argparse import ArgumentParser , Namespace

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
            
            embed = discord.Embed(colour = discord.Colour.purple(), title="Liste des commandes disponibles :D")
            embed.add_field(name="!légende",value="Vous indique quelle est la meilleure légende d'Apex",inline =False)
            embed.add_field(name="!map",value="La map détestée de tous",inline =False)
            embed.add_field(name="!server",value="Petite description du server",inline =False)
            await message.channel.send(embed=embed)

    async def on_member_join(self, member):
            guild = member.guild
            print("Quelqu'un a rejoint")
            if guild.system_channel is not None:
                to_send = 'bienvenue {0.mention} sur le serveur {1.name}'.format(member, guild)
                await guild.system_channel.send(to_send)


    def parse_args() -> Namespace:
        parser = ArgumentParser()
        parser.add_argument(
            "-c", "--config", help="Config file", required=True, dest="config"
        )
        return parser.parse_args()

    def get_config(config_file: str)-> dict:
        with open(config_file, "r") as f:
            config = json.load(f)
        return config

    def main(config: dict) -> bool:
        token = config["token"]
        bot = MyBot()
        bot.run(token)
        pass

    if __name__ == "__main__":
        args = parse_args()
        config = get_config(args.config)
        main(config)
        pass


# load_dotenv(dotenv_path="config.txt")
# bot = MyBot()
# bot.run(os.getenv("TOKEN"))

