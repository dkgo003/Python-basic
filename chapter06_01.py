# Chapter06-01
# 2023/1/18
# 파이썬 클래스 및 모듈, 패키지
# 파이썬 클래스
# OOP(객체 지향 프로그래밍), Self, 인스턴트 메소드, 인스턴트 변수

# 클래스 and 인스턴스 차이 이해
# 네임스페이스 : 객체를 인스턴스화 할 때 저장된 공간
# 클래스 변수 : 직접 접근 가능, 공유
# 인스턴스 변수 : 객체마다 별도 존재

# 예제1
class Dog: # object 상속
    # 클래스 속성
    species = 'firstdog'

    # 초기화/인스턴트 속성
    def __init__(self, name, age):
        self.name = name
        self.age = age

print()

# 클래스 정보
print(Dog)

# 인스턴스화 # 인스턴스 - 코드를 직접 구현해서 메모리에 올라간 그 시점 / 변수로 활용할 수 있는 대상
a = Dog("mikky", 2)
b = Dog("baby", 3)
c = Dog("mikky", 2)

# 비교
print(a == b, id(a), id(b))
print(a == c, id(a), id(c)) # 인스턴스화 시킨것들은 다 id가 다르다

print()

# 네임스페이스
print('dog1', a.__dict__)
print('dog1', b.__dict__)

print()

# 인스턴스 속성 확인
print('{} is {} and {} is {}'.format(a.name, a.age, b.name, b.age))

if a.species == 'firstdog':
    print('{0} is a {1}'.format(a.name, a.species))

print(Dog.species) # 클래스로 바로 접근
print(a.species) # 인스턴스화 된 변수로 바로 접근
print(b.species)

print()

# 예제2
# self의 이해
# self : 인스턴스화 된 대상
class SelfTest:
    def func1():
        print('Func1 called')
    def func2(self):
        print(id(self))
        print('Func2 called')

# init 메소드가 없을시 파이썬이 알아서 만듬
f = SelfTest()

# print(dir(f)) # func1, func2 가 추가됨
print(id(f))
# f.func1() # 예외
f.func2()

print()

SelfTest.func1() # 클래스로 바로 접근해서 에러X
# SelfTest.func2() # 예외
SelfTest.func2(f)

print()

# 예제3
# 클래스 변수, 인스턴스 변수
class Warehouse:
    # 클래스 변수
    stock_num = 0 # 재고

    def __init__(self, name):
        # 인스턴스 변수
        self.name = name
        Warehouse.stock_num += 1

    def __del__(self):
        Warehouse.stock_num -= 1

user1 = Warehouse('Lee')
user2 = Warehouse('Cho')

print(Warehouse.stock_num)
# Warehouse.stock_num = 50
print(user1.name)
print(user2.name)
print(user1.__dict__)
print(user2.__dict__)
print('before', Warehouse.__dict__)
print('>>>', user1.stock_num)

print()

del user1
print('after', Warehouse.__dict__)

print()

# 예제4
class Dog: # object 상속
    # 클래스 속성
    species = 'firstdog'

    # 초기화/인스턴트 속성
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        return '{} is {} years old'.format(self.name, self.age)

    def speak(self, sound):
        return "{} says {}!".format(self.name, sound)

# 인스턴스 생성
c = Dog('July', 4)
d = Dog('Marry', 10)
# 메소드 호출
print(c.info())
# 메소드 호출
print(c.speak('Wal Wal'))
print(d.speak('Mung Mung'))

