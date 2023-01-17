# Chapter02-01
# 2023/1/6
# 파이썬 완전 기초
# Print 사용법

# 기본 출력
print('Python Start!') # 선호
print("Python Start!")
print('''python Start!''')
print("""python Start!""")
print()

# separator 옵션 - 글자사이 넣기
print('P', 'Y', 'T', 'H', 'O', 'N', sep='')
print('010', '9092', '8405', sep='-')
print('python', 'google.com', sep='@')
print()

# end 옵션 - 이어쓰기
print('welcome to', end=' ')
print('IT News', end=' ')
print('Web Site')
print()

# File 옵션 - 파일이름저장
import sys

print('Learn Python', file=sys.stdout)
print()

# format 사용(d(정수:3), s(문자열:python), f(실수:3.14))
print('%s %s' % ('one', 'two'))
print('{} {}'.format('one', 'two'))
print('{1} {0}'.format('one', 'two'))
print()

# %s
print('%10s' % ('nice')) # 앞 비우기
print('{:>10}'.format('nice'))

print('%-10s' % ('nice')) # 뒤 비우기
print('{:10}'.format('nice')) 

print('{:$>10}'.format('nice')) # 앞에 문자넣기
print('{:^10}'.format('nice')) # 중앙정렬

print('%.5s' % ('nice'))
print('%.5s' % ('pythonstudy')) # . 붙여야 절삭가능 없을시 그대로 5글자 넘어서 출력
print('{:10.5}'.format('pythonstudy')) # 공간 남기기
print()

# %d
print('%d %d' % (1,2))
print('{} {}'.format(1,2))

print('%4d' % (42))
print('{:4d}'.format(42))
print()

# %f

print('%1.18f' % (3.1434343434343434))
print('{:f}'.format(3.14343434343434))
print('%06.2f' % (3.14159265258979)) # 0.6 -> 총 자리수 지정해줌 그래서 부족한 부분은 0으로 채움
print('{:06.2f}'.format(3.14159265258979))
print()
