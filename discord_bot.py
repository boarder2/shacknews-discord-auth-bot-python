import discord
import logging

from discord import Message
from discord.enums import ChannelType
from auth import AuthService, AuthSessionState

class DiscordBot(discord.Client):
	def __init__(self, auth_svc: AuthService):
		self.auth_svc = auth_svc
		super().__init__()
	#discordLogger = logging.getLogger('discord')
	#discordLogger.setLevel(logging.DEBUG)
	async def on_ready(self):
		logging.info("Logged in as {0}".format(self.user))
	async def on_message(self, message: Message):
		if message.author == self.user: return
		logging.info(message)

		if message.channel.type == ChannelType.text:
			if message.content == '!auth':
				self.auth_svc.start_session(message.author, message.guild.name)
				await message.author.send('What is your shacknews username?')
				logging.info(f'Starting auth session for {message.author}')

		elif message.channel.type == ChannelType.private:
			if self.auth_svc.get_session_state(message.author) == AuthSessionState.NEED_USERNAME:
				token = self.auth_svc.set_shack_username_get_token(message.author, message.content)
				if token:
					await message.author.send('Check your shackmessages and reply with the token.')
					logging.info(f'Generated token {token} for {message.author} with shackname {message.content}')

			elif self.auth_svc.get_session_state(message.author) == AuthSessionState.NEED_TOKEN:
				if self.auth_svc.match_token(message.author, message.content):
					await message.author.send('Successfully authenticated!')
					self.auth_svc.remove_session(message.author)
					logging.info(f'Successfully authenticated {message.author}')
				else:
					await message.author.send('Token didn\'t match please try again.')
			else:
				await message.author.send('Not sure what to do here. You don\'t have an active authentication session. Type !auth in the server you want to authenticate against.')