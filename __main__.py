import discord_bot
import logging
import settings

logging.basicConfig(level=logging.INFO)

s = settings.Settings()

discord_bot.DiscordClient().run(s.apikey)