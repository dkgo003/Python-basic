# Chapter06-02
# 2023/2/28
# 파이썬 모듈
# Module : 함수, 변수, 클래스 등 파이썬 구성 요소 등을 모아놓은 파일
# 재사용, 타인이 가져다 쓰기 가능

def add(x, y):
	return x + y

def subtract(x, y):
	return x - y

def multiply(x, y):
	return x * y

def divide(x, y):
	return x / y

def power(x, y):
	return x ** y

# 예약어를 사용해서 밑에 프린트문같은 필요없는 부분을 빼고 원하는 부분만 호출 가능

# print('-' * 15)
# print('called! inner!')
# print(add(5,5))
# print(subtract(15,5))
# print(multiply(5,5))
# print(divide(10,2))
# print(power(5,3))
# print('-' * 15)

# __name__ 사용
if __name__ == "__main__":  # 메인일 때에만 실행 . 모듈로 사용될때에는 실행되지않음
	print('-' * 15)
	print('called! __main__')
	print(add(5,5))
	print(subtract(15,5))
	print(multiply(5,5))
	print(divide(10,2))
	print(power(5,3))
	print('-' * 15)
