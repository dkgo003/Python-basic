# Chapter09-01
# 2023/3/1
# 파일 읽기 및 쓰기

# 읽기 모드 : r(read), 쓰기 모드 : w(write), 추가 모드 : a(append), 텍스트 모드 : t(기본값), 바이너리 모드 : b(지정값)
# 상대 경로('../, ./') , 절대 경로('C:\Django\example...')

# 파일 읽기(Read)
# 예제1

f = open('/Users/inklee/Desktop/Python-basic/resource/it_news.txt', 'r', encoding='UTF-8')
# f -> 외부에 있는 이 파일과 지금 현재 it_news파일과 연결해주는 그런 기능
# 속성 확인
print(dir(f))
# 인코딩 확인
print(f.encoding)
# 파일 이름
print(f.name)
# 모드 확인
print(f.mode)
# 내용 확인
cts = f.read()
print(cts)
# 반드시 close
f.close()

# 예제2
with open('/Users/inklee/Desktop/Python-basic/resource/it_news.txt', 'r', encoding='UTF-8') as f:
	c = f.read()
	print(c)
	print(iter(c))
	print(list(c))

print()

# 예제3
# read() : 전체 읽기 , read(10) : 10Byte 읽기
with open('/Users/inklee/Desktop/Python-basic/resource/it_news.txt', 'r', encoding='UTF-8') as f:
	c = f.read(20)
	print(c)
	c = f.read(20) # 마지막에 어디까지 읽었는지 내부적으로 기억한다.(커서)
	print(c)
	c = f.read(20)
	print(c)
	f.seek(0,0) # 다시 읽겠다. 처음으로 돌아간다.
	c = f.read(20)
	print(c)

print()

# 예제4
# readline : 한 줄 씩 읽기 (개행이 되기 전까지)
with open('/Users/inklee/Desktop/Python-basic/resource/it_news.txt', 'r', encoding='UTF-8') as f:
	line = f.readline()
	print(line)
	line = f.readline()
	print(line)

print()

# 예제5
# readlines : 전체를 읽은 후 라인 단위로 리스트로 저장 **
with open('/Users/inklee/Desktop/Python-basic/resource/it_news.txt', 'r', encoding='UTF-8') as f:
	cts = f.readlines() # 전처리 할 때 사용
	print(cts)
	print()
	for c in cts:
		print(c, end='')
	
print()

# 파일 쓰기(write)

# 예제1
with open('/Users/inklee/Desktop/Python-basic/resource/contents1.txt', 'w') as f:
	f.write('I love python\n')

# 예제2
with open('/Users/inklee/Desktop/Python-basic/resource/contents1.txt', 'a') as f:
	f.write('I love python2\n')

# 예제3
# writelines : 리스트 -> 파일
with open('/Users/inklee/Desktop/Python-basic/resource/contents2.txt', 'w') as f:
	list = ['Orange\n', 'Apple\n', 'Banana\n', 'Melon\n']
	f.writelines(list)

# 예제4 # 파일에 file 인자를 넣어서 연결하면 print 문이 내가 연결한 파일에 직접 출력
with open('/Users/inklee/Desktop/Python-basic/resource/contents3.txt', 'w') as f:
	print('Test Text Write!', file=f)
	print('Test Text Write!', file=f)
	print('Test Text Write!', file=f)