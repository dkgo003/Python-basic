# Chapter02-02-ex1
# 2023/2/24
# 파이썬 완전 기초
# Print 사용법
# 파이썬 3가지 print Formatting
# 자주 나오는 질문 참고

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

### 3가지 Format practices

x = 50
y = 100
text = 308276567
n = 'Lee'

# 출력1
ex1 = 'n = %s, s = %s, sum=%d' % (n, text, (x + y))
print(ex1)

# 출력2
ex2 = 'n = {n}, s = {s}, sum={sum}'.format(n=n, s=text, sum=x+y)
print(ex2)

# 출력3
ex3 = f'n = {n}, s = {text}, sum={x + y}'
print(ex3)
print(f'n = {n}, s = {text}, sum={x + y}') # 변수선언 안하고 바로 넣어도 같다.


# 구분기호
m = 100000000

print(f'm = {m:,}') # 금융관련 천단위 콤마구분기호 잘 인지

print()
print()

# 정렬
# ^ : 가운데정렬 , < : 왼쪽정렬 , > : 오른쪽정렬

t = 20

print(f"t = {t:10}")  # t:10 => 10칸을 확보해라
print(f"t center = {t:^10}") 
print(f"t center = {t:<10}")
print(f"t center = {t:>10}")  

print()
print()

print(f"t center : {t:*^10}")
print(f"t center : {t:#<10}")