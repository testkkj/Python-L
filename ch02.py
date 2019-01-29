# 숫자형

# 정수형
a = 123
a = -178
a = 0

# 실수형
a = 1.2
a = -3.45

# 컴퓨터식 지수 표현 방식
a = 4.24E10
a = 4.24e-10

# 8진수와 16진수
a = 0o177
a = 0O177
b = 0x8ff
b = 0xABC

# 복소수
a = 1+2j
a = 3-4j

# 복소수.real은 복소수의 실수 부분을 리턴한다.
a = 1 + 2j
a.real

# 복소수.imag는 복소수의 허수 부분을 리턴한다.
a = 1 + 2j
a.imag

# 복소수.conjugate()는 복소수스이 켤레복소수를 리턴한다.
a = 1 + 2j
a.conjugate()

# abs(복소수)는 복소수의 절댓값을 리턴한다.
a = 1 + 2j
abs(a)

# 숫자형을 활용하기 위한 연산자

# 사칙연산
a = 3
b = 4
a + b
a * b
a / b

# x의 y제곱을 나타내는 ** 연산자
a = 3
b = 4
a ** b

# 나눗셈 후 나머지를 반환하는 % 연산자
7 % 3
3 % 7

# 나눗셈 후 소수점 아랫자리를 버리는 // 연산자
7 / 4
7 // 4

# 문자열 자료형

# 문자열
"Life is too short, You need Python"
"a"
"123"

# 큰따옴표로 양쪽 둘러싸기
"Hello World"

# 작은따옴표로 양쪽 둘러싸기
'Python is fun'

# 큰따옴표 3개를 연속으로 서서 양쪽 둘러싸기
"""Life is too short, You need Python"""

# 작은따옴표 3개를 연속으로 써서 양쪽 둘러싸기
'''Life is too short, You need Python'''

# 문자열에 작은따옴표 포함시키기
food = "Python's favorite food is perl"
food

# 문자열에 큰따옴표 포함시키기
say = '"Python is very easy." he says.'
say

# \를 이용해서 작은따옴표와 큰따옴표를 문자열에 포함시키기
food = 'Python\'s favorite food is perl'
say = "\"Python is very easy.\" he says."
food
say

# 여러 줄인 문자열을 변수에 대입하고 싶을 때

# 줄 바꾸기 \n
multiline = "Life is too short\nYou need python"
print(multiline)

# 연속된 ''' 또는 """ 이용
multiline = '''
Life is too short
You need python
'''
print(multiline)

multiline = """
Life is too short
You need python
"""
print(multiline)

# 문자열 연산하기

# 문자열 더해서 연결하기
head = "Python"
tail = " is fun!"
head + tail

# 문자열 곱하기
a = "python"
a * 2

# 문자열 곱하기 응용

# multistring.py
print("=" * 50)
print("My Program")
print("=" * 50)

# 문자열 인덱싱과 슬라이싱

# 문자열 인덱싱
a = "Life is too short, You need python"
a[3]

# 문자열 인덱싱 활용하기
a = "Life is too short, You need python"
a[0]
a[12]
a[-1]
a[-0]
a[-2]
a[-5]

# 문자열 슬라이싱
a = "Life is too short, You need python"
b = a[0] + a[1] + a[2] + a[3]
b
a = "Life is too short, You need python"
a[0:4]
a[0:3]
a[0:5]
a[0:2]
a[5:7]
a[12:17]
a[19:]
a[:17]
a[:]
a[19:-7]

# 슬라이싱으로 문자열 나누기
a = "20010331Rainy"
date = a[:8]
weather = a[8:]
date
weather

a = "20010331Rainy"
year = a[:4]
day = a[4:8]
weather = a[8:]
year
day
weather

# Pithon이라는 문자열을 Python으로 바꾸려면?
a = "Pithon"
a[1]
a[1] = 'y'

a = "Pithon"
a[:1]
a[2:]
a[:1] + 'y' + a[2:]

# 문자열 포매팅

# 숫자 바로 대입
"I eat %d apples." % 3

# 문자열 바로 대입
"I eat %s apples." % "five"

# 숫자 값을 나타내는 변수로 대입
number = 3
"I eat %d apples." % number

# 2개 이상의 값 넣기
number = 10
day = "three"
"I ate %d apples. so I was sick for %s days." % (number, day)

# %s 포맷 코드(자동으로 % 뒤의 값을 문자열로 바꿈)
"I have %s apples." % 3
"rate is %s" % 3.234

# 포매팅 연산자 %d와 %를 같이 쓸 때는 %%를 쓴다
"Error is %d%." % 98
"Error is %d%%." % 98

# 포맷 코드와 숫자 함께 사용하기

# 정렬과 공백
"%10s" % "hi"
"%-10sjane." % "hi"

# 소수점 표현하기
"%0.4f" % 3.42134234
"%10.4f" % 3.42134234

# 문자열 관련 함수들

# 문자 개수 세기
a = "hobby"
a.count('b')

# 위치 알려주기1(find)
a = "Python is best choice"
a.find('b')
a.find('k')

# 위치 알려주기2(index)
a = "Life is too short"
a.index('t')
a.index('k')

# 문자열 삽입(join)
a = ","
a.join('abcd')

# 소문자를 대문자로 바꾸기(upper)
a = "hi"
a.upper()

# 대문자를 소문자로 바꾸기(lower)
a = "HI"
a.lower()

# 왼쪽 공백 지우기(lstrip)
a = " hi"
a.lstrip()

# 오른쪽 공백 지우기(rstrip)
a = " hi "
a.rstrip()

# 양쪽 공백 지우기(strip)
a = " hi "
a.strip()

# 문자열 바꾸기(replace)
a = "Life is too short"
a.replace("Life", "Your leg")

# 문자열 나누기(split)
a = "Life is too short"
a.split()

a = "a:b:c:d"
a.split(':')

# 고급 문자열 포매팅

# 숫자 바로 대입하기
"I ate {0} apples".format(3)

# 문자열 바로 대입하기
"I ate {0} apples".format("five")

# 숫자 값을 가진 변수로 대입하기
number = 3
"I ate {0} apples".format(number)

# 2개 이상의 값 넣기
number = 10
day = "three"
"I ate {0} apples. so I was sick for {1} days.".format(number, day)

# 이름으로 넣기
"I ate {number} apples. so I was sick for {day} days.".format(number = 10, day = 3)

# 인덱스와 이름을 혼용해서 넣기
"I ate {0} apples. so I was sick for {day} days.".format(10, day = 3)

# 왼쪽 정렬
"{0:<10}".format("hi")

# 오른쪽 정렬
"{0:>10}".format("hi")

# 가운데 정렬
"{0:^10}".format("hi")

# 공백 채우기
"{0:=^10}".format("hi")
"{0:!<10}".format("hi")

# 소수점 표현하기
y = 3.42134234
"{0:0.4f}".format(y)
"{0:10.4f}".format(y)

# {,} 문자 표현하기
"{{and}}".format()

# 리스트 자료형

# 리스트는 어떻게 만들고 사용할까?
odd = [1,3,5,7,9]
a = []
b = [1,2,3]
c = ['Life', 'is', 'too', 'short']
d = [1, 2, 'Life', 'is']
e = [1, 2, ['Life', 'is']]

# 리스트의 인덱싱과 슬라이싱

# 리스트의 인덱싱
a = [1,2,3]
a
a[0]
a[0] + a[2]
a[-1]

a = [1,2,3,['a', 'b', 'c']]
a[0]
a[-1]
a[3]
a[-1][0]
a[-1][1]
a[-1][2]

# 삼중 리스트에서 인덱싱하기
a = [1, 2, ['a', 'b', ['Life', 'is']]]
a[2][2][0]

# 리스트의 슬라이싱
a = [1,2,3,4,5]
a[0:2]

a = "12345"
a[0:2]

a = [1,2,3,4,5]
b = a[:2]
c = a[2:]
b
c

# 중첩된 리스트에서 슬라이싱하기
a = [1,2,3,['a','b','c'],4,5]
a[2:5]
a[3][:2]

# 리스트 연산자

# 리스트 더하기
a = [1,2,3]
b = [4,5,6]
a+b

# 리스트 반복하기
a = [1,2,3]
a*3

# 초보자가 범하기 쉬운 리스트 연산 오류
a = [1,2,3]
a[2] + "hi"
str(a[2]) + "hi"

# 리스트의 수정, 변경과 삭제

# 리스트에서 하나의 값 수정하기
a = [1,2,3]
a[2] = 4
a

# 리스트에서 연속된 범위의 값 수정하기
a[1:2]
a[1:2] = ['a','b','c']
a
'''
a[1] = ['a','b','c']
a
결과값 : [1,['a','b','c'],4]
a[1:2] = ['a','b','c'] != a[1] = ['a','b','c,]
'''

# [] 사용해 리스트 요소 삭제하기
a[1:3] = []
a

# del 함수 사용해 리스트 요소 삭제하기
a
del a[1]
a

# 리스트 관련 함수들

# 리스트에 요소 추가
a = [1,2,3]
a.append(4)
a
a.append([5,6])
a

# 리스트 정렬
a = [1,4,3,2]
a.sort()
a

a = ['a','c','b']
a.sort()
a

# 리스트 뒤집기
a = ['a','b','c']
a.reverse()
a

# 위치 반환
a = [1,2,3]
a.index(3)
a.index(1)

# 리스트에 요소 삽입
a = [1,2,3,]
a.insert(0,4)
a.insert(3,5)
a

# 리스트 요소 제거
a = [1,2,3,1,2,3]
a.remove(3)
a.remove(3)
a

# 리스트 요소 끄집어내기
a = [1,2,3]
a.pop()
a

a = [1,2,3]
a.pop(1)
a

# 리스트에 포함된 요소 x의 개수 세기
a = [1,2,3,1]
a.count(1)

# 리스트 확장
a = [1,2,3]
a.extend([4,5])
a

b = [6,7]
a.extend(b)
a

# 튜플 자료형
t1 = ()
t2 = (1,)
t3 = (1,2,3)
t4 = 1,2,3
t5 = ('a','b',('ab','cd'))

# 튜플 요소값 삭제 시 오류
t1 = (1,2,'a','b')
del t1[0]

# 튜플 요소값 변경 시 오류
t1 = (1,2,'a','b')
del t1[0] - 'c'

# 튜플의 인덱싱과 슬라이싱, 더하기와 곱하기

# 인덱싱하기
t1 = (1,2,'a','b')
t1[0]
t1[3]

# 슬라이싱 하기
t1 = (1,2,'a','b')
t1[1:]

# 튜플 더하기
t2 = (3,4)
t1 + t2

# 튜플 곱하기
t2 * 3

# 딕셔너리 자료형
dic = {'name':'pey', "phone":'0119993323', 'birth':'1118'}
a = {1:'hi'}
a = {'a':[1,2,3]}
a

# 딕셔너리 쌍 추가, 삭제하기
a = {1:'a'}
a[2] = 'b'
a
a['name'] = 'pey'
a[3] = [1,2,3]
a

# 딕셔너리 요소 삭제하기
del a[1]
a

# 딕셔너리에서 Key 사용해 Value 얻기
grade = {'pey':10, 'julliet':99}
grade['pey']
grade['julliet']

a = {1:'a', 2:'b'}
a[1]
a[2]

a = {'a':1, 'b':2}
a['a']
a['b']

dic = {'name':'pey', 'phone':'0119993323', 'birth':'1118'}
dic['name']
dic['phone']
dic['birth']

# 딕셔너리 만들 때 주의할 사항
a = {1:'a', 1:'b'}
a

a = {[1,2]:'hi'}
a

# 딕셔너리 관련 함수들

# Key 리스트 만들기
a = {'name':'pey', 'phone':'0119993323', 'birth':'1118'}
a.keys()
for k in a.keys():
    print(k)
list(a.keys())

# Value 리스트 만들기
a.values()

# Key, Value 쌍 얻기
a.items()

# Key:Value 쌍 모두 지우기
a.clear()
a

# Key로 Value얻기
a = {'name':'pey', 'phone':'0119993323', 'birth':'1118'}
a.get('name')
a.get('phone')
a.get('nokey')
a.get('foo','bar')

# 해당 Key가 딕셔너리 안에 있는지 조사하기
a = {'name':'pey', 'phone':'0119993323', 'birth':'1118'}
'name' in a
'email' in a

# 집합 자료형
s1 = set([1,2,3])
s1

s2 = set("Hello")
s2

# 집합 자료형의 특징
s1 = set([1,2,3])
l1 = list(s1)
l1
l1[0]
t1 = tuple(s1)
t1
t1[0]

# 집합 자료형 활용하는 방법

# 교집합, 합집합, 차집합 구하기
s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8,9])

# 교집합
s1 & s2
s1.intersection(s2)
s2.intersection(s1)

# 합집합
s1 | s2
s1.union(s2)
s2.union(s1)

# 차집합
s1 - s2
s2 - s1
s1.difference(s2)
s2.difference(s1)

# 집합 자료형 관련 함수들

# 값 1개 추가하기
s1 = set([1,2,3])
s1.add(4)
s1

# 값 여러 개 추가하기
s1 = set([1,2,3])
s1.update([4,5,6])
s1

# 특정 값 제거하기
s1 = set([1,2,3])
s1.remove(2)
s1

# 자료형의 참과 거짓
a = [1,2,3,4]
while a:
    a.pop()
'''
while 조건문:
    수행할 문장
'''

if[]:
    print("True")
else:
    print("False")

if[1,2,3]:
    print("True")
else:
    print("False")

# 자료형의 값을 저장하는 공간, 변수
a = 1
b = "python"
c = [1,2,3]

# 파이썬에서 '3'은 상수가 아닌 정수형 객체이다
type(3)

a = 3
b = 3
a is b

# a,b,c는 정말 같은 객체를 가리키는 걸까?
import sys
sys.getrefcount(3)

a = 3
sys.getrefcount(3)

b = 3
sys.getrefcount(3)

c = 3
sys.getrefcount(3)

# 변수를 만드는 여러 가지 방법
a,b = ('python', 'life')
(a,b) = 'python', 'life'
[a,b] = ['python', 'life']
a = b = 'python'

a = 3
b = 5
a,b = b,a
a
b

# 메모리에 생성된 변수 없애기
a = 3
b = 3
del(a)
del(b)

# 리스트를 변수에 넣고 복사하고자 할 때
a = [1,2,3]
b = a
a[1] = 4
a
b

# [:] 이용
a = [1,2,3]
b = a[:]
a[1] = 4
a
b

# copy 모듈 이용
from copy import copy
b = copy(a)
b is a

##################################################
# 연습문제
##################################################
pin = "881120-1068234"
yyyymmdd = pin[:5]
num = pin[7:]
print(yyyymmdd)
print(num)

pin = "881120-1068234"
print(pin[7])

a = [1,3,5,4,2]
a.sort()
a.reverse()
print(a)

a = ['Life', 'is', 'too', 'short']      ##
result = " ".join(a)
print(result)

a = (1,2,3)     ##
a = a + (4,)
print(a)

a = {'A':90, 'B':80, 'C':70}        ##
result =a.pop('B')
print(a)
print(result)

a = [1,1,1,2,2,3,3,3,4,4,5]
aSet = set(a)
b = list(set(a))
print(b)

a = b = [1,2,3]
a[1] = 4
print(b)
'''
a와 b 모두 같은 객체[1,2,3]을 가르키고 있었기 때문에
'''