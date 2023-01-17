# Chapter02-02
# 2023/1/6
# 파이썬 완전 기초
# 파이썬 변수

# 기본 선언
n = 700

# 출력
print(n)
print(type(n)) # type함수 : n 이라는 변수에 할당되어 있는 값의 자료형을 보여줌 ('int' - 정수형)
print()

# 동시 선언
x = y = z = 700
print(x, y, z)
print()

# 선언
var = 75

# 재선언
var = "Change Value" # 마지막에 선언한 것이 기존에 선언한 것을 덮어씌운다.

# 출력
print(var)
print(type(var)) # 'str' - 문자형
print()

# Object References
# 변수 값 할당 상태
# 1. 타입에 맞는 오브젝트 생성
# 2. 값 생성
# 3. 콘솔 출력

# 예1)
print(300)
print(int(300))
print()

# 예2)
# n -> 777
n = 777

print(n, type(n))
print()

m = n
# m -> 777 <- n

print(m, n)
print(type(m), type(n))
print()

m = 400
print(m, n)
print(type(m), type(n))
print()

# id(identity)확인: 객체의 고유값 확인

m = 800
n = 655

print(id(m))
print(id(n))
print(id(m) == id(n))
print()

# 같은 오브젝트 참조
m = 800 
n = 800 # 하나의 오브젝트로 생성해버림

print(id(m))
print(id(n))
print(id(m) == id(n))
print()

# 다양한 변수 선언 방법
# Camel Case : numberOfCollegeGraduates -> Method 선언시
# Pascal Case : NumberOfCollegeGraduates -> Class 선언시
# Snake Case : number_of_college_graduates -> 추천하는 형태

# 허용하는 변수 선언 법
age = 1
Age = 2
aGe = 3
AGE = 4
a_g_e = 5
_age = 6
age_ = 7
_AGE_ = 8  # 변수 허용은 문자나 밑줄(_)
print(_AGE_) 
print()

# 예약어는 변수명으로 불가능
# 인터넷에서 python reserved words
""" 
False       def 	    if  	    raise
None	    del 	    import	    return
True	    elif	    in	        try
and	        else	    is	        while
as	        except	    lambda  	with
assert	    finally	    nonlocal	yield
break	    for 	    not	
class	    from	    or	
continue	global	    pass
"""




