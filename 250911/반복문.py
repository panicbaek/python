# # while 문
# """
# 조건식이 true일때 반복
# while 조건식 :
#   반복할 코드
# """

# num = 1
# sum = 0

# while num <= 10 :
#   print(f"숫자 : {num}")
#   sum += num
#   num += 1

# # print(f"총 합계 : {sum}")

# # # 1~10까지 반복하다가
# # # 입력받은 수의 배수면 반복 종료
# # num = 1 
# # i = int(input("숫자 입력 : "))

# # while num <= 10:
# #   print(f"숫자 : {num}")
# #   if num % i == 0:
# #     break
# #   num += 1
# # else:
# #   print("ㅋㅋㅋㅋㅋㅋㅋ")

#   # whileansdp else는 반복이 정상적으로 종료될 경우 실행할 코드를 넣을 수 있음
#   # break로 종료 시 작동 안함

#   # while True : 무한반복

#   # for 문
#   """
#   for 반복용변수 in 반복할객체 :
#     반복 실행할 코드
#   """

# list = ["aaa", "bbb", "ccc"]
# for i in list :
#   print(i)

# list = [(1,2), (50,100), (99, 5)]

# for i in list :
#   print(i)

# for (a, b) in list :
#   print(f"a : {a} | b : {b}")
#   print(f"a + b : {a+b}")

# # range 함수 
# # range( 시작, 끝, 증감) : 끝번호 전까지

# # 1부터 10까지 반복
# for i in range(1, 11):
#   print(i)

# print("="*20)
# for i in range(5):
#   print(i)

# print("="*20)
# for i in range(1, 10, 2):
#   print(i)

# dict = {
#   "name" : "woosik",
#   "age" : 20,
#   "addr" : "서울",
#   "gender" : "Man"
# }

# # 이건 유용하게 쓰일만하다
# for k in dict: # dict.keys()
#   print(k)
# for v in dict.values():
#   print(v)
# print(dict.items())
# for k, v in dict.items():
#   print(f"{k} : {v}")

# # 컴프리헨션 
# # for, if 한줄로 축약해서 만들고 새로운 리스트, 딕셔너리 등을 만들어주는 문법 
# a = [10, 20, 30, 40]
# result = []
# for i in a :
#   result.append( i * 2 )

# print(result)

# result2 = [ i * 2 for i in a]
# print(result2)

# # 컴프리헨션 선언문
# # 식 or for 반복변수 in 반복객체 if 조건식 

# result = [ i * 2 for i in a if i % 20 == 0 ]
# print(result)

# a = ["aa", "bb", "cc"]
# for i, data in enumerate(a):
#   print(f"반복인덱스 : {i}, 내용 : {data}")

# name = ["aa", "bb", "cc"]
# score = [100, 80, 90]
# for n, s in zip(name, score):
#   print(f"{n} : {s}")

# sun = 0
# for i in range(1, 101):
#   if i % 3 == 0 and i % 5 == 0 :
#     sum += i

# if sum % 2 == 0:
#   print("짝수")
# else:
#   print("홀수")

num = int(input("입력값 : ")) 
# 별 개수가 증가되는 반복문
for i in range(1, num+1, 2):
  sp = (num - i) // 2 # 공백수
  print(" " * sp + "*" * i)
# 별 개수가 감소되는 반복문
for i in range(num - 2, 0, -2):
  sp = (num - i) // 2 # 공백수
  print(" " * sp + "*" * i)
  
  