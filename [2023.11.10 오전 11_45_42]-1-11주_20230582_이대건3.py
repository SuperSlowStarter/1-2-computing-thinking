n1 = int(input('몇 단을 출력할까요?(숫자로 입력하세요) : '))

for n2 in range(1, 10, 1):
    print(n1, end='')
    print(' * ', end='')
    print(n2, end='')
    print(' = ', end='')
    print(n1 * n2)
