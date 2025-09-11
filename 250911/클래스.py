class Dog: # Dog 클래스 만들거임
  def __init__(self, name):  # 생성자
    self.name = name # 멤버 변수  
    self.age = 10    # 멤버 변수

  def show_info(self):  # 메서드
    print(f"이름 : {self.name}, 나이 : {self.age}")

  def plus(self, num):
    self.age += num
    
dog = Dog("밤비")
print(dog.name, dog.age)
# 동적으로 추가가 가능하긴 하지만 유지보수에 문제가 있으므로 
# 잘 사용하지는 않음 
dog.gender = "남" 
print(dog.gender)

"""
__init__ , __xxx__ : 매직 메서드, 특수 메서드, 던더 메서드 
특정 상황에서 파이썬이 자동으로 호출하거나 인식하는 메서드 

매개변수의 self
- 파이썬은 메서드 호출하면 자기자신(객체)가 첫번째로 인수로 전달
- 자동으로 인식해주는 this가 없어서, 명시를 해야함 
"""

dog.plus(5)
dog.show_info()

# 클래스 변수 ( static ) 
class Counter:
  total = 0 # 클래스 변수

  def __init__(self):
    self.value = 0 # 멤버 변수

  def plus(self):
    self.value += 1
    Counter.total += 1

counter1 = Counter()
counter2 = Counter()

print(counter1.value, counter1.total)
print(counter2.value, counter2.total)
print("="*40)
counter1.plus()
counter1.plus()

print(counter1.value, counter1.total)
print(counter2.value, counter2.total)

# 클래스 변수는 객체를 통해서 접근하는 것 보다는 
# 클래스 명으로 접근하는걸 권장
# 자바에서 static 변수같은거임 
print( Counter.total )

# 클래스 메서드, 정적 메서드
class Calc:
  pi = 3.14

  def circle(self, r):
    return r * r * self.pi
  
  @classmethod
  def circle2(cls, x): # 클래스 메서드
    return x * cls.pi
  
  @staticmethod
  def is_num(n): # 정적 메서드
    return n > 0
  
calc = Calc()
print( calc.circle(3) ) # 인스턴스 메서드 

# 클래스 메서드 : cls매개변수로 클래스 상태 접근
#               객체 생성용 보조 생성자
print( Calc.circle2(10) ) # 클래스 메서드
# 정적 메서드 : 기능, 유틸 관련 메서드
print( Calc.is_num(-20) ) # 정적 메서드

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  @classmethod
  def create(cls, name, year):
    from datetime import date
    age = date.today().year - year

    return cls(name, age)
  
p = Person.create("woosik", 1997)
print(p.name, p.age)

# 자바에서 toString?? 
# __repr__, __str__ 
class Point:
  def __init__(self, x, y):
    self.x = x 
    self.y = y
  def __repr__(self):
    return f"Point(x={self.x}, y={self.y})"
  def __str__(self):
    return f"({self.x}, {self.y})"
    
p = Point(5, 10)
print(p) # -> __str__ 호출
print( [p] ) # -> __repr__ 호출
    
"""
__str__ : 사용자용 문자열 리턴 ( 사용자 친화적 )
         사람이 보기 편한 데이터형태로 출력해주는게 목적
__repr__: 개발자용 문자열 리턴 ( 개발자 친화적 )
         이게 무슨 객체인지를 알 수 있게 정보를 담는게 목적
"""

# 자바에서 접근제한자가 있었는데 
# 파이썬은 없음 하지만 관례는 있음 
# 관례 : _변수명 - protected, __변수명 - private
class Person:
  def __init__(self, age):
    self._age = None
    self.age = age

  @property
  def age(self):
    print("getter 실행")
    return self._age
  
  @age.setter
  def age(self, value):
    print("setter 실행")
    if value < 0 :
      raise ValueError("나이는 음수 불가능")
    self._age = value

print("="*40)
person = Person(20)
person.age = 100
print(person.age)
print(person._age)

# 상속
class Animal:
  def __init__(self, name):
    self.name = name
  
  def sound(self):
    return "???"
  
class Cat(Animal):
  def __init__(self, name, color):
    super().__init__(name) # 부모생성자 호출
    self.color = color
  
  def sound(self): # 메서드 오버라이딩
    return "야옹"
  
cat = Cat("나비", "치즈")
print( cat.name, cat.color)
print( cat.sound() )