# Chapter09-02
# 2023/3/1
# CSV : 쉼표(또는 임의)로 구분이 되어있는 record set
# CSV 파일 읽기 및 쓰기

# CSV : MEME - text/csv

import csv

# 예제1
with open('/Users/inklee/Desktop/Python-basic/resource/test1.csv', 'r') as f:
	reader = csv.reader(f)
	next(reader) # Header Skip
	# 객체 확인
	print(reader)
	# 타입 확인
	print(type(reader))
	# 속성 확인
	print(dir(reader)) # __iter__ 가 있는지 확인 (있으면 for문 사용가능)

	for c in reader:
		# print(c) # 내용확인
		# 타입 확인(리스트)
		# print(type(c))
		# list to str
		print(' : '.join(c))

# 예제2
with open('/Users/inklee/Desktop/Python-basic/resource/test2.csv', 'r') as f:
	reader = csv.reader(f, delimiter='|') # 내가 지정한 기호로 구분되어있으면 그 기호를 적어서 사용

	for c in reader:
		print(c)

# 예제3
with open('/Users/inklee/Desktop/Python-basic/resource/test1.csv', 'r') as f:
	reader = csv.DictReader(f)
	# 확인
	print(reader)
	print(type(reader))
	print(dir(reader))
	print()

	for c in reader:
		for k,v in c.items():
			print(k,v)
		print('---------------')

# 예제4
w = [[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15],[16,17,18],[19,20,21]]

with open('/Users/inklee/Desktop/Python-basic/resource/write1.csv', 'w', encoding='utf-8') as f:
	print(dir(csv))
	wt = csv.writer(f)

	# dir 확인
	print(dir(wt))
	# 타입 확인
	print(type(wt))

	for v in w:
		wt.writerow(v)

# 예제5
with open('/Users/inklee/Desktop/Python-basic/resource/write2.csv', 'w', encoding='utf-8') as f:
	# 필드명
	fields = ['One', 'Two', 'Three']

	# Dict Writer
	wt = csv.DictWriter(f, fieldnames=fields)
	# Header Writer
	wt.writeheader()

	for v in w:
		wt.writerow({'One': v[0], 'Two': v[1], 'Three': v[2]})
