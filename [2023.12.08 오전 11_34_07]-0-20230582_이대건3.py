num = 10

def fun1():
    global num
    num = 20
    print('함수 안 num:', num)

print('함수 밖 num:', num)
fun1()
print('함수 밖 num:', num)

print('-------------------------')

def greet(age, name, pay=200):
    print(age, '세', name, '씨, 안녕하세요.')
    print('월급:', pay)

greet(20, '홍길동', 400)
greet(pay=300, age=22, name='박찬호')
greet(30, '박지성', 700)
print('-------------------------')

def addFunction(n1, n2):
    sum = n1 + n2
    return sum

result = addFunction(10, 20)
print(result)

def add(n1, n2):
    print(n1+n2)

num1 = int(input('숫자를 입력하세요: '))
num2 = int(input('숫자를 입력하세요: '))
add(num1, num2)

print('-------------------------')
#return의 또다른 역할은 함수의 실행을 중단한다는 것

def increaseStar():
    print('*')
    print('**')
    print('***')
    return
    print('****')
    print('*****')
    print('******')
    print('*******')

increaseStar()
