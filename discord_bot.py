import discord
import logging

class DiscordClient(discord.Client):    
    #discordLogger = logging.getLogger('discord')
    #discordLogger.setLevel(logging.DEBUG)
    async def on_ready(self):
        logging.info("Logged in as {0}".format(self.user))
    async def on_message(message):
        logging.info("{0.author}: {0.content} ".format(message))