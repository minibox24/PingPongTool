from PingPongTool import PingPong
import asyncio

URL = "이곳에 커스텀 API 링크를 넣으세요"
Authorization = "이곳에 인증 토큰을 넣으세요"

Ping = PingPong(URL, Authorization)

async def Console():
    while True:
        data = await Ping.Pong("Console", input(">>> "))
        print(f"핑퐁: {data['text']}")

asyncio.run(Console())
