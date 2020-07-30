from aiohttp import ClientSession
import asyncio
import json

class PingPong:
    def __init__(self, URL: str, Authorization: str):
        url = URL.split("/custom/")[0]
        self.url = url + "/custom/"
        self.Authorization = Authorization

    async def Pong(self, id_: str, text: str, NoTopic=False):
        data = await self.PingPongRequest(id_, text)
        data = data['response']['replies']
        ReturnData = {
            "text": data[0]['text'],
            "image": None
        }
        for i in data:
            try:
                if i['from']['name'] == "imageSet":
                    ReturnData['image'] = i['image']['url']
                if i['from']['name'] == "topic":
                    if not NoTopic:
                        ReturnData['image'] = None
                        ReturnData['text'] = i['text']
            except KeyError:
                pass
        return ReturnData


    async def PingPongRequest(self, id_, text):
        url = self.url + str(id_)
        headers = {
            'Authorization': self.Authorization,
            'Content-Type': 'application/json; charset=utf-8'
        }
        data = {
            'request': {
                'query': text
            }
        }
        data = json.dumps(data)
        res = await self.AsyncRequestJson(url, headers, data)
        return res

    async def AsyncRequestJson(self, url, headers, data):
        async with ClientSession() as session:
            async with session.post(url, headers=headers, data=data) as resp:
                return await resp.json()
        return res
