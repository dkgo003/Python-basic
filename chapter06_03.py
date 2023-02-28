# Chapter06-03
# 2023/2/28
# 파이썬 패키지
# 패키지 작성 및 사용법
# 파이썬은 패키지로 분할 된 개별적인 모듈로 구성
# __init__.py : python 3.3 부터는 없어도 패키지로 인식 -> 단, 하위 호환을 위해 작성 추천
# 상대경로 : ..(부모 디렉토리) .(현재 디텍토리) -> 모듈 내부에서만 사용

# 예제1
import sub.sub1.module1  
import sub.sub2.module2

# 사용
sub.sub1.module1.mod1_test1() # import 는 패키지 경로를 풀네임으로 써줘야함 -> 비효율적
sub.sub1.module1.mod1_test2()

sub.sub2.module2.mod2_test1()
sub.sub2.module2.mod2_test2()

print()
print()
print()

# 예제2
from sub.sub1 import module1
from sub.sub2 import module2 as m2

module1.mod1_test1() # 간단히 호출 가능
module1.mod1_test2()

m2.mod2_test1() # 베스트 사용법 (원하는 폴더까지는 form 으로 접근한 뒤 
				#             import 로 모듈을 가져온 뒤 as 로 이름까지 변경)
m2.mod2_test2()

print()
print()
print()

# 예제3
from sub.sub1 import *   #   * : 폴더안의 모든 파일을 가져온다 (불피요한 작업이 될 수 있음)
from sub.sub2 import *

module1.mod1_test1()
module1.mod1_test2()

module2.mod2_test1()
module2.mod2_test2()