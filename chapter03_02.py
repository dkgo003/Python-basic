# Chapter03-02
# 2023/1/10
# 파이썬 기초 자료형
# 문자형
# 문자형은 중요하다!

# 문자열 생성
str1 = "I am Python"
str2 = 'Python'
str3 = """How are you?"""
str4 = '''Thank you!'''

print(type(str1), type(str2), type(str3), type(str4))
print(len(str1), len(str2), len(str3), len(str4)) # 문자의 길이를 표현
print()

# 빈 문자열
str1_t1 = ''
str2_t2 = str()

print(type(str1_t1), len(str1_t1))
print(type(str2_t2), len(str2_t2))
print()

# 이스케이프 문자 사용
# I'm Boy

print("I'm Boy")
print('I\'m Boy')
print('I\\m Boy')
print('a \t b') # 탭키만큼 벌어짐
print('a \n b') # 줄바꿈
print('a \"\" b')

"""
참고 : Escape 코드

\n : 개행
\t : 탭
\\ : 문자
\' : 문자
\" : 문자
\000 : 널 문자
...

"""

escape_str1 = "Do you have a \"retro games\"?"
print(escape_str1)
escape_str2 = 'What\'s on TV?'
print(escape_str2)
print()

# 탭, 줄 바꿈
t_s1 = "Click \t Start!"
t_s2 = "New Line \n Check!"

print(t_s1)
print(t_s2)
print()

# Raw String
raw_s = r'D:\Python\test' # 이스케이프를 사용하지 않기위해 변수를 설정한것 (r로)
print(raw_s)
print()

# 멀티라인 입력
# 역슬래시 사용
multi_str = \
"""
문자열
멀티라인 입력
테스트
"""
# \로 문장을 마무리하면 이 다음에 어떤 변수를 바인딩을 한다라고 이해
print(multi_str)
print()

# 문자열 연산
str_o1 = "Python"
str_o2 = "Apple"
str_o3 = "How are you doing"
str_o4 = "Seoul Deajeon Busan Jinju"

print(str_o1 * 3)
print(str_o1 + str_o2)
print('y' in str_o1)
print('n' in str_o1)
print('z' in str_o1)
print('P' not in str_o2) # 대소문 구분
print()

# 문자열 형 변환
print(str(66), type(str(66)))
print(str(10.1))
print(str(True), type(str(True))) # str 안에 원하는 값을 넣어주면됨

# 문자열 함수(upper, isalnum, startwith, count, endswith, isalpha...)

print("Capitalize: ", str_o1.capitalize()) # 대문자로 바꿔줌
print("endswith?: ", str_o2.endswith("!")) # 문자의 끝이 무었인지 확인
print("replace", str_o1.replace("thon", ' Good')) # 문자 부분을 찾아 원하는 문자로 바꿔줌
print("sorted: ", sorted(str_o1))
print("split: ", str_o4.split(' ')) # split뒤에 넣어준 문자로 기존 문자열을 분리해준다.
print()

# 반복(시퀀스)
im_str = "Good Boy!"

print(dir(im_str)) # __iter__ 가 존재하면 시퀀스(반복)를 반복할 수 있다는 것

# 출력
for i in im_str:
    print(i)
print()

# 슬라이싱
str_s1 = "Nice Python"

print(len(str_s1))
# 슬라이싱 연습
print(str_s1[0:3]) # 3-1 까지 나오는것 -> 그니까 0, 1, 2 3개가 출력되야함
print(str_s1[5:11]) 
print(str_s1[5:]) # 둘이 같다
print(str_s1[:len(str_s1)]) # = str_s1[:11]
print(str_s1[1:9:2]) # 3번째 인수는 단위
print(str_s1[-5:])
print(str_s1[1:-2])
print(str_s1[::2]) # 처음부터 끝까지 2칸 간격으로 가져와라
print(str_s1[::-1]) # 음수는 오른쪽에서 왼쪽으로 역방향
print()

# 아스키 코드(또는 유니코드)
a = 'z'

print(ord(a)) # ord : 문자를 아스키 코드로 변환
print(chr(122)) # chr : 아스키 코드를 우리에게 변환해서 보여줌

