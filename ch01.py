# 예제
if 4 in [1,2,3,4]: print("4가 있습니다")

# simple.py
languages = ['python', 'perl', 'c', 'java']

for lang in languages:
    if lang in ['python', 'perl']:
        print("%6s need interpreter" % lang)
    elif lang in ['c', 'java']:
        print("%6s need compiler" % lang)
    else:
        print("should not reach here")

# 사칙연산
1+2

3/2.4

3*9

# 변수에 숫자 대입하고 계산하기
a = 1
b = 2
a + b

# 변수에 문자 대입하고 출력하기
a = "Python"
print(a)

# 복소수
a = 2 + 3j
b = 3
a * b

# 조건문 if
a = 3
if a > 1:
    print("a is greater than 1")

# 반복문 for
for a in [1, 2, 3]:
    print(a)

# 반복문 while
i = 0
while i < 3:
    i = i + 1
    print(i)

# 함수
def sum(a,b):
    return a + b

print(sum(3,4))

#hello.py
print("Hello world")

# 주석처리
"""
Author: EungYong Park
Date : 2016-01-01
이 프로그램은 Hello World를 출력하는 프로그램이다.
"""
