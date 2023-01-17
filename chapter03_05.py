# Chapter03-05
# 2023/1/12
# 파이썬 기초 자료형
# 딕셔너리
# 범용적으로 가장 많이 사용 (JSON)
# 딕셔너리 자료형 (순서X, 키key 중복X, 수정O, 삭제O)

# 선언
# a = {'name': 'Kim'} # {'키': '밸류'} 키는 어떤 자료형이던 가능하다
a = {'name': 'Kim', 'phone': '01090928405', 'birth': '970427'}
b = {0: 'Hello Python'}
c = {'arr': [1, 2, 3, 4]}
d = {
    'Name': 'Niceman',
    'City': 'Seoul',
    'Age': 27,
    'Grade': 'A',
    'Status': True
}
e = dict([
    ('Name', 'Niceman'),
    ('City', 'Seoul'),
    ('Age', 27),
    ('Grade', 'A'),
    ('Status', True)
])
f = dict(
    Name='Niceman',
    City='Seoul',
    Age=27,
    Grade='A',
    Status=True
)

print('a - ', type(a), a)
print('b - ', type(b), b)
print('c - ', type(c), c)
print('d - ', type(d), d)
print('e - ', type(e), e)
print('f - ', type(f), f)
print()

# 출력
print('a - ', a['name']) # 존재X -> 에러 발생
print('a - ', a.get('name')) # get함수를 사용시 키가 없을때 None로 나옴 -> 에러가 발생하지 않음 -> 좀더 안정적인 코딩이 가능 
print('b - ', b[0])
print('b - ', b.get(0))
print('f - ', f.get('City'))
print('f - ', f.get('Age'))
print()

# 딕셔너리 추가
a['address'] = 'seoul' # 추가
print('a - ', a)
# a['name'] = 'seoul' # 만약 기존 키를 다시 사용하면 덧씌워서 수정
a['rank'] = [1, 2, 3]
print('a - ', a)
print()

# 딕셔너리 길이
print('a - ', len(a))
print('b - ', len(b))
print('c - ', len(c))
print('d - ', len(d))
print()

# dict_keys, dict_values, dict_items : 반복문(__iter__)에서 사용 가능
print('a - ', a.keys()) # 키들만 가져옴
print('b - ', b.keys())
print('c - ', c.keys())
print('d - ', d.keys())
print()

print('a - ', list(a.keys()))
print('b - ', list(b.keys()))
print()

print('a - ', a.values()) # 값들만 가져옴
print('b - ', b.values())
print('c - ', c.values())
print()

print('a - ', list(a.values())) 
print('b - ', list(b.values()))
print()

print('a - ', a.items()) # 둘다 가져옴
print('b - ', b.items())
print('c - ', c.items())
print()

print('a - ', list(a.items())) 
print('b - ', list(b.items()))
print()

print('a - ', a.pop('name'))
print('a - ', a)
print('c - ', c.pop('arr'))
print('c - ', c)
print()

print('f - ', f.popitem()) # 랜덤으로 하나 호출
print('f - ', f)
print('f - ', f.popitem())
print('f - ', f)
print('f - ', f.popitem())
print('f - ', f)
print('f - ', f.popitem())
print('f - ', f)
print('f - ', f.popitem())
print('f - ', f)
print()

print('a - ', 'birth' in a) # in 연산자 - 딕셔너리에서 키를 포함하고 있는지 조회 - 대소문자 구분함
print('d - ', 'City' in d)
print()

# 수정
a['test'] = 'test_dict'
print('a - ', a)

a['address'] = 'dj'
print('a - ', a)

a.update(birth='910904')
print('a - ', a)

temp = {'address' : 'Busan'}
a.update(temp)
print('a - ', a)


