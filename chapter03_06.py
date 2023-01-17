# Chapter03-06
# 2023/1/12
# 파이썬 기초 자료형
# 집합(Set)의 특징
# 집합(Set) 자료형 (순서X, 중복X, 추가O, 삭제O)

# 선언
a = set()
b = set([1, 2, 3, 4])
c = set([1, 4, 5, 6])
d = set([1, 2, 'Pen', 'Cap', 'Plate'])
e = {'foo', 'bar', 'baz', 'foo', 'qux'} # key 없이 {}안에 리스트 나열하면 set
f = {42, 'foo', (1, 2, 3), 3.14159}

print('a - ', type(a), a)
print('b - ', type(b), b)
print('c - ', type(c), c)
print('d - ', type(d), d)
print('e - ', type(e), e)
print('f - ', type(f), f)
print()

# 튜플 변환(set -> tuple)
t = tuple(b)
print('t - ', type(t), t)
print('t -', t[0], t[1:3])
print()

# 리스트 변환(set -> list)
l = list(c)
l2 = list(e)
print('l - ', l)
print('l2 - ', l2)
print()

# 길이
print(len(a))
print(len(b))
print(len(c))
print(len(d))
print(len(e))
print(len(f))
print()

# 집합 자료형 활용
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

print('s1 & s2 : ', s1 & s2) # 교집합
print('s1 & s2 : ', s1.intersection(s2))
print()

print('s1 | s2 : ', s1 | s2) # 합집합
print('s1 | s2 : ', s1.union(s2))
print()

print('s1 - s2 : ', s1 - s2) # 차집합
print('s1 - s2 : ', s1.difference(s2))
print()

# 중복 원소 확인
print('s1 & s2 : ', s1.isdisjoint(s2)) # False - 교집합 되는 원소가 있다
print()

# 부분 집합 확인
print('subset : ', s1.issubset(s2)) # 부분 집합
print('superset : ', s1.issuperset(s2)) # 상위 집합
print()

# 추가 & 제거
s1 = set([1, 2, 3, 4])

s1.add(5)
print('s1 - ', s1)

s1.remove(2) # 없는걸 제거하면 예외(에러) 발생
print('s1 - ', s1)

s1.discard(4) # 예외(에러) 발생하지 않음 -> 안정성
print('s1 - ', s1)

s1.clear()
print('s1 - ', s1)


