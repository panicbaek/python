import 패키지

print( __name__ )
print( 패키지.add(10, 20) )
print( 패키지.mul(10, 20) )
obj = 패키지.A()
print( obj.test() )

# 예외처리
# try:
#   예외발생될 가능성이 있는 코드
# except:
#   에외가 발생하면 실행할 코드
# finally:
#   항상 실행하는 코드

try:
  a = 4/2
except ZeroDivisionError as e:
  print("2로 안나눠 지면 나한테온다?")
else: # 정상적일떄 실행할 코드
  print("2로 나눠지면 나한테온다?")
finally:
  print("항상실행")

a=5
if a>=10:
  pass
else:
  pass