for num in range(1,6,1):
    print(num)
else:
    print('--------------')

for num in range(1, 11, 1):
    if num % 2 == 0:
        continue
    print(num)
    print('--------------')

for num1 in range(1,6,1):
    for num2 in range(num1):
        print('*', end = '')
    print()
