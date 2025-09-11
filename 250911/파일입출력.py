# 파일 열기
# open(파일명, 모드, 인코딩)
# 작업 이후 close하기 
# 모드 : r - 읽기 모드, w - 쓰기 모드, a - 추가 모드
path = "C:/aaa/ppp/ww/dwx.png" #파일경로
path = r"C:\aaa\ppp\www\dd.png" 
f = open("test.txt", "w", encoding='utf-8')

print("abcde", file=f)
print("abcde", file=f)
print("안녕하세요 나는 메모장으로 들어갑니다", file=f)
f.write("한글은 안되는데요?\n")
f.write("hi my name is sik\n")

for i in range(5):
  f.write(f"{i} : 반복문임\n")

f.close()

f = open('test.txt', 'r', encoding='utf-8')
# a = f.read()
# print(a)
# print("="*200)

# 줄단위로 가져오기
while True:
  line = f.readline()
  print(line, end="")
  if not line:
    break
  
f.close()

# readline 는 실행할때마다 한줄씩 리턴
# readlines 는 각각 라인들을 list에 담아서 리턴 
f = open('test.txt', 'r', encoding='utf-8')
lines = f.readlines()
print(lines)
for line in lines:
  print(line, end='')
f.close()

f = open('test.txt', 'a', encoding='utf-8')
f.write("추가하기~~")

f.close()

# with 
with open('test.txt', 'a', encoding='utf-8') as f:
  f.write('with사용해보기~~\n')
  f.write('with사용해보기~~\n')

c = open('커피.txt', "r", encoding='utf-8')
with open('커피.txt', "r", encoding='utf-8') as c:
  lines = c.readlines()
  print(lines[0].split())

  for line in line:
    print(line, end='')
  