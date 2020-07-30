# PingPongTool
쉬운 핑퐁빌더 사용을 위한 모듈

## 설명
이 모듈은 `discord.py` 에서도 사용할 수 있게 비동기로 제작되었습니다.

꼭 `discord.py` 이 아니라도 다양한 곳에서 사용할 수 있게 제작되었습니다.

## 제작자
> Minibox

**연락**

이메일: `minibox724@gmail.com`

디스코드: `Minibox#8888`

## 사용 설명
`pip install PingPongTool`
```py
from PingPongTool import PingPong  # 핑퐁툴 모듈 임포트
import asyncio  # 비동기 사용을 위한 asyncio 모듈

URL = "이곳에 커스텀 API 링크를 넣으세요"  # 핑퐁 커스텀 API 사이트에서 링크
Authorization = "이곳에 인증 토큰을 넣으세요"  # 핑퐁 커스텀 API 사이트에서 인증 토큰

Ping = PingPong(URL, Authorization)  # 핑퐁 클래스 선언

async def Example():  # 비동기 사용을 위한 함수
    text = input(">>> ")  # 입력 받기
    data = await Ping.Pong("Example", text)  # 자연스러운 대화를 위한 세션 아이디와
                                             # 전송할 텍스트
    print(data) # {"text": "안녕안녕입니다🖐", "image": None}

asyncio.run(Example())  # 비동기로 함수 실행
```


## 라이선스
만약 이 모듈을 사용한다면 크레딧, 또는 임베드 푸터 같은곳에 이 모듈을 사용했다는 것을 정확히 알리세요.

---
---
버그 제보 받습니다.

깃허브 이슈 or 디스코드 ( `Minibox#8888` )