for i in range(5):
    print('안녕하세요.')
    print (i)

print('-' * 20)

for num in range (2, 10, 2):
    print('num = ', num)

print('-' * 20)

num = int(input('메일 발송 횟수를 입력하세요.'))

for num in range(1, num+1, 1):
    print('메일 발송')

print('-' * 20)

for num in range(1,11,1):
    print('num =',num)
    if num % 7 == 0:
        print('7의 배수!')
