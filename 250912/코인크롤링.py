import requests
import json
from datetime import datetime

response = requests.get('https://crix-api-cdn.upbit.com/v1/crix/candles/minutes/60?code=CRIX.UPBIT.KRW-BTC&count=20&to=2025-09-12T04%3A03%3A21Z&timestamp=1757649833362')

coinData = response.content
coinData = json.loads(coinData)

print(coinData)
print(type(coinData))
print(len(coinData))

for data in coinData:
  print(data['highPrice'])
  date_str = datetime.fromtimestamp(data['timestamp']/1000).strftime('%Y-%m-%d %H:%M:%S')
  print(date_str)