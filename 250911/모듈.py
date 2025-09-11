"""
모듈 ( module )
모든 python 파일 ( 함수, 변수, 클래스 등등... 을 
다른 python파일에 inport해서 사용이 가능함)
"""

# 날짜 시간 관련된 모듈 
from datetime import datetime, date, time
print( datetime.now() )
print( datetime.today() )
print( datetime.today().year )
print( datetime.today().month )
print( datetime.today().day )
print( datetime.today().hour )
print( datetime.today().minute )
print( datetime.today().second )

# date
print( date.today() )
a = date(2025, 1, 16)
print(a)

now = datetime.now()

print(now)
print( type(now) )
now2 = "2025-9-11 13:24:25"

format = now.strftime("%Y년 %m월 %d일 %A %H시%M분")
print(format)

# 난수생성 모듈
import random

print( random.randint(0, 10))

