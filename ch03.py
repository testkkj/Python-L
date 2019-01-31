# 프로그램의 구조를 쌓는다! 제어문

# if문
money = 1
if money:
    print("택시를 타고 가라")
else:
    print("걸어 가라")

# if문의 기본 구조
'''
if 조건문:
    수행할 문장1
    수행할 문장2
    ...
else:
    수행할 문장1
    수행할 문장2
    ...
'''

# 들여쓰기
'''
money = 1
if money:
    print("택시를")
print("타고")   # 오류발생
    print("가자)

money = 1
if money:
    print("택시를")
    print("타고")
        print("가자)   # 오류발생
'''

# 조건문이란 무엇인가?
'''
자료형        참          거짓
숫자          0이외       0
문자열        "abc"       ""
리스트        [1,2,3]     []
튜플          (1,2,3)     ()
딕셔너리      {"a":"b"}   {}
'''

# 비교연산자
'''
x<y
x>y
x==y
x!=y
x>=y
x<=y
'''

x = 3
y = 2
x>y
x<y
x==y
x!=y

money = 2000
if money >= 3000:
    print("택시를 타고 가라")
else:
    print("걸어 가라")

# and, or, not
'''
x or y : 둘중하나만 참이면 참
x and y : 둘다 참이면 참
not x : x가 거짓이면 참
'''

money = 2000
card = 1
if money >= 3000 or card:
    print("택시를 타고 가라")
else:
    print("걸어 가라")

# x in s, x not in s
'''
in                  not in
x in 리스트         x not in 리스트
x in 튜플           x not in 튜플
x in 문자열         x not in 문자열
'''

1 in [1,2,3]
1 not in [1,2,3]

'a' in ('a','b','c')
'j' not in 'python'

pocket = ['paper', 'cellphone', 'money']
if 'money' in pocket:
    print("택시를 타고 가라")
else:
    print("걸어 가라")

# 조건문에서 아무 일도 하지 않게 설정하고 싶다면?
'''
pocket = ['paper', 'cellphone', 'money']
if 'money' in pocket:
    pass
else:
    print("걸어 가라")
'''

# 다양한 조건을 판단하는 elif
pocket = ['paper', 'cellphone']
card = 1
if 'money' in pocket:
    print("택시를 타고 가라")
else:
    if card:
        print("택시를 타고 가라")
    else:
        print("걸어 가라")

pocket = ['paper', 'cellphone']
card = 1
if 'money' in pocket:
    print("택시를 타고 가라")
elif card:
    print("택시를 타고 가라")
else:
    print("걸어 가라")

# if문을 한 줄로 작성하기
'''
if 'money' in pocket:
    pass
else:
    print("카드를 꺼내라")

if 'money' in pocket: pass
else: print("카드를 거내라")
'''

# while문
'''
while 조건문:
    수행할 문장1
    수행할 문장2
    수행할 문장3
    ...
'''

treeHit = 0
while treeHit < 10:
    treeHit = treeHit + 1
    print("나무를 %d번 찍었습니다." % treeHit)
    if treeHit == 10:
        print("나무 넘어 갑니다.")

# while문 직접 만들기
prompt = """
1. Add
2. Del
3. List
4. Quit

Enter number:"""

number = 0
while number != 4:
    print(prompt)
    number = int(input())

# while문 강제로 빠져나가기
coffee = 10
money = 300
while money:
    print("돈을 받았으니 커피를 줍니다.")
    coffee = coffee - 1
    print("남은 커피의 양은 %d개입니다." % coffee)
    if not coffee:
        print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
        break

# break문 이용해 자판기 작동 과정 만들기
# coffee.py
coffee = 10
while True:
    money = int(input("돈을 넣어 주세요: "))
    if money == 300:
        print("커피를 줍니다.")
        coffee = coffee - 1
    elif money > 300:
        print("거스름돈 %d를 주고 커피를 줍니다." % (money - 300))
        coffee = coffee - 1
    else:
        print("돈을 다시 돌려주고 커피를 주지 않습니다.")
        print("남은 커피의 양은 %d개 입니다." % coffee)
    if not coffee:
        print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
        break

# 조건에 맞지 않는 경우 맨 처음으로 돌아가기
a = 0
while a < 10:
    a = a + 1
    if a % 2 == 0: continue
    print(a)

# 무한 루프
'''
while True:
    수행할 문장1
    수행할 문장2
'''

while True:
    print("Ctrl+C를 눌러야 while문을 빠져 나갈 수 있습니다.")

# for문
'''
for 변수 in 리스트(또는 튜플, 문자열):
    수행할 문장1
    수행할 문장2
    ...
'''

# 전형적인 for문
test_list = ['one', 'two', 'three']
for i in test_list:
    print(i)

# 다양한 for문의 사용
a = [(1,2),(3,4),(5,6)]
for (first, last) in a:
    print(first + last)

# for문의 응용
# marks1.py
marks = [90, 25, 67, 45, 80]
number = 0
for mark in marks:
    number = number + 1
    if mark >= 60:
        print("%d번 학생은 합격입니다." % number)
    else:
        print("%d번 학생은 불합격입니다." % number)

# for문과 continue

# marks2.py
marks = [90, 25, 67, 45, 80]
number = 0
for mark in marks:
    number = number + 1
    if mark < 60:
        continue
    print("%d번 학생 축하합니다. 합격입니다." % number)

# for와 함께 자주 사용하는 range함수
a = range(10)
a
a = range(1, 11) # 끝 숫자는 포함되지 않음
a

# range 함수의 예시 살펴보기
sum = 0
for i in range(1,11):
    sum = sum + i
print(sum)

# marks3.py
marks = [90, 25, 67, 45, 80]
for number in range(len(marks)):
    if marks[number] < 60:
        continue
    print("%d번 학생 축하합니다. 합격입니다." % (number + 1))

# for와 range를 이용한 구구단
for i in range(2, 10):
    for j in range(1, 10):
        print(i * j, end = " ")
    print('')

# 입력 인수 end를 넣어 준 이유는 무엇일까?
'''
print(i * j, end = " ") 결과값 출력시 다음줄로 넘기지 않기위해(2 4 6 8 10 ...)
print('') 두번째 포문이 끝나면 줄을 넘어가기 위해
'''

# 리스트 안에 for문 포함하기
a = [1, 2, 3, 4]
result = []
for num in a:
    result.append(num*3)
print(result)

result = [num * 3 for num in a]
print(result)

result = [num * 3 for num in a if num % 2 == 0]
print(result)

'''
[표현식 for 항목 in 반복 가능 객체 if 조건]
[표현식 for 항목1 in 반복 가능 객체1 if 조건1
        for 항목2 in 반복 가능 객체2 if 조건2
        ...
        for 항목n in 반복 가능 객체n if 조건n]
'''

result = [x * y for x in range(2, 10)
                    for y in range(1, 10)]
print(result)

##################################################
# 연습문제
##################################################
a = "Life is too short, you need python"
if "wife" in a: print("wife")
elif "python" in a and 'you' not in a: print("python")
elif "shirt" not in a: print("shirt")
elif "need" in a: print("need")
else: print("none")

i = 0
while True:
    i += 1
    if i > 5: break
    print("*"*i)

A = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]       ##
total = 0
for score in A:
    total += score
average = total / len(A)
print(average)
