
import requests
#from bs4 import BeautifulSoup

from eclass.links import MAIN_PAGE, LOGIN_PAGE

class Fetcher():
	def __init__(self, username, password, cookie_storage):
		self.username = username
		self.password = password
		self.cookie_storage = cookie_storage
		self.session = requests.Session()
		self._read_cookies()

	# async def _init(self):
	# 	response = self.session.get(MAIN_PAGE, allow_redirects=False)
	# 	if response.status_code==303:
	# 		await self._login()

	def _read_cookies(self, ):
		self.cookie_storage.restore(self.username, self.session)

	def _write_cookies(self, ):
		self.cookie_storage.store(self.username, self.session)

	async def get(self, *args, **kwargs):

		response = self.session.get(*args, allow_redirects=False, **kwargs)
		if response.status_code==303:
			await self._login()
			response = self.session.get(*args, **kwargs)

		# retry = 1
		# while response.status_code==303:
		# 	await self._login()
		# 	response = self.session.get(*args, **kwargs)
		# 	retry +=1

		return response.text

	async def post(self, *args, **kwargs):
		return self.session.post(*args, **kwargs)

	async def _login(self):
		response = await self.post(
			LOGIN_PAGE,
			data={"username":self.username, "password":self.password}
		)
		self._write_cookies()

# async def create_fetcher(*args, **kwargs):
# 	fetcher = Fetcher(*args, **kwargs)
# 	await fetcher._init()
# 	return fetcher