# 함수

# 파이썬 함수의 구조
'''
def 함수명(입력 인수):
    수행할 문장1
    수행할 문장2
    ...
'''

def sum(a,b):
    return a + b

a = 3
b = 4
c = sum(a,b)
print(c)

# 입력값과 결과값에 따른 함수의 형태

# 일반적인 함수
'''
def 함수명(입력 인수):
    수행할 문장
    ...
    return 결과값
'''

def sum(a,b):
    result = a + b
    return result

a = sum(3,4)
print(a)

# 입력값이 없는 함수
def say():
    return 'Hi'

a = say()
print(a)

'''
결과값을 받을 변수 = 함수명()
'''

# 결과값이 없는 함수
def sum(a,b):
    print("%d, %d의 합은 %d입니다." % (a,b,a+b))
sum(3,4)

'''
함수명(입력 인수1, 입력 인수2, ...)
'''

a = sum(3,4)
print(a)

# 입력값도 결과값도 없는 함수
def say():
    print("Hi")

say()

'''
함수명()
'''

# 입력값이 몇 개가 될지 모를 때는 어떻게 해야 할까?
'''
del 함수명(*입력 변수):
    수행할 문장
    ...
'''

# 여러 개의 입력값을 받는 함수 만들기
def sum_many(*args):
    sum = 0
    for i in args:
        sum = sum + i
    return sum

result = sum_many(1,2,3)
print(result)

result = sum_many(1,2,3,4,5,6,7,8,9,10)
print(result)

def sum_mul(choice, *args):
    if choice == "sum":
        result = 0
        for i in args:
            result = result + i
    elif choice == "mul":
        result = 1
        for i in args:
            result = result * i
    return result

result = sum_mul('sum', 1,2,3,4,5)
print(result)

result = sum_mul('mul', 1,2,3,4,5)
print(result)

# 함수의 결과값은 언제나 하나이다
def sum_and_mul(a,b):
    return a+b, a*b

result = sum_and_mul(3,4)
print(result)
sum, mul = sum_and_mul(3,4)
print(sum, mul)

def sum_and_mul(a,b):
    return a+b
    return a*b

result = sum_and_mul(2,3)
print(result)
'''
def sum_and_mul(a,b):
    return a+b
    return a*b

위 함수는 아래와 동일하다.

def sum_and_mul(a,b):
    return a+b

return에서 함수를 빠져 나옴
'''

# return의 또 다른 쓰임새
def say_nick(nick):
    if nick == '바보':
        return
    print("나의 별명은 %s입니다." % nick)

say_nick('야호')
say_nick('바보')

# 입력 인수에 초기값 미리 설정하기
def say_myself(name, old, man=True):
    print("나의 이름은 %s입니다." % name)
    print("나이는 %d살입니다." % old)
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")

say_myself("박응용", 27)
say_myself("박응용", 27, True)

say_myself("박응선", 27, False)

# 함수 입력 인수에 초깃값을 설정할 때 주의할 사항
def say_myself(name, man=True, old):
    print("나의 이름은 %s입니다." % name)
    print("나이는 %d살입니다." % old)
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")

say_myself("박응용", 27)

# 함수 안에서 선언된 변수의 효력 범위
# vartest.py
a = 1
def vartest(a):
    a = a + 1

vartest(a)
print(a)

# vartest_error.py
def vartest(a):
    a = a + 1

vartest(3)
print(a)

# 함수 안에서 함수 밖의 변수를 변경하는 방법

# return 이용하기
# vartest_return.py
a = 1
def vartest(a):
    a = a + 1
    return a

a = vartest(a)
print(a)

# global 명령어 이용하기
# vartest_global.py
a = 1
def vartest():
    global a
    a = a + 1

vartest()
print(a)

# 사용자 입력과 출력

# 사용자 입력

# input의 사용
a = input()

# 프롬프트를 띄워서 사용자 입력 받기
number = input("숫자를 입력하세요: ")

print(number)

# print 자세히 알기
a = 123
print(a)

a = 'Python'
print(a)

a = [1,2,3]
print(a)

# 큰따옴표(")로 둘러싸인 문자열은 + 연산과 동일하다
print("life""is""too short")
print("life"+"is"+"too short")

# 문자열 띄어쓰기는 콤마로 한다
print("life","is","too short")
print("life", "is", "too short")

# 한 줄에 결과값 출력하기
for i in range(10):
    print(i, end='')

# 파일 읽고 쓰기

# 파일 생성하기
f = open("새파일.txt", 'w')
f.close()

'''
파일 열기 모드
r               읽기 모드 - 파일을 읽기만  할 때 사용
w               쓰기 모드 - 파일에 내용을 쓸 때 사용
a               추가 모드 - 파일의 마지막에 새로운 내용을 추가할 때 사용
'''

# 파일을 쓰기 모드로 열어 출력값 적기
# writedata.py
f = open("새파일.txt", 'w')
for i in range(1, 11):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()

# 프로그램의 외부에 저장된 파일을 읽는 여러 가지 방법

# readline() 함수 이용하기
# readline.py
f = open("새파일.txt",'r')
line = f.readline()
print(line)
f.close()

# readline_all.py
f = open("새파일.txt",'r')
while True:
    line = f.readline()
    if not line: break
    print(line)
f.close()

# readlines() 함수 이용하기
f = open("새파일.txt", 'r')
lines = f.readlines()
for line in lines:
    print(line)
f.close()

# read() 함수 이용하기
f = open("새파일.txt", 'r')
data = f.read()
print(data)
f.close()

# 파일에 새로운 내용 추가하기
# adddata.py
f = open("새파일.txt", 'a')
for i in range(11, 20):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()

# with문과 함께 사용하기
f = open("foo.txt", 'w')
f.write("Life is too short, you need python")
f.close()

with open("foo.txt", "w") as f:
    f.write("Life is too short, you need python")

##################################################
# 연습문제
##################################################
def fib(n):
    if n == 0: return 0
    if n == 1: return 1
    return fib(n-2) + fib(n-1)

for i in range(10):
    print(fib(i))

f = open("sample.txt")
lines = f.readlines()
f.close()

total = 0
for line in lines:
    score = int(line)
    total += score

average = total / len(lines)

f = open("result.txt", "w")
f.write(str(average))
f.close()