from aiohttp import ClientSession
import asyncio
import json

class PingPong:
    def __init__(self, URL: str, Authorization: str):
        url = URL.split("/custom/")[0]
        self.url = url + "/custom/"
        
        self.headers = {
            'Authorization': str(Authorization),
            'Content-Type': 'application/json; charset=utf-8'
        }

    async def Pong(self, id_: str, text: str, NoTopic:bool =False) -> dict:
        data = await self.PingPongRequest(id_, text)
        data = data['response']['replies']
        ReturnData = {
            "text": data[0]['text'],
            "image": None
        }
        i = data[0]
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


    async def PingPongRequest(self, id_: str, text: str) -> dict:
        url = self.url + str(id_)
        data = {
            'request': {
                'query': text
            }
        }
        data = json.dumps(data)
        res = await self.AsyncRequestJson(url, self.headers, data)
        return res

    async def AsyncRequestJson(self, url: str, headers: dict, data: dict) -> dict:
        async with ClientSession() as session:
            async with session.post(url, headers=headers, data=data) as resp:
                return await resp.json()
