"""
함수 기본 문법
def 함수이름(매개변수) :
  코드 
  return 리턴값
"""

def print_msg():
  print("hello")
  print("python")

print_msg()

def add(x=100, y=200):
  print(f"x : {x}, y : {y}")
  return x + y

print(add(10, 20)) # 매개변수 
print( add(y=10, x=20)) # 매개변수 지정
add() # 매개변수가 지정되어있는 경우
add(y=10)

def add2(*args): # * 는 개수상관없이 다 받아줌 
  print(args)
  print(type(args)) # 튜플 형태로 받아주는 매개변수

add2(1,2,3,4,5,6,7)
# 키워드 매개변수
def info(**kwargs):
  print(kwargs)
info(name="woosik", age=20, gender="man") # 딕셔너리 형태로 받아주는 매개변수

def test():
  return (10,20), (10,30)

x, y = test()
print(x, y)

total = 20
def test2(x):
  global total
  total = total - x
  return total

test2(10)
print(total)

def add(a, b):
  return a+b

# 람다
# 함수명 = lambda 매개변수 : 리턴값
result = lambda a,b : a+b
print(result(10, 20 ))

# 콜백함수

def msg():
  print("lolololol")

def call_msg(i, func):
  for _ in range(i):
    func()
    
call_msg( 5, msg )

num = [1,2,3,4,5,6,7,8]
def is_even(n):
  return n % 2 == 0
# num에 있는 숫자들 중에서 짝수인것만 모아봄
# filter(함수, 리스트 or 튜플)
result = filter(is_even, num)
print(result)
print(list(result))

def po(n):
  return n * n
result = map(po, num)
print(result)
print(list(result))

# 중첩 함수
# 함수 내부에 새로운 함수를 정의
# 정의한 영역에서만 호출 가능
def outer_func(): # 함수
  print("outer_func!!!!")

  def inner_func(): # 중첩함수임
    return "inner func!!!!"
  
  print(inner_func())

outer_func()
# inner_func() 는 outer_func 내부에 선언되어있어서 호출 불가능함

def outer_func2(num): # 함수
  print("outer_func!!!!")

  def inner_func2(): # 중첩함수임
    print(num)
    return "inner func!!!!"
  
  return inner_func2

print("="*40)
fn = outer_func2(50) # first-class function
fn() # Closure 호출

"""
first-class funtion
- 함수를 변수에 저장
- 함수 인수를 다른 함수 인수로 전달
- 함수 리턴값이 함수로 함 

Closure
- 내부 함수를 구현하고 내부 함수를 리턴
"""
def square(n):
  return n * n

fn = square

print( fn(5) )

def html_creator(tag):
  def text_wrap(msg):
    print(f"<{tag}>{msg}</{tag}>")

  return text_wrap

h1_creator = html_creator('h1')
img_creator = html_creator('img')

h1_creator('h1태그는 제목태그임')
img_creator('img태그는 이미지를 넣을 수 있음')

del html_creator
#외부함수가 삭제되도 사용 가능함
h1_creator('ㅋㅋㅋㅋ')
img_creator('이것도 안되나??')

# 데코레이터 => 자바의 어노테이션임
import datetime

def logger_login():
  print( datetime.datetime.now() )
  print("login~~")
  print( datetime.datetime.now() )

logger_login()

# 데코레이터를 생성
def datetime_deco(func):
  def wrapper():
    print(datetime.datetime.now())
    func()
    print(datetime.datetime.now())
  return wrapper

@datetime_deco
def login():
  print("로그인을 시도합니다")

login()