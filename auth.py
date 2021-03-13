import datetime

class AuthSession():
	def __init__(self, discord_username: str, discord_guild: str) -> None:
		self.discord_username = discord_username
		self.discord_guild = discord_guild

	discord_username: str
	discord_guild: str
	shack_name: str
	auth_token: str
	expire_time: datetime

class AuthService:
	sessions = dict()

	def __init__(self) -> None:
		pass

	def start_session(self, discord_username: str, discord_guild: str):
		self.sessions[discord_username] = AuthSession(discord_username, discord_guild)
	
	def get_token(self, discord_username: str, shack_name: str) -> str:
		if (discord_username in self.sessions == False):
			print('no session')
			return
		
		session : AuthSession = self.sessions.get(discord_username)
		session.shack_name = shack_name
		return 'TOKEN'
