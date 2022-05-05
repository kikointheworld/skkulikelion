import requests
import json # 파이썬 기본 모듈 javascript object notation

# 응용 프로그램 프로그래밍 인터페이스 
# interface? 
# client <-> API <-> server
# 클라이언트와 서버가 데이터를 원활하게 주고받게 하기 위해서 API 를 이용한다.
# 궁금한 지역만 입력하면 바로 가져왔으면 좋겠다~~~
# 사용자가 만들 프로그램과 기존의 프로그램이랑 연결해준다고 하면.. 된다..
# 공짜 API? OpenAPI

city = "Seoul"
apikey = f"b4c11f36efce5b888330d041eee671b3"
lang = "kr"
api = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={apikey}&lang={lang}&units=metric" # f-string 바꾸고싶은 변수는 중괄호이용
# API 를 누가 사용? 방명록을 쓴 사람만 사용할 수 있게 하고 싶다!
# 본인이 누구인지 나타낼 때 API 키를 이용한다!
# 특정 사용자를 알아 볼 수 있는 문자열을 API key 라고 한다.

result = requests.get(api) #이건 str타입이라 제이슨 타입으로 변경해주자
# print(type(result.text))

data = json.loads(result.text)

# 지역 : name
print(data["name"],"의 날씨입니다.")
# 자세한 날씨 : weather - description
print("날씨는 ",data["weather"][0]["description"],"입니다.")
# 현재 온도 : main - temp
print("현재 온도는 ",data["main"]["temp"],"입니다.")
# 체감 온도 : main - feels_like
print("하지만 체감 온도는 ",data["main"]["feels_like"],"입니다.")
# 최저 기온 : main - temp_min
print("최저 기온은 ",data["main"]["temp_min"],"입니다.")
# 최고 기온 : main - temp_max
print("최고 기온은 ",data["main"]["temp_max"],"입니다.")
# 습도 : main - humidity
print("습도는 ",data["main"]["humidity"],"입니다.")
# 기압 : main - pressure
print("기압은 ",data["main"]["pressure"],"입니다.")
# 풍향 : wind - deg
print("풍향은 ",data["wind"]["deg"],"입니다.")
# 풍속 : wind - speed
print("풍속은 ",data["wind"]["speed"],"입니다.")