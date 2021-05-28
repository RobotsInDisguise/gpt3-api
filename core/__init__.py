import aiohttp
import ujson
from asyncinit import asyncinit

@asyncinit
class HTTPClient:
  
  async def __init__(self, api_key):
    if 'session' not in self:
      async with aiohttp.ClientSession(
          json_serialize=ujson.dumps) as session:
          self.session = session

  async def get(self, api_path):
    self.headers={"Authorization": f"Bearer {{self.api_key}}"}
    async with aiohttp.ClientSession(self.headers=headers) as session:
        async with session.get(f"https://api.openai.com/v1/{{api_path}}") as resp:
          return resp
          

  

@asyncinit
class Files(HTTPClient):

  async def __init__(self):
    await super(self)
  
  async def list(self):
    await self.session.get('https://api.openai.com/v1/files'):

