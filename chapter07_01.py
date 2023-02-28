# Chapter07-01
# 2023/2/28
# 파이썬 예외처리의 이해
# 예외 종류
# SyntaxError, TypeError, NameError, IndexError, ValueError, KeyError....
# 문법적으로는 예외가 없지만, 코드 실행 프로세스(단계)에서 발생하는 예외도 중요
# 1. 예외는 반드시 처리
# 2. 로그는 반드시 남긴다.
# 3. 예외는 던져진다.
# 4. 예외 무시


# SyntaxError : 문법 오류
# print('error)
# print('error'))
# if True
#     pass


# NameError : 참조 없음
# a = 10
# b = 15
# print(c)


# ZeroDivisionError
# print(100 / 0)


# IndexError
# x = [50, 70, 90]
# print(x[1])
# print(x[4])
# print(x.pop())
# print(x.pop())
# print(x.pop())
# print(x.pop()) # 인덱스 범위를 넘어가는 pop사용시 IndexError


# KeyError
# dic = {'name': 'Lee', 'Age': 41, 'City': 'Busan'}
# print(dic['hobby']) # KeyError
# print(dic.get('hobby')) # None 으로 표시 -> 실행가능


# 예외 없는 것을 가정하고 프로그램 작성 -> 런타임 예외 발생 시 예외 처리 권장(EAFP)


# AttributeError : 모듈, 클래스에 있는 잘못된 속성 사용 예외
import time
# print(time.time2())


# ValueError
# x = [10, 50, 90]
# x.remove(50)
# print(x)
# x.remove(200)

# FileNotFoundError
# f = open('test.txt') # 파일이 없을 때


# TypeError : 자료형에 맞지 않는 연산을 수행 할 경우
# x = [1,2]
# y = (1,2)
# z = 'test'

# print(x + y)
# print(x + z)
# print(y + z)

# print(x + list(y))
# print(x + list(z))


# 예외 처리 기본
# try : 에러가 발생 할 가능성이 있는 코드 실행
# except 에러명1(TypeError) : 여러개 가능
# except 에러명2 : 
# else : try 블록의 에러가 없을 경우 실행
# finally : 항상 실행

name = ['Kim', 'Lee', 'Park']

# 예제1
try:
	z = 'Lee' # 'Cho' 로 바꿀시 예외 발생 -> except로 넘어감
	x = name.index(z)
	print('{} Found it! {} in name'.format(z, x + 1))
except ValueError:
	print('Not found it! - Occurred ValueError')
else:
	print('Ok! else.')

print()

# 예제2
try:
	z = 'Kim' # 'Cho' 로 바꿀시 예외 발생 -> except로 넘어감
	x = name.index(z)
	print('{} Found it! {} in name'.format(z, x + 1))
except Exception:  # 모든 에러를 다잡음 -> 단점 : 어떤 에러가 발생 했는지를 알 수 없음
	print('Not found it! - Occurred ValueError')
else:
	print('Ok! else.')

print()

# 예제3
try:
	z = 'Cho' # 'Cho' 로 바꿀시 예외 발생 -> except로 넘어감
	x = name.index(z)
	print('{} Found it! {} in name'.format(z, x + 1))
except Exception as e:  # 에러의 내용을 출력할 때 as e 로 사용
	print(e)  
	print('Not found it! - Occurred ValueError')
else:  # 예외문이 발생하지 않아야 실행
	print('Ok! else.')
finally:  # 예외가 발생해도 항상 실행
	print('Ok! finally!')

print()

# 예제4
# 예외 발생 : raise
# raise 키워드로 예외 직접 발생

try:
	a = 'Park'
	if a == 'Kim':
		print('Ok! Pass!')
	else:
		raise ValueError  # a 가 Park 이 아닐시 강제로 ValueError로 예외 발생시켜버림
except ValueError:
	print('Occurred! Exception!')
else:
	print('Ok! else!')