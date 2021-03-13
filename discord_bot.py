import discord
import logging

from discord import Message
from auth import AuthService

class DiscordBot(discord.Client):
	def __init__(self, auth_svc: AuthService):
		self.auth_svc = auth_svc
		super().__init__()
	#discordLogger = logging.getLogger('discord')
	#discordLogger.setLevel(logging.DEBUG)
	async def on_ready(self):
		logging.info("Logged in as {0}".format(self.user))
	async def on_message(self, message: Message):
		self.auth_svc.start_session(message.author, message.guild.name)
		logging.info("{0.author}:{0.author.guild.name} - {0.content} ".format(message))