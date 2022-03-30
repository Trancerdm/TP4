from discord import Client
import discord

class MyBot(Client):
    def __init__(self):
        super().__init__()
        self.run("OTU4NjkyMzEwOTM2MzUwNzQw.YkRByg.VHACXURL6RbI5gkU4PtLb6fOyjw")

   # async def on_ready(self):
   #a     self.log.infolog(f"{self.user} has connected to Discord!")

    # Créer un événement
    async def on_ready(self):
        print("Le bot est prêt !")

    async def on_message(ctx, message):
        if message.content == "Best Apex legend?":
            await message.channel.send("BLOODHOUND!!!")

    async def on_member_join(member):
        print(f"L'utilisateur {member.display_name} a rejoint le serveur !")

bot = MyBot()

default_intents = discord.Intents.default()
default_intents.members = True
client = discord.Client(intents=default_intents)