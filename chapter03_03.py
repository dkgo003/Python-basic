# Chapter03-03
# 2023/1/11
# 파이썬 기초 자료형
# 리스트(List)
# 자료구조에서 중요!
# 데이터 컨테이너
# 리스트 자료형 (순서O, 중복O, 수정O, 삭제O)

# 선언
a = []
b = list()
c = [70, 75, 80, 85] # Len = 4
d = [1000, 10000, 'Ace', 'Base', 'Captine'] # 서로 다른 자료형 List 안에 담기 가능
e = [1000, 10000, ['Ace', 'Base', 'Captine']] # 리스트 안에 리스트
f = [21.42, 'foobar', 3, 4, False, 3.14159]

# 인덱싱 - 내가 원하는 데이터를 꺼내오는 과정
print('>>>>>')
print('d - ', type(d), d)
print('d - ', d[1])
print('d - ', d[0] + d[1] + d[1])
print('d - ', d[-1])
print('e - ', e[-1][1])
print('e - ', type(e[-1][1]))
print('e - ', list(e[-1][1])) # 형 변환
print()

# 슬라이싱
print('>>>>>')
print('d - ', d[0:3])
print('d - ', d[2:])
print('e - ', e[-1][1:3])
print()

# 리스트
print('>>>>>')
print('c + d', c + d)
print('c * 3', c * 3)
print("'Test' + c[0]", 'Test' + str(c[0])) # 문자형이 맞지 않아서 형변환을 통해 맞춰주기
print()

# 값 비교
print(c == c[:3] + c[3:])
print(c)
print(c[:3] + c[3:])
print(c == c[:5])
print()

# Identity(id)
temp = c
print(temp, c)
print(id(temp))
print(id(c)) # 같은 id 값
print()

# 리스트 수정, 삭제
print('>>>>>')
c[0] = 4
print('c - ', c)
c[1:2] = ['a', 'b', 'c'] # 괄호가 2개면 c[1:2] = [['a', 'b', 'c']] => c -  [4, ['a', 'b', 'c'], 80, 85] -> 리스트안에 리스트
print('c - ', c)
c[1] = ['a', 'b', 'c'] # 리스트 안에 중첩
print('c - ', c)
c[1:3] = [] # 리스트 안에 원소를 삭제하기 : 실전에선 안씀
print('c - ', c)
del c[2] # 삭제
print('c - ', c)
print()

# 리스트 함수
a = [5, 2, 3, 1, 4]

print('a - ', a)
a.append(10) # append : 마지막 끝부분에 데이터 삽입 
print('a - ', a)
a.sort() # sort : 오름차순으로 정리
print('a - ', a) 
a.reverse() # reverse : 반대로 출력
print('a - ', a)
print('a - ', a.index(3), a[3])
a.insert(2, 7) # insert : insert(위치, 내가 추가할 값) -> 데이터 삽입
print('a - ', a) 
a.reverse()
print('a - ', a)
a.sort()
print('a - ', a) 
a.remove(10) # remove : 데이터를 선택해서 삭제
print('a - ', a)
print('a - ', a.pop()) # pop : 기존의 리스트에서 마지막 인덱스의 원소를 가져오고 나머지 원소들로 list를 다시 구성해서 출력
print('a - ', a)
print('a - ', a.pop())
print('a - ', a)
print('a - ', a.count(4)) # count : count(데이터) 의 개수가 몇개가 중복되어 있는지 or 있는지 없는지 찾을때 사용
print('a - ', a)
ex = [8, 9]
a.extend(ex)
print('a - ', a)
print()

# 삭제 : removem, pop, del

# 반복문 활용
while a:
    data = a.pop()
    print(data)

