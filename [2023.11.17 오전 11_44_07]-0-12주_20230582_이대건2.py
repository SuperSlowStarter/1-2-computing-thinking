for n1 in range (2, 10, 1):
    for n2 in range (1, 10, 1):
        print(n1, end='')
        print('*', end='')
        print(n2, end='')
        print('=', end='')
        print(n1 * n2)
    print()
